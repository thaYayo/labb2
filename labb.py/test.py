# def läs_fil(filename):
#     result = []
#     with open(filename, "r") as file:
#         for files in file:
#            result.append(files.strip())
#         print(result) 


# läs_fil("ipadress.txt")

# import requests
# base_url = "http://api.sr.se/api/v2/"



# def get_schedule(channel_id):
#     response = requests.get(f"{base_url}scheduledepisodes?channelid={channel_id}&format=json")
#     # kanal_tablå = response.json()["schedule"]
#     print(response)

# channel_id=int(input("Ange id till kanalen vars tablå du önskar se: "))
# # get_schedule(channel_id)

# get_schedule(channel_id)
# def convert_time(sr_time):
#      import time
#      timestamp = sr_time //1000
#      epoch_time = timestamp  
#      formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))
#      print(formatted_time)

# convert_time(1728424800000)

# import logging 

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logger.debug('This message should go to the log file')
# logger.info('So should this')
# logger.warning('And this, too')
# logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
