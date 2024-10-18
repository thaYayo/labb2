'''.'''
# Uppgift 4
# Time Travelers Calculator
# Programmet ska fråga användaren om ett startdatum och en tidsresa i termer av år,
# månader, dagar, timmar och minuter. Programmet ska sedan visa det exakta datumet och
# klockslaget efter resan.
# Exempel på Utdata: Presentera resultatet i ett läsbart format, t.ex. Du kommer att anlända
# 2099-12-31 kl. 23:59

from datetime import datetime,timedelta

start_datum = input("Ange startdatum(ÅÅÅÅMMDD HH:MM): ")
tid_resa= input("Ange mängd tid som du vill resa: (år-månader-dagar-timmar-minuter)").split("-")
year = int(tid_resa[0])
months = int(tid_resa[1])
dagar = int(tid_resa[2])
timmar = int(tid_resa[3])
minuter = int(tid_resa[4])

year = year*52
months = months*4
weeks = year+months

def time_travel_calculator():
    '''funktion för tidsresa'''
    start_datum_datetime = datetime.strptime(start_datum, '%Y%m%d %H:%M')
    # breakpoint()
    start_datum_datetime += timedelta(weeks=weeks,days=dagar, hours=timmar, minutes=minuter )
    print(start_datum_datetime)

time_travel_calculator()
