## skapa ett script som konsumerar sveriges radio api på ett valfritt sätt.
# använd gärna moduler för att dela upp scriptet i flera filer.


import time
import requests

BASE_URL = "http://api.sr.se/api/v2/"


def convert_time(sr_time):
    ## Function för att convertera tiden från unix epoch till svensk datum/tid
    timestamp = int(sr_time.strip("/Date()")) //1000
    epoch_time = timestamp
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))
    return formatted_time



# funktion för att hämta och visa nyhetskanaler
def get_newsprograms():
    try:
        response = requests.get(f"{BASE_URL}news/?format=json", timeout=10)
    except requests.exceptions.Timeout:
        print("timed out")
    news = response.json()["programs"]
    if response.status_code == 200:
        print("\nNyheter: ")
        for nyhet in news:
            print(f"ID: {nyhet["id"]}, Namn: {nyhet["name"]}\n")
    else:
        print("Ojdå! Något gick fel!\n")


def trafik_info():
    """ funktion för att hämta trafikinfo,plats och  beskrivning från sr api."""   
    response = requests.get(f"{BASE_URL}traffic/messages?format=json")
    trafikinfo = response.json()["messages"]
    if response.status_code == 200:
        print("Trafikinfo: ")
        for info in trafikinfo:
            if info["exactlocation"] == "":
                print(f"Plats: {info["title"]}, Beskrivning: {info['description']}\n")
            else:
                print(f"Plats: {info["exactlocation"]}, Beskrivning: {info['description']}\n")
    else:
        print("Ojdå! Något gick fel!\n")


def get_channels():
    # funktion för att hämta alla kanaler
    try:
        response = requests.get(f"{BASE_URL}channels?format=json", timeout=10)
    except requests.exceptions.Timeout:
        print("timed out")
    if response.status_code == 200:
        channels = response.json()["channels"]
        print("\nKanaler: ")
        for channel in channels:
            print(f"ID: {channel["id"]} Namn: {channel["name"]}")
    else:
        print("Ojdå! Något gick fel!\n")


def get_schedule(channel_id):
    """funktion för att hämta och vis atablån för en kanal med hjälp av sr api."""
    try:
        response = requests.get(f"{BASE_URL}scheduledepisodes?channelid={channel_id}&format=json", timeout=10)
    except requests.exceptions.Timeout:
        print("timed out")
    kanal_tablå = response.json()["schedule"]
    if response.status_code == 200:
        print("\n Tablå för kanalen: ")
        for tablå in kanal_tablå:
            starttime = convert_time(tablå["starttimeutc"])
            print(f"{starttime} - {tablå["title"]}\n")
        else:
            print("Ojdå! Något gick fel!\n")






# huvud meny funktion

def main():
    while True:
        print("\nHuvud meny")
        print("1. Visa alla nyhetsprogram")
        print("2. Visa trafikinformation")
        print("3. Visa alla kanaler")
        print("4. Visa tablå för angiven kanal")
        print("5. Avsluta program")

        choice = input("\nAnge val: ")

        if choice == '1':
            get_newsprograms()
        if choice == '2':
            trafik_info()
        if choice == '3':
            get_channels()
        if choice == '4':
            channel_id=int(input("Ange id till kanalen vars tablå du önskar se (siffror): "))
            get_schedule(channel_id)
        if choice == '5':
            break

if __name__ == "__main__":
    main()
