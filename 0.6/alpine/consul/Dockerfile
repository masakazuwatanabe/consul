FROM alpine


ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip /tmp/consul.zip
ADD https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_web_ui.zip /tmp/consul_web_ui.zip
RUN echo "make consul." \
  && mkdir -p /var/lib/consul/config \
  && mkdir -p /var/lib/consul/data \
  && mkdir -p /var/lib/consul/web_ui \
  && cd /tmp \
  && unzip consul.zip \
  && chmod +x ./consul \
  && mv ./consul /usr/local/bin \
  && rm -f ./consul.zip \
  && unzip consul_web_ui.zip -d /var/lib/consul/web_ui

RUN apk --update add python && rm -rf /var/cache/apk/*

COPY entrypoint.sh /
COPY entrypoint.py /
RUN chmod +x entrypoint.sh entrypoint.py


ENV \
  CONSUL_CONFIG_DIR="/var/lib/consul/config" \
  CONSUL_DEV="" \
  \
  CONSUL_ACL_DATACENTER="" \
  CONSUL_ACL_DEFAULT_POLICY="" \
  CONSUL_ACL_DOWN_POLICY="" \
  CONSUL_ACL_MASTER_TOKEN="" \
  CONSUL_ACL_TOKEN="" \
  CONSUL_ACL_TTL="" \
  CONSUL_ADDRESSES_DNS="" \
  CONSUL_ADDRESSES_HTTP="" \
  CONSUL_ADDRESSES_HTTPS="" \
  CONSUL_ADDRESSES_RPC="" \
  CONSUL_ADVERTISE_ADDR="" \
  CONSUL_ADVERTISE_ADDRS_SERF_LAN="" \
  CONSUL_ADVERTISE_ADDRS_SERF_WAN="" \
  CONSUL_ADVERTISE_ADDRS_RPC="" \
  CONSUL_ADVERTISE_ADDR_WAN="" \
  CONSUL_ATLAS_ACL_TOKEN="" \
  CONSUL_ATLAS_INFRASTRUCTURE="" \
  CONSUL_ATLAS_JOIN="" \
  CONSUL_ATLAS_TOKEN="" \
  CONSUL_ATLAS_ENDPOINT="" \
  CONSUL_BOOTSTRAP="" \
  CONSUL_BOOTSTRAP_EXPECT="" \
  CONSUL_BIND_ADDR="0.0.0.0" \
  CONSUL_CA_FILE="" \
  CONSUL_CERT_FILE="" \
  CONSUL_CHECK_UPDATE_INTERVAL="" \
  CONSUL_CLIENT_ADDR="0.0.0.0" \
  CONSUL_DATACENTER="" \
  CONSUL_DATA_DIR="/var/lib/consul/data" \
  CONSUL_DISABLE_ANONYMOUS_SIGNATURE="" \
  CONSUL_DISABLE_REMOTE_EXEC="" \
  CONSUL_DISABLE_UPDATE_CHECK="" \
  CONSUL_DNS_CONFIG_ALLOW_STALE="" \
  CONSUL_DNS_CONFIG_MAX_STALE="" \
  CONSUL_DNS_CONFIG_NODE_TTL="" \
  CONSUL_DNS_CONFIG_SERVICE_TTL="" \
  CONSUL_DNS_CONFIG_ENABLE_TRUNCATE="" \
  CONSUL_DNS_CONFIG_ONLY_PASSING="" \
  CONSUL_DOMAIN="" \
  CONSUL_ENABLE_DEBUG="" \
  CONSUL_ENABLE_SYSLOG="" \
  CONSUL_ENCRYPT="" \
  CONSUL_KEY_FILE="" \
  CONSUL_HTTP_API_RESPONSE_HEADERS="" \
  CONSUL_LEAVE_ON_TERMINATE="true" \
  CONSUL_LOG_LEVEL="" \
  CONSUL_NODE_NAME="" \
  CONSUL_PORTS_DNS="" \
  CONSUL_PORTS_HTTP="" \
  CONSUL_PORTS_HTTPS="" \
  CONSUL_PORTS_RPC="" \
  CONSUL_PORTS_SERF_LAN="" \
  CONSUL_PORTS_SERF_WAN="" \
  CONSUL_PORTS_SERVER="" \
  CONSUL_PROTOCOL="" \
  CONSUL_REAP="" \
  CONSUL_RECURSOR="" \
  CONSUL_RECURSORS="" \
  CONSUL_REJOIN_AFTER_LEAVE="" \
  CONSUL_RETRY_JOIN="" \
  CONSUL_RETRY_INTERVAL="" \
  CONSUL_RETRY_JOIN_WAN="" \
  CONSUL_RETRY_INTERVAL_WAN="" \
  CONSUL_SERVER="" \
  CONSUL_SERVER_NAME="" \
  CONSUL_SESSION_TTL_MIN="" \
  CONSUL_SKIP_LEAVE_ON_INTERRUPT="" \
  CONSUL_START_JOIN="" \
  CONSUL_START_JOIN_WAN="" \
  CONSUL_TELEMETRY_STATSD_ADDRESS="" \
  CONSUL_TELEMETRY_STATSITE_ADDRESS="" \
  CONSUL_TELEMETRY_STATSITE_PREFIX="" \
  CONSUL_TELEMETRY_DOGSTATSD_ADDR="" \
  CONSUL_TELEMETRY_DOGSTATSD_TAGS="" \
  CONSUL_TELEMETRY_DISABLE_HOSTNAME="" \
  CONSUL_STATSD_ADDR="" \
  CONSUL_STATSITE_ADDR="" \
  CONSUL_STATSITE_PREFIX="" \
  CONSUL_DOGSTATSD_ADDR="" \
  CONSUL_DOGSTATSD_TAGS="" \
  CONSUL_SYSLOG_FACILITY="" \
  CONSUL_TRANSLATE_WAN_ADDRS="" \
  CONSUL_UI="" \
  CONSUL_UI_DIR="/var/lib/consul/web_ui" \
  CONSUL_UNIX_SOCKETS_USER="" \
  CONSUL_UNIX_SOCKETS_GROUP="" \
  CONSUL_UNIX_SOCKETS_MODE="" \
  CONSUL_VERIFY_INCOMING="" \
  CONSUL_VERIFY_OUTGOING="" \
  CONSUL_VERIFY_SERVER_HOSTNAME="" \
  \
  CONSUL_EX_ADVERTISE_ADDR="" \
  CONSUL_EX_ADVERTISE_ADDRS_SERF_LAN="" \
  CONSUL_EX_ADVERTISE_ADDRS_SERF_WAN="" \
  CONSUL_EX_ADVERTISE_ADDRS_RPC="" \
  CONSUL_EX_ADVERTISE_ADDR_WAN=""


VOLUME \
  /var/lib/consul/config \
  /var/lib/consul/data \
  /var/lib/consul/web_ui

EXPOSE 8300 8301/tcp 8301/udp 8302/tcp 8302/udp 8400 8500 8600/tcp 8600/udp


ENTRYPOINT ["/entrypoint.sh"]
CMD []
