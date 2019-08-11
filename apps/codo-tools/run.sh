#!/usr/bin/env bash

#启动服务：
#如：故障管理、事件管理、提醒管理、告警管理、随机密码、加密解密
python3 startup.py --service=tools --port=8040

#启动定时检测任务
#如：每隔6小时去检测定时管理里面是否有要通知的提醒

#python3 startup.py --service=cron_jobs

for rtxt in $(find . -name 'requirements.txt' | awk '{print $1}') do echo $rtxt ; done  

for((i=1;i<=10;i++));  do   echo $(expr $i \* 3 + 1);  done  
for x in $(find . -name 'requirements.txt' | awk '{print $1}'); do echo '======'; done