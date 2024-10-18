# Import nmap so we can use it for the scan
import nmap
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# open_ports = []
# # Ask user to input the ip address they want to scan.
# while True:
#     ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
#     break

# while True:
#     # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
#     # all the ports is not advised.
#     print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
#     port_range = input("Enter port range: ")
#     port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
#     if port_range_valid:
#         port_min = int(port_range_valid.group(1))
#         port_max = int(port_range_valid.group(2))
#         break

nm = nmap.PortScanner()
# We're looping over all of the ports in the specified range.
for port in range(port_min, port_max + 1):
    try:
        # The result is quite interesting to look at. You may want to inspect the dictionary it returns. 
        # It contains what was sent to the command line in addition to the port status we're after. 
        # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
        result = nm.scan(ip_add_entered, str(port))
        # Uncomment following line and look at dictionary
        # print(result)
        # We extract the port status from the returned object
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
        print(f"Cannot scan port {port}.")
        