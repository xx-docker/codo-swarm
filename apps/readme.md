## 将微服务全部打包到当前APP
- [codo](./codo)
- [codo-admin](./codo-admin)
- [codo-cmdb](./codo-cmdb)
- [codo-cron](./codo-cron)
- [codo-dns](./codo-dns)
- [codo-task](./codo-task)
- [codo-tools](./codo-tools)
- [kerrigan](./codo-tools)

## codo 生态单机打造
- [codo](http://docs.opendevops.cn/zh/latest/codo-admin.html)


## RUN - cat-startup-shells 
```
cat codo-admin/doc/supervisor_ops.conf | grep port
cat codo-cmdb/doc/supervisor_ops.conf | grep port
cat codo-task/doc/supervisor_ops.conf | grep port
cat kerrigan/doc/supervisor_ops.conf | grep port
cat codo-tools/doc/supervisor_ops.conf | grep port
cat codo-cron/doc/supervisor_ops.conf | grep port
cat codo-dns/doc/supervisor_ops.conf | grep port
```

## rebuild Dockerfile 

### 更新，拷贝文件到 apps
```bash 
yum -y install git 
cd apps && rm -rf * \ && \
git clone https://github.com/xx-codo/codo-admin \
git clone https://github.com/xx-codo/codo-cmdb \
git clone https://github.com/xx-codo/codo \
git clone https://github.com/xx-codo/codo-tools \
git clone https://github.com/xx-codo/codo-task \
git clone https://github.com/xx-codo/kerrigan \
git clone https://github.com/xx-codo/codo-cron \
git clone https://github.com/xx-codo/codo-dns \
```

## python-project 
- admin-settings 
- cmdb-settings 
- task-settings 

## Mysql 初始化 1
```bash
cd /home/opendevops
docker cp /home/opendevops/sql mysql-server:/root
docker exec -it mysql-server bash 
```
- 
- 接着执行下面的脚本

```bash
cd /root/
## 创建数据库
for x in $(find . -name *.sql); do mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "create database "$(echo $x | awk -F '-' '{print $1}' | awk -F '/' '{print $3}')" default character set utf8mb4 collate utf8mb4_unicode_ci;" ; done

## 初始化数据库
for x in $(find . -name *.sql); do mysql -uroot -p${MYSQL_ROOT_PASSWORD} $(echo $x | awk -F '-' '{print $1}' | awk -F '/' '{print $3}') < $x; done
```

## pymysql 来初始化 2

```bash 
cd apps && for x in $(find . -name 'db_sync.py' | awk '{print $1}'); do \
docker run -it -v /home/opendevops/apps:/home/opendevops/apps -w /home/opendevops/apps \
--rm registry.cn-hangzhou.aliyuncs.com/xxzhang/codo-base:v0.0.3 \
python3 $x; \
done
```

### docker-compose 映射IP升级管理
- codo-admim 
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.100:8010/are_you_ok/
- codo-cmdb 
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.102:8050/are_you_ok/
- codo-cron 
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.103:9900/are_you_ok/
- codo-dns 
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.104:8060/are_you_ok/
- codo-task 
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.105:8020/are_you_ok/
- codo-task-other/wx
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.108:8021/are_you_ok/
- codo-tools
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.110:8040/are_you_ok/
- kerrigan
  - curl -I -X GET -m 10 -o /dev/null -s -w %{http_code} http://192.168.235.112:8030/are_you_ok/