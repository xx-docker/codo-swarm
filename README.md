# CODO 单机部署解决方案

## 仓库目录结构简单说明
```
[root@VastSpecific-VM codo-swarm]# tree -d -L 2
.
├── apps             python 的后台工具
│   ├── codo-admin   opendevops/codo-admin
│   ├── codo-cmdb    opendevops/codo-cmdb
│   ├── codo-cron    opendevops/codo-cron
│   ├── codo-dns     opendevops/codo-dns
│   ├── codo-task    opendevops/codo-task
│   ├── codo-tools   opendevops/codo-tools
│   └── kerrigan     opendevops/kerrigan
├── codo-ui       Codo-UI 对应的是 github 上的 opendevops/codo
│   ├── public
│   ├── src
│   └── tests
├── scripts  可以无视
│   └── v2
├── sql      数据库初始的内容
└── tengine  进行单机部署的Nginx配置
    └── vhosts

17 directories
```

## 快速开始
- 1, 拷贝仓库
```bash 
cd /home && \ 
git clone git@code.aliyun.com:xx-zhang/codo-swarm.git && mv codo-swarm opendevops
# 说明
## apps 下记录的是 python 后台的app; 
## codo-ui 记录的前台的代码。都没有修改。
## > 注意需要修改 codo-ui 的 vue.config.js 里面额后台地址为自己的IP
## > 也可以直接使用域名映射。当然生产环境中可以省掉。
```
- 2, 修改自己的个性化配置
> 注意观察 7个 python-apps 我们可以发现都 import local_settings.py 所以直接将 local_settings映射进去就行了。
> 在这里为了优化和简化配置，用户只需要修改 apps/config.yml 即可。
- [config.yml](./apps/config.yml)
- 修改这个文件后，local_settings.py 会加载进去。

- 3, 启动 docker-compose 
```bash 
cd /home/opendevops && docker-compose up -d 
```

- 4, 修改数据库
```bash 
# 第一步
cd /home/opendevops && \
docker cp /home/opendevops/sql mysql-server:/root && \
docker exec -it mysql-server bash 

# 第二步 进入mysql-server容器后进入root目录执行
# >>>>>>>>>>>>>>>容器环境>>>>>>>>>>>>>>>>>>>>
cd /root/
## 创建数据库
for x in $(find . -name *.sql); do mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "create database "$(echo $x | awk -F '-' '{print $1}' | awk -F '/' '{print $3}')" default character set utf8mb4 collate utf8mb4_unicode_ci;" ; done

## 初始化数据库
for x in $(find . -name *.sql); do mysql -uroot -p${MYSQL_ROOT_PASSWORD} $(echo $x | awk -F '-' '{print $1}' | awk -F '/' '{print $3}') < $x; done
# <<<<<<<<<<<<<<< 容器环境 <<<<<<<<<<<<<<<<<<<
```
- 5, 当前codo-ui为 dev run 
> 修改 ./codo-ui/vue.config.js 后的 
```javascript
devServer: {
    // proxy: 'http://172.16.0.223:9800/'
    proxy: 'http://<your-domain or ip>:10080/'
    // proxy: 'https://demo.opendevops.cn/api/'
  }
```

- 5, 其他说明
> 因为数据库 MYSQL_REDIS_MQ 都是开放的端口，如果不开放，可以设置对应的HOST; expose
 
## 使用的镜像说明
- rabbitmq:3-management 这个被 我的代替了
- actanble/codo-admin/base 代表的是基础镜像 构建环境就是 apps/Dockerfile 
- tengine 构建的是 xx-docker/Dockerfile 就是一个Nginx 环境
- redis/mysql 都是出自 library; 为了下载迅速全部通过xx-docker的github源转移重新编译了
- actanbe/codo-ui 对应的 codo-ui 下的编译环境。

## 其他修改; 可能用得上
```
## 解析域名到 etc/hosts 
- echo codo.actanble.org   192.168.2.228 >> /etc/hosts 

## 更换源
- sed -i 's/"actanble/codo-admin-base"/"registry.cn-hangzhou.aliyuncs.com/xxzhang/codo-base:0.0.3"/g' \
 docker-compose.yml  
```
## 参考信息
- [Docker-compose参考](https://github.com/zabbix/zabbix-docker/blob/4.2/docker-compose_v3_alpine_mysql_latest.yaml)