#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import json


ENTRY_CMD="/usr/local/bin/consul"
BOOT_CONFIG="boot_config.json"


def get_value(config, key, default=None):
    try:
        if key not in config or config[key] == "":
            return default
        return config[key]
    except:
        raise


def get_bool(config, key, default=None):
    try:
        if key not in config or config[key] == "":
            return default

        val = str(config[key]).lower()
        if val in ("true", "yes", "on"):
            val = True
        elif val in ("false", "no", "off"):
            val = True
        else:
            val = None

        return val
    except:
        raise


def get_list(config, key, default=None):
    try:
        if key not in config or config[key] == "":
            return default

        vals = str(config[key]).split(",")
        return vals if 0 < len(vals) else None
    except:
        raise


def get_kv_list(config, key, default=None):
    try:
        if key not in config or config[key] == "":
            return default

        result = {}
        vals = str(config[key]).split(",")
        for val in vals:
            val = val.split("=")
            k = val[0]
            v = val[1]
            result[k] = v

        return result if 0 < len(result) else None
    except:
        raise




def main():

    # config_dir
    environ = os.environ
    config_dir = get_value(config=environ, key="CONSUL_CONFIG_DIR", default="/var/lib/consul/config")
    path_boot_config = os.path.join(config_dir, BOOT_CONFIG)

    # load exists config.
    boot_config = {}
    if os.path.exists(path_boot_config):
        with open(path_boot_config, "r") as rfp:
            boot_config = json.loads(rfp.read())


    val = get_value(config=environ, key="CONSUL_ACL_DATACENTER")
    if val is not None:
        boot_config["acl_datacenter"] = val

    val = get_value(config=environ, key="CONSUL_ACL_DEFAULT_POLICY")
    if val is not None:
        boot_config["acl_default_policy"] = val

    val = get_value(config=environ, key="CONSUL_ACL_DOWN_POLICY")
    if val is not None:
        boot_config["acl_down_policy"] = val

    val = get_value(config=environ, key="CONSUL_ACL_MASTER_TOKEN")
    if val is not None:
        boot_config["acl_master_token"] = val

    val = get_value(config=environ, key="CONSUL_ACL_MASTER_TOKEN")
    if val is not None:
        boot_config["acl_master_token"] = val

    val = get_value(config=environ, key="CONSUL_ACL_TOKEN")
    if val is not None:
        boot_config["acl_token"] = val

    val = get_value(config=environ, key="CONSUL_ACL_TTL")
    if val is not None:
        boot_config["acl_ttl"] = val

    val = get_value(config=environ, key="CONSUL_ADDRESSES_DNS")
    if val is not None:
        boot_config["addresses"]["dns"] = val

    val = get_value(config=environ, key="CONSUL_ADDRESSES_HTTP")
    if val is not None:
        boot_config["addresses"]["http"] = val

    val = get_value(config=environ, key="CONSUL_ADDRESSES_HTTPS")
    if val is not None:
        boot_config["addresses"]["https"] = val

    val = get_value(config=environ, key="CONSUL_ADDRESSES_RPC")
    if val is not None:
        boot_config["addresses"]["rpc"] = val

    val = get_value(config=environ, key="CONSUL_ADVERTISE_ADDR")
    if val is not None:
        boot_config["advertise_addr"] = val

    val = get_value(config=environ, key="CONSUL_ADVERTISE_ADDRS_SERF_LAN")
    if val is not None:
        boot_config["advertise_addrs"]["serf_lan"] = val

    val = get_value(config=environ, key="CONSUL_ADVERTISE_ADDRS_SERF_WAN")
    if val is not None:
        boot_config["advertise_addrs"]["serf_wan"] = val

    val = get_value(config=environ, key="CONSUL_ADVERTISE_ADDRS_RPC")
    if val is not None:
        boot_config["advertise_addrs"]["rpc"] = val

    val = get_value(config=environ, key="CONSUL_ADVERTISE_ADDR_WAN")
    if val is not None:
        boot_config["advertise_addr_wan"] = val

    val = get_value(config=environ, key="CONSUL_ATLAS_ACL_TOKEN")
    if val is not None:
        boot_config["atlas_acl_token"] = val

    val = get_value(config=environ, key="CONSUL_ATLAS_INFRASTRUCTURE")
    if val is not None:
        boot_config["atlas_infrastructure"] = val

    val = get_value(config=environ, key="CONSUL_ATLAS_JOIN")
    if val is not None:
        boot_config["atlas_join"] = val

    val = get_value(config=environ, key="CONSUL_ATLAS_TOKEN")
    if val is not None:
        boot_config["atlas_token"] = val

    val = get_value(config=environ, key="CONSUL_ATLAS_ENDPOINT")
    if val is not None:
        boot_config["atlas_endpoint"] = val

    val = get_bool(config=environ, key="CONSUL_BOOTSTRAP")
    if val is not None:
        boot_config["bootstrap"] = val

    val = get_value(config=environ, key="CONSUL_BOOTSTRAP_EXPECT")
    if val is not None:
        boot_config["bootstrap_expect"] = val

    val = get_value(config=environ, key="CONSUL_BIND_ADDR")
    if val is not None:
        boot_config["bind_addr"] = val

    val = get_value(config=environ, key="CONSUL_CA_FILE")
    if val is not None:
        boot_config["ca_file"] = val

    val = get_value(config=environ, key="CONSUL_CERT_FILE")
    if val is not None:
        boot_config["cert_file"] = val

    val = get_value(config=environ, key="CONSUL_CHECK_UPDATE_INTERVAL")
    if val is not None:
        boot_config["check_update_interval"] = val

    val = get_value(config=environ, key="CONSUL_CLIENT_ADDR")
    if val is not None:
        boot_config["client_addr"] = val

    val = get_value(config=environ, key="CONSUL_DATACENTER")
    if val is not None:
        boot_config["datacenter"] = val


    val = get_value(config=environ, key="CONSUL_DATA_DIR")
    if val is not None:
        boot_config["data_dir"] = val

    val = get_bool(config=environ, key="CONSUL_DISABLE_ANONYMOUS_SIGNATURE")
    if val is not None:
        boot_config["disable_anonymous_signature"] = val

    val = get_bool(config=environ, key="CONSUL_DISABLE_REMOTE_EXEC")
    if val is not None:
        boot_config["disable_remote_exec"] = val

    val = get_bool(config=environ, key="CONSUL_DISABLE_UPDATE_CHECK")
    if val is not None:
        boot_config["disable_update_check"] = val

    val = get_value(config=environ, key="CONSUL_DNS_CONFIG_ALLOW_STALE")
    if val is not None:
        boot_config["dns_config"]["allow_stale"] = val

    val = get_value(config=environ, key="CONSUL_DNS_CONFIG_MAX_STALE")
    if val is not None:
        boot_config["dns_config"]["max_stale"] = val

    val = get_value(config=environ, key="CONSUL_DNS_CONFIG_NODE_TTL")
    if val is not None:
        boot_config["dns_config"]["node_ttl"] = val

    val = get_kv_list(config=environ, key="CONSUL_DNS_CONFIG_SERVICE_TTL")
    if val is not None:
        boot_config["dns_config"]["service_ttl"] = val

    val = get_bool(config=environ, key="CONSUL_DNS_CONFIG_ENABLE_TRUNCATE")
    if val is not None:
        boot_config["dns_config"]["enable_truncate"] = val

    val = get_bool(config=environ, key="CONSUL_DNS_CONFIG_ONLY_PASSING")
    if val is not None:
        boot_config["dns_config"]["only_passing"] = val

    val = get_value(config=environ, key="CONSUL_DOMAIN")
    if val is not None:
        boot_config["domain"] = val

    val = get_bool(config=environ, key="CONSUL_ENABLE_DEBUG")
    if val is not None:
        boot_config["enable_debug"] = val

    val = get_bool(config=environ, key="CONSUL_ENABLE_SYSLOG")
    if val is not None:
        boot_config["enable_syslog"] = val

    val = get_value(config=environ, key="CONSUL_ENCRYPT")
    if val is not None:
        boot_config["encrypt"] = val

    val = get_value(config=environ, key="CONSUL_KEY_FILE")
    if val is not None:
        boot_config["key_file"] = val

    val = get_kv_list(config=environ, key="CONSUL_HTTP_API_RESPONSE_HEADERS")
    if val is not None:
        boot_config["http_api_response_headers"] = val

    val = get_value(config=environ, key="CONSUL_LEAVE_ON_TERMINATE")
    if val is not None:
        boot_config["leave_on_terminate"] = val

    val = get_value(config=environ, key="CONSUL_LOG_LEVEL")
    if val is not None:
        boot_config["log_level"] = val

    val = get_value(config=environ, key="CONSUL_NODE_NAME")
    if val is not None:
        boot_config["node_name"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_DNS")
    if val is not None:
        boot_config["ports"]["dns"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_HTTP")
    if val is not None:
        boot_config["ports"]["http"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_HTTPS")
    if val is not None:
        boot_config["ports"]["https"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_RPC")
    if val is not None:
        boot_config["ports"]["rpc"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_SERF_LAN")
    if val is not None:
        boot_config["ports"]["serf_lan"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_SERF_WAN")
    if val is not None:
        boot_config["ports"]["serf_wan"] = val

    val = get_value(config=environ, key="CONSUL_PORTS_SERVER")
    if val is not None:
        boot_config["ports"]["server"] = val

    val = get_value(config=environ, key="CONSUL_PROTOCOL")
    if val is not None:
        boot_config["protocol"] = val

    val = get_bool(config=environ, key="CONSUL_REAP")
    if val is not None:
        boot_config["reap"] = val

    val = get_value(config=environ, key="CONSUL_RECURSOR")
    if val is not None:
        boot_config["recursor"] = val

    val = get_list(config=environ, key="CONSUL_RECURSORS")
    if val is not None:
        boot_config["recursors"] = val

    val = get_value(config=environ, key="CONSUL_REJOIN_AFTER_LEAVE")
    if val is not None:
        boot_config["rejoin_after_leave"] = val

    val = get_list(config=environ, key="CONSUL_RETRY_JOIN")
    if val is not None:
        boot_config["retry_join"] = val

    val = get_value(config=environ, key="CONSUL_RETRY_INTERVAL")
    if val is not None:
        boot_config["retry_interval"] = val

    val = get_list(config=environ, key="CONSUL_RETRY_JOIN_WAN")
    if val is not None:
        boot_config["retry_join_wan"] = val

    val = get_value(config=environ, key="CONSUL_RETRY_INTERVAL_WAN")
    if val is not None:
        boot_config["retry_interval_wan"] = val

    val = get_bool(config=environ, key="CONSUL_SERVER")
    if val is not None:
        boot_config["server"] = val

    val = get_value(config=environ, key="CONSUL_SERVER_NAME")
    if val is not None:
        boot_config["server_name"] = val

    val = get_value(config=environ, key="CONSUL_SESSION_TTL_MIN")
    if val is not None:
        boot_config["session_ttl_min"] = val

    val = get_bool(config=environ, key="CONSUL_SKIP_LEAVE_ON_INTERRUPT")
    if val is not None:
        boot_config["skip_leave_on_interrupt"] = val

    val = get_value(config=environ, key="CONSUL_START_JOIN")
    if val is not None:
        boot_config["start_join"] = val

    val = get_value(config=environ, key="CONSUL_START_JOIN_WAN")
    if val is not None:
        boot_config["start_join_wan"] = val

    val = get_value(config=environ, key="CONSUL_STATSD_ADDR")
    if val is not None:
        boot_config["statsd_addr"] = val

    val = get_value(config=environ, key="CONSUL_DOGSTATSD_ADDR")
    if val is not None:
        boot_config["dogstatsd_addr"] = val

    val = get_list(config=environ, key="CONSUL_DOGSTATSD_TAGS")
    if val is not None:
        boot_config["dogstatsd_tags"] = val

    val = get_value(config=environ, key="CONSUL_STATSITE_ADDR")
    if val is not None:
        boot_config["statsite_addr"] = val

    val = get_value(config=environ, key="CONSUL_STATSITE_PREFIX")
    if val is not None:
        boot_config["statsite_prefix"] = val

    val = get_value(config=environ, key="CONSUL_SYSLOG_FACILITY")
    if val is not None:
        boot_config["syslog_facility"] = val

    val = get_bool(config=environ, key="CONSUL_UI")
    if val is not None:
        boot_config["ui"] = val

    val = get_value(config=environ, key="CONSUL_UI_DIR")
    if val is not None:
        boot_config["ui_dir"] = val

    val = get_value(config=environ, key="CONSUL_UNIX_SOCKETS_USER")
    if val is not None:
        boot_config["unix_sockets"]["user"] = val

    val = get_value(config=environ, key="CONSUL_UNIX_SOCKETS_GROUP")
    if val is not None:
        boot_config["unix_sockets"]["group"] = val

    val = get_value(config=environ, key="CONSUL_UNIX_SOCKETS_MODE")
    if val is not None:
        boot_config["unix_sockets"]["mode"] = val

    val = get_bool(config=environ, key="CONSUL_VERIFY_INCOMING")
    if val is not None:
        boot_config["verify_incoming"] = val

    val = get_bool(config=environ, key="CONSUL_VERIFY_OUTGOING")
    if val is not None:
        boot_config["verify_outgoing"] = val

    val = get_bool(config=environ, key="CONSUL_VERIFY_SERVER_HOSTNAME")
    if val is not None:
        boot_config["verify_server_hostname"] = val

    #val = get_list(config=environ, key="CONSUL_WATCHES")
    #if val is not None:
    #    boot_config["watches"] = val


    # save boot config
    with open(path_boot_config, "w") as wfp:
        wfp.write(json.dumps(boot_config, indent=1))


    cmd = []
    cmd.append("agent")
    cmd.append("-config-dir=%s" % (str(config_dir),))

    val = get_bool(config=environ, key="CONSUL_DEV")
    if val is not None and val is True:
        cmd.append("-dev")

    print "================================================================================"
    print "cmd: %s" % (str(cmd),)
    print "boot_config.json:"
    with open(path_boot_config, "r") as rfp:
        print rfp.read()
    print "================================================================================"

    sys.stdout.flush()
    sys.stderr.flush()
    os.execvp(ENTRY_CMD, [ENTRY_CMD] + cmd)


if __name__ == "__main__":
    main()
