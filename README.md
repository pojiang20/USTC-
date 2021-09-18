# USTC-xuanke
### 用途
中科大软件学院/科软抢课用。

#### ssh传输文件
- 本地复制到远程`scp local_file remote_username@remote_ip:remote_folder` 如`scp -r USTC root@121.40.127.98
- 远程复制到本地交换地址即可，`scp -r root@121.40.127.98 USTC`

#### 服务器后台挂起
- 后台挂起`$ nohup python3 -u xx.py > error.log 2>&1 &`，即可一直运行python程序，并且error.log文件记录异常信息。
![image](https://user-images.githubusercontent.com/25092256/133866374-7fcf8514-0288-4222-9159-32662049a283.png)

- `ps -ef|grep python` 查看python程序运行情况
- `kill -9 pid` 结束程序

#### log.txt日志记录
`cat log.txt` 即可查看
![image](https://user-images.githubusercontent.com/25092256/133866385-febcc49b-0b2e-4296-afb3-53ac3759e017.png)
