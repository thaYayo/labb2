import nmap
import pprint

iplist = ["192.168.0.96", "8.8.8.8"]

def scan_host(*args):
    if len(args) == 1:
        hosts = args[0]
    else:
        hosts = ",".join(args)

    nm = nmap.PortScanner()
    nm.scan(hosts)
    return nm[hosts]
    # result = {}

    # for host in 

scan_host("192.168.0.96 8.8.8.8")
# result = scan_host()
# pprint.pprint(result)

# hostname = result["hostnames"][0]["name"] if result["hostnames"] else "unknown"
# if "tcp" in result:
#     print(f"open tcp port: ")
#     for port, port_data in result["tcp"].items():
#         print(f"Port: {port}: {port_data["name"]} ({port_data["state"]})")
