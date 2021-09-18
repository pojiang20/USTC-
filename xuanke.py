import ssl
import requests
import time
import json

# 处理ssl报错
ssl._create_default_https_context = ssl._create_unverified_context

# 课程ID和学生ID
# 实用算法137452 高级网络技术137461 形式化方法137457 辩证法137481
dataid=[137481]
studentId=452319
# 使用chrome查看，右键-检查-Application，即可在cookies看到session内容，session有一定的有效期，需要定期更换
session='69f32ad3-2a58-4f83-a6d9-5be6fe96db74'

# 设置Cookie
cookies={'_ga': 'GA1.3.723975782.1615628000',
'UM_distinctid': '172362ec9d635e-0ad71cfb6b0a8c-1633685b-1fa400-178762ec9d7629',
'SVRNAME': 'student1',
'SESSION': session}
# 打开日志记录
f=open("log.txt","a")

# 查询课程剩余数量
# url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/std-count'
# queryid=137481
# params={'lessonIds[]':queryid}
# # 发送请求
# r=requests.post(url,cookies=cookies,params=params)
# f.write("\n查询网站："+r.url+"\n查询时间："+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"\n课程剩余数量："+r.text)

success=False
cnt=0
while success==False:
    cnt=(cnt+1)%len(dataid)
    # 第一次请求获取返回码用于校验
    url = 'https://jw.ustc.edu.cn/ws/for-std/course-select/add-request'
    params={"studentAssoc":studentId,
    "lessonAssoc":dataid[cnt],
    "courseSelectTurnAssoc":481,
    "scheduleGroupAssoc": "" ,
    "virtualCost":0}
    resp=requests.post(url,cookies=cookies,params=params).text

    f.write(str(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime()))+"\n查询网站："+url+"\n查询返回码："+resp)
    # 第二次请求选课
    url= 'https://jw.ustc.edu.cn/ws/for-std/course-select/add-drop-response'
    params={"studentId":studentId,"requestId":resp}
    r=requests.post(url,cookies=cookies,params=params)

    j=json.loads(r.text,strict=False)
    success=j['success']
    errorMessage=j['errorMessage']
    f.write("\n查询网站："+r.url+"\n请求课程："+str(dataid[cnt])+"\n选课结果："+str(success)+"\n"+str(errorMessage)+"\n=========\n")
    # 设置一定的间隔时间，请求太快会导致还没有响应就读取数据，导致循环退出
    time.sleep(5)
