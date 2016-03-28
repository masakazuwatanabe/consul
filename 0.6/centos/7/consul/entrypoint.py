#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import json
from subprocess import Popen
from subprocess import PIPE


ENTRY_CMD="/usr/local/bin/consul"
BOOT_CONFIG="boot_config.json"


TABLE_CONFIG = \
{
    "CONSUL_ACL_DATACENTER":              { "type": "str",  "key": ["acl_datacenter"]                              },
    "CONSUL_ACL_DEFAULT_POLICY":          { "type": "str",  "key": ["acl_default_policy"]                          },
    "CONSUL_ACL_DOWN_POLICY":             { "type": "str",  "key": ["acl_down_policy"]                             },
    "CONSUL_ACL_MASTER_TOKEN":            { "type": "str",  "key": ["acl_master_token"]                            },
    "CONSUL_ACL_TOKEN":                   { "type": "str",  "key": ["acl_token"]                                   },
    "CONSUL_ACL_TTL":                     { "type": "str",  "key": ["acl_ttl"]                                     },
    "CONSUL_ADDRESSES_DNS":               { "type": "str",  "key": ["addresses", "dns"]                            },
    "CONSUL_ADDRESSES_HTTP":              { "type": "str",  "key": ["addresses", "http"]                           },
    "CONSUL_ADDRESSES_HTTPS":             { "type": "str",  "key": ["addresses", "https"]                          },
    "CONSUL_ADDRESSES_RPC":               { "type": "str",  "key": ["addresses", "rpc"]                            },
    "CONSUL_ADVERTISE_ADDR":              { "type": "str",  "key": ["advertise_addr"]                              },
    "CONSUL_ADVERTISE_ADDRS_SERF_LAN":    { "type": "str",  "key": ["advertise_addrs", "serf_lan"]                 },
    "CONSUL_ADVERTISE_ADDRS_SERF_WAN":    { "type": "str",  "key": ["advertise_addrs", "serf_wan"]                 },
    "CONSUL_ADVERTISE_ADDRS_RPC":         { "type": "str",  "key": ["advertise_addrs", "rpc"]                      },
    "CONSUL_ADVERTISE_ADDR_WAN":          { "type": "str",  "key": ["advertise_addr_wan"]                          },
    "CONSUL_ATLAS_ACL_TOKEN":             { "type": "str",  "key": ["atlas_acl_token"]                             },
    "CONSUL_ATLAS_INFRASTRUCTURE":        { "type": "str",  "key": ["atlas_infrastructure"]                        },
    "CONSUL_ATLAS_JOIN":                  { "type": "str",  "key": ["atlas_join"]                                  },
    "CONSUL_ATLAS_TOKEN":                 { "type": "str",  "key": ["atlas_token"]                                 },
    "CONSUL_ATLAS_ENDPOINT":              { "type": "str",  "key": ["atlas_endpoint"]                              },
    "CONSUL_BOOTSTRAP":                   { "type": "bool", "key": ["bootstrap"]                                   },
    "CONSUL_BOOTSTRAP_EXPECT":            { "type": "str",  "key": ["bootstrap_expect"]                            },
    "CONSUL_BIND_ADDR":                   { "type": "str",  "key": ["bind_addr"]                                   },
    "CONSUL_CA_FILE":                     { "type": "str",  "key": ["ca_file"]                                     },
    "CONSUL_CERT_FILE":                   { "type": "str",  "key": ["cert_file"]                                   },
    "CONSUL_CHECK_UPDATE_INTERVAL":       { "type": "str",  "key": ["check_update_interval"]                       },
    "CONSUL_CLIENT_ADDR":                 { "type": "str",  "key": ["client_addr"]                                 },
#    "CONSUL_CONFIG_DIR":                  { "type": "str",  "key": ["config_dir"]                                  },
    "CONSUL_DATACENTER":                  { "type": "str",  "key": ["datacenter"]                                  },
    "CONSUL_DATA_DIR":                    { "type": "str",  "key": ["data_dir"]                                    },
    "CONSUL_DEV":                         { "type": "bool", "key": ["dev"]                                         },
    "CONSUL_DISABLE_ANONYMOUS_SIGNATURE": { "type": "bool", "key": ["disable_anonymous_signature"]                 },
    "CONSUL_DISABLE_REMOTE_EXEC":         { "type": "bool", "key": ["disable_remote_exec"]                         },
    "CONSUL_DISABLE_UPDATE_CHECK":        { "type": "bool", "key": ["disable_update_check"]                        },
    "CONSUL_DNS_CONFIG_ALLOW_STALE":      { "type": "bool", "key": ["dns_config", "allow_stale"]                   },
    "CONSUL_DNS_CONFIG_MAX_STALE":        { "type": "str",  "key": ["dns_config", "max_stale"]                     },
    "CONSUL_DNS_CONFIG_NODE_TTL":         { "type": "str",  "key": ["dns_config", "node_ttl"]                      },
    "CONSUL_DNS_CONFIG_SERVICE_TTL":      { "type": "kv",   "key": ["dns_config", "service_ttl"]                   },
    "CONSUL_DNS_CONFIG_ENABLE_TRUNCATE":  { "type": "bool", "key": ["dns_config", "enable_truncate"]               },
    "CONSUL_DNS_CONFIG_ONLY_PASSING":     { "type": "bool", "key": ["dns_config", "only_passing"]                  },
    "CONSUL_DOMAIN":                      { "type": "str",  "key": ["domain"]                                      },
    "CONSUL_ENABLE_DEBUG":                { "type": "bool", "key": ["enable_debug"]                                },
    "CONSUL_ENABLE_SYSLOG":               { "type": "bool", "key": ["enable_syslog"]                               },
    "CONSUL_ENCRYPT":                     { "type": "str",  "key": ["encrypt"]                                     },
    "CONSUL_KEY_FILE":                    { "type": "str",  "key": ["key_file"]                                    },
    "CONSUL_HTTP_API_RESPONSE_HEADERS":   { "type": "kv",   "key": ["http_api_response_headers"]                   },
    "CONSUL_LEAVE_ON_TERMINATE":          { "type": "bool", "key": ["leave_on_terminate"]                          },
    "CONSUL_LOG_LEVEL":                   { "type": "str",  "key": ["log_level"]                                   },
    "CONSUL_NODE_NAME":                   { "type": "str",  "key": ["node_name"]                                   },
    "CONSUL_PORTS_DNS":                   { "type": "str",  "key": ["ports", "dns"]                                },
    "CONSUL_PORTS_HTTP":                  { "type": "str",  "key": ["ports", "http"]                               },
    "CONSUL_PORTS_HTTPS":                 { "type": "str",  "key": ["ports", "https"]                              },
    "CONSUL_PORTS_RPC":                   { "type": "str",  "key": ["ports", "rpc"]                                },
    "CONSUL_PORTS_SERF_LAN":              { "type": "str",  "key": ["ports", "serf_lan"]                           },
    "CONSUL_PORTS_SERF_WAN":              { "type": "str",  "key": ["ports", "serf_wan"]                           },
    "CONSUL_PORTS_SERVER":                { "type": "str",  "key": ["server"]                                      },
    "CONSUL_PROTOCOL":                    { "type": "str",  "key": ["protocol"]                                    },
    "CONSUL_REAP":                        { "type": "bool", "key": ["reap"]                                        },
    "CONSUL_RECURSOR":                    { "type": "str",  "key": ["recursor"]                                    },
    "CONSUL_RECURSORS":                   { "type": "list", "key": ["recursors"]                                   },
    "CONSUL_REJOIN_AFTER_LEAVE":          { "type": "bool", "key": ["rejoin_after_leave"]                          },
    "CONSUL_RETRY_JOIN":                  { "type": "list", "key": ["retry_join"]                                  },
    "CONSUL_RETRY_INTERVAL":              { "type": "str",  "key": ["retry_interval"]                              },
    "CONSUL_RETRY_JOIN_WAN":              { "type": "list", "key": ["retry_join_wan"]                              },
    "CONSUL_RETRY_INTERVAL_WAN":          { "type": "str",  "key": ["retry_interval_wan"]                          },
    "CONSUL_SERVER":                      { "type": "bool", "key": ["server"]                                      },
    "CONSUL_SERVER_NAME":                 { "type": "str",  "key": ["server_name"]                                 },
    "CONSUL_SESSION_TTL_MIN":             { "type": "str",  "key": ["session_ttl_min"]                             },
    "CONSUL_SKIP_LEAVE_ON_INTERRUPT":     { "type": "bool", "key": ["skip_leave_on_interrupt"]                     },
    "CONSUL_START_JOIN":                  { "type": "str",  "key": ["start_join"]                                  },
    "CONSUL_START_JOIN_WAN":              { "type": "str",  "key": ["start_join_wan"]                              },
    "CONSUL_TELEMETRY_STATSD_ADDRESS":    { "type": "str",  "key": ["telemetry", "statsd_address"]                 },
    "CONSUL_TELEMETRY_STATSITE_ADDRESS":  { "type": "str",  "key": ["telemetry", "statsite_address"]               },
    "CONSUL_TELEMETRY_STATSITE_PREFIX":   { "type": "str",  "key": ["telemetry", "statsite_prefix"]                },
    "CONSUL_TELEMETRY_DOGSTATSD_ADDR":    { "type": "str",  "key": ["telemetry", "dogstatsd_addr"]                 },
    "CONSUL_TELEMETRY_DOGSTATSD_TAGS":    { "type": "str",  "key": ["telemetry", "dogstatsd_tags"]                 },
    "CONSUL_TELEMETRY_DISABLE_HOSTNAME":  { "type": "str",  "key": ["telemetry", "disable_hostname"]               },
    "CONSUL_STATSD_ADDR":                 { "type": "str",  "key": ["statsd_addr"]                                 },
    "CONSUL_STATSITE_ADDR":               { "type": "str",  "key": ["statsite_addr"]                               },
    "CONSUL_STATSITE_PREFIX":             { "type": "str",  "key": ["statsite_prefix"]                             },
    "CONSUL_DOGSTATSD_ADDR":              { "type": "str",  "key": ["dogstatsd_addr"]                              },
    "CONSUL_DOGSTATSD_TAGS":              { "type": "list", "key": ["dogstatsd_tags"]                              },
    "CONSUL_SYSLOG_FACILITY":             { "type": "str",  "key": ["syslog_facility"]                             },
    "CONSUL_TRANSLATE_WAN_ADDRS":         { "type": "bool", "key": ["translate_wan_addrs"]                         },
    "CONSUL_UI":                          { "type": "bool", "key": ["ui"]                                          },
    "CONSUL_UI_DIR":                      { "type": "str",  "key": ["ui_dir"]                                      },
    "CONSUL_UNIX_SOCKETS_USER":           { "type": "str",  "key": ["unix_sockets", "user"]                        },
    "CONSUL_UNIX_SOCKETS_GROUP":          { "type": "str",  "key": ["unix_sockets", "group"]                       },
    "CONSUL_UNIX_SOCKETS_MODE":           { "type": "str",  "key": ["unix_sockets", "mode"]                        },
    "CONSUL_VERIFY_INCOMING":             { "type": "bool", "key": ["verify_incoming"]                             },
    "CONSUL_VERIFY_OUTGOING":             { "type": "bool", "key": ["verify_outgoing"]                             },
    "CONSUL_VERIFY_SERVER_HOSTNAME":      { "type": "bool", "key": ["verify_server_hostname"]                      },
#    "CONSUL_WATCHES":                     { "type": "list", "key": ["watches"]                                     },
}


