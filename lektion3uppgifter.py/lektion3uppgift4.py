import os 

# 4. Ip pinger
# Lägg till IP-adresser från tailscale-miljön i en text fil (en ip-adress per rad).
# Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen och till en fil.
# Använd följande i toppen av ditt skript:
# import os
# Os-funktion för att pinga en adress (en funktion för win och en för linux):
# os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1") # Linux
# os.system(f"ping -n 1 {ip_address} > NUL 2>&1") # Windows

with open("ipadress.txt", "r") as file:
    with open("resultat_ping.txt", "a") as result_file:
        for ip in file:
            ip = ip.strip()    
            response = os.popen(f"ping -n 1 {ip}").read()
            if "Destination host unreachable." in response:
                print(f"{ip} -> fail")
                result_file.write(f"{ip} -> fail\n")
            else:
                print(f"{ip} -> success")
                result_file.write(f"{ip} -> success\n")
print("Ping is done")


