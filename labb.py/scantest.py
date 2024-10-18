import nmap 
import pprint

def scanner(ips):
    nm = nmap.PortScanner()
    result = {}
    for ip in ips:
        scan_result = nm.scan(ip)
        result[ip] = scan_result
        result[ip]["nmap"]["scaninfo"]["tcp"].pop("services")
    return result
        



def scan():

    ip_to_scan = input("Ange ip adresser som önskas skanna (separera med ','): ").split(',')
    resultat = (scanner(ip_to_scan))
    pprint.pprint(resultat)


scan()

