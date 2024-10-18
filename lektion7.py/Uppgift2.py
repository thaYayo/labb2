# Uppgift 2
# Skapa en generator kallad “date_range" som tar emot startdatum, slutdatum och intervall i dagar.
# Använd generatorn för att skriva ut alla datum i intervallet.




from datetime import datetime,timedelta
#variablar för datum till generatorn
start_datum = input("Ange startdatum: ")
start_datum_datetime = datetime.strptime(start_datum, '%Y%m%d')
slut_datum = input("Ange slutdatum: ")
slut_datum_datetime = datetime.strptime(slut_datum, '%Y%m%d')
intervall = int(input("Ange intervall (dagar): "))


def date_range(start_datum_datetime,slut_datum_datetime,intervall):
    '''funktion för generatorn'''
    while start_datum_datetime < slut_datum_datetime:
        start_datum_datetime += timedelta(days = intervall)
        print(start_datum_datetime)




date_range(start_datum_datetime,slut_datum_datetime,intervall)