def get_str(val, default=None):
    try:
        if val is None:
            return default
        return str(val)
    except:
        raise


def get_bool(val, default=None):
    try:
        if val is None:
            return default

        val = str(val).lower()
        if val in ("true", "yes", "on"):
            val = True
        elif val in ("false", "no", "off"):
            val = True
        else:
            val = None

        return val
    except:
        raise


def get_list(val, default=None):
    try:
        if val is None:
            return default

        vals = str(val).split(",")

        return vals if 0 < len(vals) else None
    except:
        raise


def get_kv(val, default=None):
    try:
        if val is None:
            return default

        result = {}
        vals = str(val).split(",")
        for val in vals:
            val = val.split("=")
            k = val[0]
            v = val[1]
            result[k] = v

        return result if 0 < len(result) else None
    except:
        raise


def build_values(environ, table, config):
    try:
        for env_key, env_val in environ.items():
            if env_key in table and env_val is not None and env_val != "":
                attr = table[env_key]
                type = attr["type"]
                keys = attr["key"]
                n_keys = len(keys)
                if n_keys < 1:
                    continue

                val = None
                if type == "str":
                    val = get_str(env_val)
                elif type == "bool":
                    val = get_bool(env_val)
                elif type == "list":
                    val = get_list(env_val)
                elif type == "kv":
                    val = get_kv(env_val)

                update_base = {}
                update_cur = update_base
                for i, key in enumerate(keys):
                    if i == (n_keys - 1):
                        update_cur[key] = val
                    else:
                        update_cur[key] = {}
                        update_cur = update_cur[key]
                config.update(update_base)
    except:
        raise


