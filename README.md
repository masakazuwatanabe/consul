# consul docker container.

consul container. (env args)

## type

 - consul (default ver)
 - consul-client (client args ver)
 - consul-server (server args ver)

## tags latest (consul 0.6)

 - consul:latest (consul latest centos7 ver)
 - consul-client:latest (consul-client latest centos7 ver)
 - consul-server:latest (consul-server latest centos7 ver)

## tags latest (consul 0.6) other
 - consul:latest-centos7 (consul latest centos7 ver)
 - consul:latest-centos6 (consul latest centos6 ver)
 - consul-client:latest-centos7 (consul latest centos7 ver)
 - consul-client:latest-centos6 (consul latest centos6 ver)
 - consul-server:latest-centos7 (consul latest centos7 ver)
 - consul-server:latest-centos6 (consul latest centos6 ver) 

## tags 0.6
 - consul:0.6 (consul 0.6 centos7 ver)
 - consul:0.6-centos7 (consul 0.6 centos7 ver)
 - consul:0.6-centos6 (consul 0.6 centos6 ver)
 - consul-client:0.6 (consul-client 0.6 centos7 ver)
 - consul-client:0.6-centos7 (consul-client 0.6 centos7 ver)
 - consul-client:0.6-centos6 (consul-client 0.6 centos6 ver)
 - consul-server:0.6 (consul-server 0.6 centos7 ver) 
 - consul-server:0.6-centos7 (consul-server 0.6 centos7 ver) 
 - consul-server:0.6-centos6 (consul-server 0.6 centos6 ver) 

## environment

> Please refer to the official page of the consul.
> https://www.consul.io/docs/agent/options.html

  - CONSUL_CONFIG_DIR
  - CONSUL_DEV
  - CONSUL_ACL_DATACENTER
  - CONSUL_ACL_DEFAULT_POLICY
  - CONSUL_ACL_DOWN_POLICY
  - CONSUL_ACL_MASTER_TOKEN
  - CONSUL_ACL_MASTER_TOKEN
  - CONSUL_ACL_TOKEN
  - CONSUL_ACL_TTL
  - CONSUL_ADDRESSES_DNS
  - CONSUL_ADDRESSES_HTTP
  - CONSUL_ADDRESSES_HTTPS
  - CONSUL_ADDRESSES_RPC
  - CONSUL_ADVERTISE_ADDR
  - CONSUL_ADVERTISE_ADDRS_SERF_LAN
  - CONSUL_ADVERTISE_ADDRS_SERF_WAN
  - CONSUL_ADVERTISE_ADDRS_RPC
  - CONSUL_ADVERTISE_ADDR_WAN
  - CONSUL_ATLAS_ACL_TOKEN
  - CONSUL_ATLAS_INFRASTRUCTURE
  - CONSUL_ATLAS_JOIN
  - CONSUL_ATLAS_TOKEN
  - CONSUL_ATLAS_ENDPOINT
  - CONSUL_BOOTSTRAP
  - CONSUL_BOOTSTRAP_EXPECT
  - CONSUL_BIND_ADDR
  - CONSUL_CA_FILE
  - CONSUL_CERT_FILE
  - CONSUL_CHECK_UPDATE_INTERVAL
  - CONSUL_CLIENT_ADDR
  - CONSUL_DATACENTER
  - CONSUL_DATA_DIR
  - CONSUL_DISABLE_ANONYMOUS_SIGNATURE
  - CONSUL_DISABLE_REMOTE_EXEC
  - CONSUL_DISABLE_UPDATE_CHECK
  - CONSUL_DNS_CONFIG_ALLOW_STALE
  - CONSUL_DNS_CONFIG_MAX_STALE
  - CONSUL_DNS_CONFIG_NODE_TTL
  - CONSUL_DNS_CONFIG_SERVICE_TTL
  - CONSUL_DNS_CONFIG_ENABLE_TRUNCATE
  - CONSUL_DNS_CONFIG_ONLY_PASSING
  - CONSUL_DOMAIN
  - CONSUL_ENABLE_DEBUG
  - CONSUL_ENABLE_SYSLOG
  - CONSUL_ENCRYPT
  - CONSUL_KEY_FILE
  - CONSUL_HTTP_API_RESPONSE_HEADERS
  - CONSUL_LEAVE_ON_TERMINATE
  - CONSUL_LOG_LEVEL
  - CONSUL_NODE_NAME
  - CONSUL_PORTS_DNS
  - CONSUL_PORTS_HTTP
  - CONSUL_PORTS_HTTPS
  - CONSUL_PORTS_RPC
  - CONSUL_PORTS_SERF_LAN
  - CONSUL_PORTS_SERF_WAN
  - CONSUL_PORTS_SERVER
  - CONSUL_PROTOCOL
  - CONSUL_REAP
  - CONSUL_RECURSOR
  - CONSUL_RECURSORS
  - CONSUL_REJOIN_AFTER_LEAVE
  - CONSUL_RETRY_JOIN
  - CONSUL_RETRY_INTERVAL
  - CONSUL_RETRY_JOIN_WAN
  - CONSUL_RETRY_INTERVAL_WAN
  - CONSUL_SERVER
  - CONSUL_SERVER_NAME
  - CONSUL_SESSION_TTL_MIN
  - CONSUL_SKIP_LEAVE_ON_INTERRUPT
  - CONSUL_START_JOIN
  - CONSUL_START_JOIN_WAN
  - CONSUL_STATSD_ADDR
  - CONSUL_DOGSTATSD_ADDR
  - CONSUL_DOGSTATSD_TAGS
  - CONSUL_STATSITE_ADDR
  - CONSUL_STATSITE_PREFIX
  - CONSUL_SYSLOG_FACILITY
  - CONSUL_UI
  - CONSUL_UI_DIR
  - CONSUL_UNIX_SOCKETS_USER
  - CONSUL_UNIX_SOCKETS_GROUP
  - CONSUL_UNIX_SOCKETS_MODE
  - CONSUL_VERIFY_INCOMING
  - CONSUL_VERIFY_OUTGOING
  - CONSUL_VERIFY_SERVER_HOSTNAME

## License
MIT
