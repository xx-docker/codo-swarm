## 描述

- codo 前段展示。使用的框架是 vue2+iview
  - 跟 element-ui 差不多。

## Install
```bush
// install dependencies
npm install --ignore-script
```
## Run
### Development
```bush
npm run dev
```
### Production(Build)
```bush
npm run build
```

## 2019-8-9 Upgrade By actanble-Test - NOTE 必看
- 更新了脱离和Dockerfile
- 直接在 Docker 中构建的时候出现了问题。 所以选择在本地生成了 node_module 直接映射进去。
- NOTE: 先在本地执行环境 映射进去。
```bash 
#!/bin/bash 
## linux 下二进制安装 Node 

[ -f /usr/local/bin/node ] && echo "Node already exists" && exit -1
cd /usr/local/src && rm -rf node-v8.11.3-linux-x64.tar.xz
wget -q -c https://nodejs.org/dist/v8.11.3/node-v8.11.3-linux-x64.tar.xz
tar xf node-v8.11.3-linux-x64.tar.xz -C  /usr/local/ >/dev/null 2>&1
rm -rf /usr/local/bin/node
rm -rf /usr/local/bin/npm
ln -s /usr/local/node-v8.11.3-linux-x64/bin/node /usr/local/bin/node
ln -s /usr/local/node-v8.11.3-linux-x64/bin/node /usr/bin/node
ln -s /usr/local/node-v8.11.3-linux-x64/bin/npm  /usr/local/bin/npm
ln -s /usr/local/node-v8.11.3-linux-x64/bin/npm  /usr/bin/npm
/usr/local/bin/node -v
/usr/local/bin/npm -v
sudo npm i -g pm2 >/dev/null 2>&1
ln -s /usr/local/node-v8.11.3-linux-x64/bin/pm2 /usr/bin/
```
- npm install --ignore-script
- NOTE 国外的源进行npm run dev 我自己弄好了一个 actanble/

## License
[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2016-present, iView