def is_enable(environ, key):
    if key in environ and environ[key] is not None and environ[key] != "":
        return True
    return False




def main():

    environ = os.environ

    # config_dir
    config_dir = "/var/lib/consul/config"
    if "CONSUL_CONFIG_DIR" in environ:
        config_dir = str(environ["CONSUL_CONFIG_DIR"])
    path_boot_config = os.path.join(config_dir, BOOT_CONFIG)

    # remove old config.
    boot_config = {}
    if os.path.exists(path_boot_config):
        os.remove(path_boot_config)


    # build environment configuration.
    build_values(environ=environ, table=TABLE_CONFIG, config=boot_config)


    # extra configuration =====================================================

    if is_enable(environ=environ, key="CONSUL_EX_ADVERTISE_ADDR"):
        val = get_str(environ["CONSUL_EX_ADVERTISE_ADDR"])
        val = str(Popen(val, stdout=PIPE, shell=True).communicate()[0]).strip()
        boot_config["advertise_addr"] = val


    if is_enable(environ=environ, key="CONSUL_EX_ADVERTISE_ADDRS_SERF_LAN"):
        val = get_str(environ["CONSUL_EX_ADVERTISE_ADDRS_SERF_LAN"])
        val = str(Popen(val, stdout=PIPE, shell=True).communicate()[0]).strip()
        update_ip, sep, update_port = val.partition(":")

        base_ip = sep = base_port = None
        if "advertise_addrs" in boot_config and "serf_lan" in boot_config["advertise_addrs"]:
            base_val = boot_config["advertise_addrs"]["serf_lan"]
            base_ip,  sep, base_port = base_val.partition(":")

        update_ip = update_ip if update_ip != "" else base_ip
        update_port = update_port if update_port != "" else base_port
        boot_config["advertise_addrs"]["serf_lan"] = update_ip + ":" + update_port


    if is_enable(environ=environ, key="CONSUL_EX_ADVERTISE_ADDRS_SERF_WAN"):
        val = get_str(environ["CONSUL_EX_ADVERTISE_ADDRS_SERF_WAN"])
        val = str(Popen(val, stdout=PIPE, shell=True).communicate()[0]).strip()
        update_ip, sep, update_port = val.partition(":")

        base_ip = sep = base_port = None
        if "advertise_addrs" in boot_config and "serf_wan" in boot_config["advertise_addrs"]:
            base_val = boot_config["advertise_addrs"]["serf_wan"]
            base_ip,  sep, base_port = base_val.partition(":")

        update_ip = update_ip if update_ip != "" else base_ip
        update_port = update_port if update_port != "" else base_port
        boot_config["advertise_addrs"]["serf_wan"] = update_ip + ":" + update_port


    if is_enable(environ=environ, key="CONSUL_EX_ADVERTISE_ADDRS_SERF_RPC"):
        val = get_str(environ["CONSUL_EX_ADVERTISE_ADDRS_SERF_RPC"])
        val = str(Popen(val, stdout=PIPE, shell=True).communicate()[0]).strip()
        update_ip, sep, update_port = val.partition(":")

        base_ip = sep = base_port = None
        if "advertise_addrs" in boot_config and "serf_rpc" in boot_config["advertise_addrs"]:
            base_val = boot_config["advertise_addrs"]["serf_rpc"]
            base_ip,  sep, base_port = base_val.partition(":")

        update_ip = update_ip if update_ip != "" else base_ip
        update_port = update_port if update_port != "" else base_port
        boot_config["advertise_addrs"]["serf_rpc"] = update_ip + ":" + update_port


    if is_enable(environ=environ, key="CONSUL_EX_ADVERTISE_ADDR_WAN"):
        val = get_str(environ["CONSUL_EX_ADVERTISE_ADDR_WAN"])
        val = str(Popen(val, stdout=PIPE, shell=True).communicate()[0]).strip()
        boot_config["advertise_addr_wan"] = val

    # extra configuration =====================================================


    # build cmd agent config_dir
    cmd = []
    cmd.append("agent")
    cmd.append("-config-dir=%s" % (str(config_dir),))

    # build cmd dev
    if "dev" in boot_config:
        if boot_config["dev"] is True:
            cmd.append("-dev")
        del boot_config["dev"]

    # save boot config
    with open(path_boot_config, "w") as wfp:
        wfp.write(json.dumps(boot_config, indent=1))


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
