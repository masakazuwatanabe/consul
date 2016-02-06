#!/bin/sh


DIR_CURRENT=`pwd`


################################################################################
# consul latest / default ver.
################################################################################
cd ${DIR_CURRENT}/0.6/centos/7/consul
docker build -t docker.io/masakazuwatanabe/consul:latest .

cd ${DIR_CURRENT}/0.6/centos/7/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:latest .

cd ${DIR_CURRENT}/0.6/centos/7/consul-server
docker build -t docker.io/masakazuwatanabe/consul-server:latest .


################################################################################
# consul latest / centos 7 ver.
################################################################################
cd ${DIR_CURRENT}/0.6/centos/7/consul
docker build -t docker.io/masakazuwatanabe/consul:latest-centos7 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:latest-centos7 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-server
docker build -t docker.io/masakazuwatanabe/consul-server:latest-centos7 .


################################################################################
# consul latest / centos 6 ver.
################################################################################
cd ${DIR_CURRENT}/0.6/centos/7/consul
docker build -t docker.io/masakazuwatanabe/consul:latest-centos6 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:latest-centos6 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-server
docker build -t docker.io/masakazuwatanabe/consul-server:latest-centos6 .




################################################################################
# consul 0.6 / default ver. (centos 7)
################################################################################
cd ${DIR_CURRENT}/0.6/centos/7/consul
docker build -t docker.io/masakazuwatanabe/consul:0.6 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:0.6 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-server
docker build -t docker.io/masakazuwatanabe/consul-server:0.6 .


################################################################################
# consul 0.6 / centos 7 ver.
################################################################################
cd ${DIR_CURRENT}/0.6/centos/7/consul
docker build -t docker.io/masakazuwatanabe/consul:0.6-centos7 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:0.6-centos7 .

cd ${DIR_CURRENT}/0.6/centos/7/consul-server
docker build -t docker.io/masakazuwatanabe/consul-server:0.6-centos7 .



################################################################################
# consul 0.6 / centos 6 ver.
################################################################################
cd ${DIR_CURRENT}/0.6/centos/6/consul
docker build -t docker.io/masakazuwatanabe/consul:0.6-centos6 .

cd ${DIR_CURRENT}/0.6/centos/6/consul-client
docker build -t docker.io/masakazuwatanabe/consul-client:0.6-centos6 .

cd ${DIR_CURRENT}/0.6/centos/6/consul-server:0.6
docker build -t docker.io/masakazuwatanabe/consul-server:0.6-centos6 .





