FROM node:10.14

#RUN npm config set registry https://registry.npm.taobao.org

ARG PROGRAME_DIR=/var/www/codo-ui
ADD . ${PROGRAME_DIR}
WORKDIR ${PROGRAME_DIR}
RUN npm install --ignore-script

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "-vvv", "-g", "-w", "--"]

## Error Elint
CMD ['/usr/local/bin/npm', 'run', 'dev']
