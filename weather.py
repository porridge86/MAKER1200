# Url
import requests
# Read json file
import json
# Random number
import random
# Export data to Excel
import pandas as pd

# City setting
# if you add more cities, write here


def chooseCity(city):
    dict_Oslo = {'latitude': '59.9138',
                 'longitude': '10.7387', 'timezone': 'Europe%2FBerlin'}
    dict_Tokyo = {'latitude': '35.6785',
                  'longitude': '139.6823', 'timezone': 'Asia%2FTokyo'}
    if city == "Oslo":
        return dict_Oslo
    elif city == "Tokyo":
        return dict_Tokyo
    else:
        print("error.")

# weathercode to texts
# descriptions are from website Open Meteo


def giveWeatherData(weathercode):
    if weathercode == 0:
        return ("Clear sky ")
    elif weathercode in [1, 2, 3]:
        return (" Mainly clear, partly cloudy, and overcast")
    elif weathercode in [45, 48]:
        return (" Fog and depositing rime fog")
    elif weathercode in [51, 53, 55]:
        return (" Drizzle: Light, moderate, and dense intensity. It’s raining but barely noticeable.")
    elif weathercode in [56, 57]:
        return (" Freezing Drizzle: Light and dense intensity")
    elif weathercode in [61, 63, 65]:
        return (" Rain: Slight, moderate and heavy intensity")
    elif weathercode in [66, 67]:
        return (" Freezing Rain: Light and heavy intensity")
    elif weathercode in [71, 73, 75]:
        return (" Snow fall: Slight, moderate, and heavy intensity")
    elif weathercode in [77]:
        return (" Snow grains")
    elif weathercode in [80, 81, 82]:
        return (" Rain showers: Slight, moderate, and violent")
    elif weathercode in [85, 86]:
        return (" Snow showers slight and heavy")
    elif weathercode in [95]:
        return (" Thunderstorm: Slight or moderate")
    elif weathercode in [96, 99]:
        return (" Thunderstorm with slight and heavy hail")
    else:
        return ("We will see...")

# Show message


def showMessage(data, city, day, dayAsString):
    # dato
    dato = data["daily"]["time"][day]
    # weather
    weather = giveWeatherData(data["daily"]["weathercode"][day])
    # max temperture
    max_temp = data["daily"]["temperature_2m_max"][day]
    # min temperture
    min_temp = data["daily"]["temperature_2m_min"][day]
    message = city + ": " + str(dato) + " (" + dayAsString + " - local time)"
    message = city + ": " + str(dato) + " (" + dayAsString + " - local time)" + "\n" + "The weather is " + weather + \
        ". " + "\n" + "Max tempurture will be " + \
        str(max_temp) + "°C" + " and minimum tempurture will be " + \
        str(min_temp) + "°C.\n\n"
    print(message)


# Open Meteo Url
api_url = "https: // api.open-meteo.com/v1/forecast?latitude={latitude} & longitude={longitude} & daily=weathercode, temperature_2m_max, temperature_2m_min, precipitation_sum & timezone={timezone}"
# if you add more cities, write here
cities = ["Oslo", "Tokyo"]
# Days :  if you add more days to display, change here
days = {"Today": 0, "Tomorrow": 1}
cityData = {}
for city in cities:
    cityDict = chooseCity(city)
    url = api_url.format(
        latitude=cityDict["latitude"], longitude=cityDict["longitude"], timezone=cityDict["timezone"])
# get url
    response = requests.get(url)
    # put json's data in "data"
    data = json.loads(response.text)
    cityData[city] = data
    # today/tomorrow, Oslo/Tokyo
    for day in days:
        showMessage(data, city, days[day], day)

# EndMessage randomMessage
# Give random number and show the message as randomMessage
if __name__ == '__main__':
    # Random messages
    randomMessage = {
        1: "Have a good day!",
        2: "Have a beautiful day!",
        3: "Have a lovely day!",
        4: "Have a great day!",
        5: "Have an amazing day!"
    }
    # pick one number
    dice = random.randint(1, 5)
    print(randomMessage[dice])

# Excel
# Make tables(dataframe)
# Dato   Weather  Max temp  Min temp
# Oslo
# 0   **/**   A1        B1         C1
# 1   **/**   A2        B2         C2
# Dato    Weather  Max temp  Min temp
# Tokyo
# 0     **/** AA1       BB1        CC1
# 1     **/** AA2       BB2        CC2

# Number of Days is corresbonding to the number in dataFrames's number(e.g.2) below.


def returnDataFrame(data, city, numberOfDays):
    weatherCode = data["daily"]["weathercode"][0:numberOfDays]
    # make weather messages from weatherCode and put it in "weather"
    weather = map(giveWeatherData, weatherCode)
    max_temp = data["daily"]["temperature_2m_max"][0:numberOfDays]
    min_temp = data["daily"]["temperature_2m_min"][0:numberOfDays]
    date = data["daily"]["time"][0:numberOfDays]
    df = pd.DataFrame(
        data={'Date': date, 'Weather': weather, 'Max Temp': max_temp, 'Min Temp': min_temp})
    df.index.name = city
    print(df)
    return df


# if "2" in returnDataFrame, it means 2 days ("today" & "tomorrow") and it will be "numberOfDays"
# if you add more days to display, change here
dataFrames = []
for key in cityData:
    dataFrames.append(returnDataFrame(cityData[key], key, 2))

# Path and sheet name, and show error
try:
    with pd.ExcelWriter("pandas_to_excel.xlsx") as writer:
        for df in dataFrames:
            df.to_excel(writer, sheet_name=df.index.name)
    print('Data is saved as excel file.')
except ZeroDivisionError:
    print('Error')
