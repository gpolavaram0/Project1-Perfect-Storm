#Dependencies
import os
import csv
from pprint import pprint
import time
import datetime
import matplotlib.pyplot as plt
import requests
import pandas as pd
#from config import api_key

api_key = '3ab60ea333b64e4404d7ad76309764ae'

import time
import datetime
from datetime import timezone

#CSV path join in 
csvpath = os.path.join('Fires Data', 'working_fires.csv')


fireFile = open(csvpath, 'r' )
next(csv.reader(fireFile))
fire_csvReader = list(csv.reader(fireFile))
counter = 0
for row in fire_csvReader:
    #print(row)
    counter += 1
    
    #Counter limit in "if" is for number of API calls. setting counter to 501 will output 500 values
    if counter == 100:
        break
    else:
        csv_add = []
        Lat_fireLoc = row[30]
        Long_fireLoc = row[31]
        DISCOVERY_DATE = row[20]
        DISCOVERY_TIME = row[22]
        DISCOVERY_TIME_SECONDS = 43200


        #---------------------------------------------------
        #Converts DISCOVERY_DATE column in "working_fires" CSV into distinct year, month, and day value for the UNIX time conversion
        DISCOVERY_YEAR = int(DISCOVERY_DATE.split('-')[0])
        DISCOVERY_MONTH = int(DISCOVERY_DATE.split('-')[1])
        DISCOVERY_DAY = int(DISCOVERY_DATE.split('-')[2])

        #print(f"DISCOVERY_YEAR:{DISCOVERY_YEAR}-")
        #print(f"DISCOVERY_MONTH:{DISCOVERY_MONTH}-")
        #print(f"DISCOVERY_DAY:{DISCOVERY_DAY}-")

        #-------------------------------------------
        #DISCOVERY_TIME_SECONDS: The number of 

        #If statement to convert Discover time into seconds (while adjusting for 3 vs 4 character time to separate hours and minutes)
        #If len(DISCOVERY_TIME) == 3:
        #    DISCOVERY_TIME[0]
        dt = datetime.date(DISCOVERY_YEAR, DISCOVERY_MONTH, DISCOVERY_DAY)
        #dt = datetime.date(2015, 10, 19)
        d = datetime.date(int(2005),int(7),int(9))
        #d = datetime.date(2005,7,9)

        #Converts that date to 5 PM Greenwich (UTC) time, and add 43200 to make it noon CST (central) time
        
        #UnixTime = time.mktime(d.timetuple()) + 43200
        #UnixTime = '1584481193'
        #UnixTime = '1322683200'

        #Adding 61200 seconds (17 hours) to unix to change from midnight GMT to noon same day in CST time. 
        UnixTime = (dt - datetime.date(1970, 1, 1)).total_seconds() + 61200


        #print("UnixTime: " + str(UnixTime))
        #11/30/2011 @ 8:00pm (UTC)
        

        #https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]

        url = 'https://api.darksky.net/forecast/' + api_key + '/' + str(Lat_fireLoc) + ',' + str(Long_fireLoc) + ',' + str(int(UnixTime))

        response = requests.get(url)
        #print(response.url)

        data = response.json()
        #pprint(data['currently'])

        #pprint(data)

        csv_row_list = ['OBJECTID','FOD_ID','FPA_ID','apparentTemperatureHigh','apparentTemperatureHighTime','apparentTemperatureLow','apparentTemperatureLowTime','apparentTemperatureMax','apparentTemperatureMaxTime','apparentTemperatureMin','apparentTemperatureMinTime','dewPoint','humidity','icon','moonPhase','precipIntensity','precipIntensityMax','precipIntensityMaxTime','precipProbability','precipType','sunriseTime','sunsetTime','temperatureHigh','temperatureHighTime','temperatureLow','temperatureLowTime','temperatureMax','temperatureMaxTime','temperatureMin','temperatureMinTime','time','uvIndex','uvIndexTime','windBearing','windGust','windGustTime','windSpeed']        
        #df.to_excel() # Writes to an Excel file WeatherAPI_Data


        WeatherAPI_Data = open("WeatherAPI_Data.csv", "a")
        #dewPoint = str(data['currently']['dewPoint'])


        #converting JSON values to strings for the write function
        #try:

         
        OBJECTID = str(row[0])
        FOD_ID = str(row[1])
        FPA_ID = str(row[2])
        
        """ apparentTemperatureHigh = str(data['daily']['data'][0]['apparentTemperatureHigh'])
        apparentTemperatureHighTime = str(data['daily']['data'][0]['apparentTemperatureHighTime'])
        apparentTemperatureLow = str(data['daily']['data'][0]['apparentTemperatureLow'])
        apparentTemperatureLowTime = str(data['daily']['data'][0]['apparentTemperatureLowTime'])
        apparentTemperatureMax = str(data['daily']['data'][0]['apparentTemperatureMax'])
        apparentTemperatureMaxTime = str(data['daily']['data'][0]['apparentTemperatureMaxTime'])
        apparentTemperatureMin = str(data['daily']['data'][0]['apparentTemperatureMin'])
        apparentTemperatureMinTime = str(data['daily']['data'][0]['apparentTemperatureMinTime'])
        dewpoint = str(data['daily']['data'][0]['dewPoint'])
        humidity = str(data['daily']['data'][0]['humidity'])
        icon = str(data['daily']['data'][0]['icon'])
        moonPhase = str(data['daily']['data'][0]['moonPhase'])
        precipIntensity = str(data['daily']['data'][0]['precipIntensity'])
        precipIntensityMax = str(data['daily']['data'][0]['precipIntensityMax'])
        precipIntensityMaxTime = str(data['daily']['data'][0]['precipIntensityMaxTime'])
        precipProbability = str(data['daily']['data'][0]['precipProbability'])
        precipType = str(data['daily']['data'][0]['precipType'])
        sunriseTime = str(data['daily']['data'][0]['sunriseTime'])
        sunsetTime = str(data['daily']['data'][0]['sunsetTime'])
        temperatureHigh = str(data['daily']['data'][0]['temperatureHigh'])
        temperatureHighTime = str(data['daily']['data'][0]['temperatureHighTime'])
        temperatureLow = str(data['daily']['data'][0]['temperatureLow'])
        temperatureLowTime = str(data['daily']['data'][0]['temperatureLowTime'])
        temperatureMax = str(data['daily']['data'][0]['temperatureMax'])
        temperatureMaxTime = str(data['daily']['data'][0]['temperatureMaxTime'])
        temperatureMin = str(data['daily']['data'][0]['temperatureMin'])
        temperatureMinTime = str(data['daily']['data'][0]['temperatureMinTime'])
        time = str(data['daily']['data'][0]['time'])
        uvIndex = str(data['daily']['data'][0]['uvIndex'])
        uvIndexTime = str(data['daily']['data'][0]['uvIndexTime'])
        windBearing = str(data['daily']['data'][0]['windBearing'])
        windGust = str(data['daily']['data'][0]['windGust'])
        windGustTime = str(data['daily']['data'][0]['windGustTime'])
        windSpeed = str(data['daily']['data'][0]['windSpeed'])
 """
        latitude_print = str(data['latitude'])
        longitude_print = str(data['longitude'])
        offset_print = str(data['offset'])
        timezone_print = str(data['timezone'])


        #df = print(pd.DataFrame(data))
        #WeatherAPI_Data.write(OBJECTID + "," + FOD_ID + "," + FPA_ID + "," + apparentTemperatureHigh + "," + apparentTemperatureHighTime + "," + apparentTemperatureLow + "," + apparentTemperatureLowTime + "," + apparentTemperatureMax + "," + apparentTemperatureMaxTime + "," + apparentTemperatureMin + "," + apparentTemperatureMinTime + "," + dewpoint + "," + humidity + "," + "," + moonPhase + "," + precipIntensity + "," + precipIntensityMax + "," + precipIntensityMaxTime + "," + precipProbability + "," + precipType + "," + sunriseTime + "," + sunsetTime + "," + temperatureHigh + "," + temperatureHighTime + "," + temperatureLow + "," + temperatureLowTime + "," + temperatureMax + "," + temperatureMaxTime + "," + temperatureMin + "," + temperatureMinTime + "," + time + "," + uvIndex + "," + uvIndexTime + "," + windBearing + "," + windGust + "," + windGustTime + "," + windSpeed + "," + latitude_print + "," + longitude_print + "," + offset_print + "," + timezone_print + "\n")
        #WeatherAPI_Data.write(OBJECTID + "," + FOD_ID + "," + FPA_ID + "," + apparentTemperatureHigh + "," + apparentTemperatureHighTime + "," + apparentTemperatureLow + "," + apparentTemperatureLowTime + "," + apparentTemperatureMax + "," + apparentTemperatureMaxTime + "," + apparentTemperatureMin + "," + apparentTemperatureMinTime + "," + dewpoint + "," + humidity + "," + "," + moonPhase + "," + precipIntensity + "," + precipIntensityMax + "," + precipIntensityMaxTime + "," + precipProbability + "," + precipType + "," + sunriseTime + "," + sunsetTime + "," + temperatureHigh + "," + temperatureHighTime + "," + temperatureLow + "," + temperatureLowTime + "," + temperatureMax + "," + temperatureMaxTime + "," + temperatureMin + "," + temperatureMinTime + "," + time + "," + uvIndex + "," + uvIndexTime + "," + windBearing + "," + windGust + "," + windGustTime + "," + windSpeed + "," + latitude_print + "," + longitude_print + "," + offset_print + "," + timezone_print + "\n")
        
        #Adding first 3 values to csv_add
        csv_add = [OBJECTID,FOD_ID,FPA_ID]
        
        #Checks every value in csv_row_list against "daily" key in API JSON and appends to a list. If value is not there. it appends an empty string
        for column in csv_row_list[3:]:

            try:
                value = str(data['daily']['data'][0][column])
                csv_add.append(value)
            except:
                csv_add.append("")
        
        #adding last 4 values to list
        csv_add.append(latitude_print)
        csv_add.append(longitude_print)
        csv_add.append(offset_print)
        csv_add.append(timezone_print)

        #Joined all values in list as long string limited with commas for the CSV
        csv_add_join = ",".join(csv_add)
        #WeatherAPI_Data.write(OBJECTID + "," + FOD_ID + "," + FPA_ID + "," + apparentTemperatureHigh + "," + apparentTemperatureHighTime + "," + apparentTemperatureLow + "," + apparentTemperatureLowTime + "," + apparentTemperatureMax + "," + apparentTemperatureMaxTime + "," + apparentTemperatureMin + "," + apparentTemperatureMinTime + "," + dewpoint + "," + humidity + "," + "," + moonPhase + "," + precipIntensity + "," + precipIntensityMax + "," + precipIntensityMaxTime + "," + precipProbability + "," + precipType + "," + sunriseTime + "," + sunsetTime + "," + temperatureHigh + "," + temperatureHighTime + "," + temperatureLow + "," + temperatureLowTime + "," + temperatureMax + "," + temperatureMaxTime + "," + temperatureMin + "," + temperatureMinTime + "," + time + "," + uvIndex + "," + uvIndexTime + "," + windBearing + "," + windGust + "," + windGustTime + "," + windSpeed + "," + latitude_print + "," + longitude_print + "," + offset_print + "," + timezone_print + "\n")
        
        WeatherAPI_Data.write(csv_add_join + "\n")
        
        #print((OBJECTID + "," + FOD_ID + "," + FPA_ID + "," + apparentTemperatureHigh + "," + apparentTemperatureHighTime + "," + apparentTemperatureLow + "," + apparentTemperatureLowTime + "," + apparentTemperatureMax + "," + apparentTemperatureMaxTime + "," + apparentTemperatureMin + "," + apparentTemperatureMinTime + "," + dewpoint + "," + humidity + "," + "," + moonPhase + "," + precipIntensity + "," + precipIntensityMax + "," + precipIntensityMaxTime + "," + precipProbability + "," + precipType + "," + sunriseTime + "," + sunsetTime + "," + temperatureHigh + "," + temperatureHighTime + "," + temperatureLow + "," + temperatureLowTime + "," + temperatureMax + "," + temperatureMaxTime + "," + temperatureMin + "," + temperatureMinTime + "," + time + "," + uvIndex + "," + uvIndexTime + "," + windBearing + "," + windGust + "," + windGustTime + "," + windSpeed + "," + latitude_print + "," + longitude_print + "," + offset_print + "," + timezone_print + "\n"))
               #print("apparentTemperatureHigh: "  +apparentTemperatureHigh)
               
        #OBJECTID	FOD_ID	FPA_ID	apparentTemperatureHigh	apparentTemperatureHighTime	apparentTemperatureLow	apparentTemperatureLowTime	apparentTemperatureMax	apparentTemperatureMaxTime	apparentTemperatureMin	apparentTemperatureMinTime	dewPoint	humidity	icon	moonPhase	precipIntensity	precipIntensityMax	precipIntensityMaxTime	precipProbability	precipType	sunriseTime	sunsetTime	temperatureHigh	temperatureHighTime	temperatureLow	temperatureLowTime	temperatureMax	temperatureMaxTime	temperatureMin	temperatureMinTime	time	uvIndex	uvIndexTime	windBearing	windGust	windGustTime	windSpeed
        fireFile.close()
        WeatherAPI_Data.close()
        print("Printing Call#: " + str(counter) + "      API Url: " + url + "    Object ID: " + OBJECTID)
        #except KeyError:
            #print("KeyError: Keep moving")

print("Done printing to CSV!")
