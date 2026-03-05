# source https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates/data
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

import tkinter
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.add_feature(cfeature.BORDERS)


with open('airpollution.csv') as f:
    f.readline()
    udaje = f.read().strip().split("\n")

def world_map():
    ax.set_extent([67, 98, 5, 38])
    for riadok in udaje:
        aktualne = riadok.split(',')
        country = aktualne[0]
        city = aktualne[1]
        AQI_value = int(aktualne[2])
        AQI_category = aktualne[3]
        CO_AQI_value = int(aktualne[4])
        CO_AQI_category = aktualne[5]
        Ozone_AQI_value = int(aktualne[6])
        Ozone_AQI_category = aktualne[7]
        NO2_AQI_value = int(aktualne[8])
        NO2_AQI_category = aktualne[9]
        PM2_5_AQI_value = int(aktualne[10])
        PM2_5_AQI_category = aktualne[11]
        lat = float(aktualne[12])
        lng = float(aktualne[13])
        if AQI_category == 'Good':
            plt.plot(lng, lat, marker='o', color='green', markersize=1, transform=ccrs.PlateCarree())
        if AQI_category == 'Moderate':
            plt.plot(lng, lat, marker='o', color='yellow', markersize=1, transform=ccrs.PlateCarree())
        if AQI_category == 'Unhealthy':
            plt.plot(lng, lat, marker='o', color='red', markersize=1, transform=ccrs.PlateCarree())
        if AQI_category == 'Very Unhealthy':
            plt.plot(lng, lat, marker='o', color='black', markersize=1, transform=ccrs.PlateCarree())
        if AQI_category == 'Unhealthy for Sensitive Groups':
            plt.plot(lng, lat, marker='o', color='orange', markersize=1, transform=ccrs.PlateCarree())

# Europe if 35<=lat<=72 and -25<=lng<=40:
# Africa	if 35<=lat<=35 and 20<=lng<=55:
# Asia	if 10<=lat<=80 and 25<=lng<=180:
# North America	if 7<=lat<=83 and 170<=lng<=20:
# South America	if 55<=lat<=13 and 82<=lng<=35:
# Australia / Oceania	if -50<=lat<=10 and 110<=lng<=180:
# Southeast Asia if 11<=lat<=28 and 92<=lng<=141:

def draw():
    for riadok in udaje:
        aktualne = riadok.split(',')
        AQI_category = aktualne[3]
        CO_AQI_category = aktualne[5]
        Ozone_AQI_category = aktualne[7]
        NO2_AQI_category = aktualne[9]
        PM2_5_AQI_category = aktualne[11]
        lat = float(aktualne[12])
        lng = float(aktualne[13])
        teraz = NO2_AQI_category
        if 35<=lat<=72 and -25<=lng<=40:
            if teraz == 'Good':
                plt.plot(lng, lat, marker='o', color='green', markersize=1, transform=ccrs.PlateCarree())
            if teraz == 'Moderate':
                plt.plot(lng, lat, marker='o', color='yellow', markersize=1, transform=ccrs.PlateCarree())
            if teraz == 'Unhealthy':
                plt.plot(lng, lat, marker='o', color='red', markersize=1, transform=ccrs.PlateCarree())
            if teraz == 'Very Unhealthy':
                plt.plot(lng, lat, marker='o', color='black', markersize=1, transform=ccrs.PlateCarree())
            if teraz == 'Unhealthy for Sensitive Groups':
                plt.plot(lng, lat, marker='o', color='orange', markersize=1, transform=ccrs.PlateCarree())
draw()
print('ok')
plt.savefig("world.png")
print("ok")
plt.show()