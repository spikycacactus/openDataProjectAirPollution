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

#country = aktualne[0]
#city = aktualne[1]
#AQI_value = int(aktualne[2])
#AQI_category = aktualne[3]
#CO_AQI_value = int(aktualne[4])
#CO_AQI_category = aktualne[5]
#Ozone_AQI_value = int(aktualne[6])
#Ozone_AQI_category = aktualne[7]
#NO2_AQI_value = int(aktualne[8])
#NO2_AQI_category = aktualne[9]
#PM2_5_AQI_value = int(aktualne[10])
#PM2_5_AQI_category = aktualne[11]
#lat = float(aktualne[12])
#lng = float(aktualne[13])
def draw(co, minlat, minlng, maxlat, maxlng):
    good_lng, good_lat = [], []
    moderate_lng, moderate_lat = [], []
    unhealthy_lng, unhealthy_lat = [], []
    very_lng, very_lat = [], []
    sensitive_lng, sensitive_lat = [], []
    for riadok in udaje:
        aktualne = riadok.split(',')
        lat = float(aktualne[12])
        lng = float(aktualne[13])
        teraz = aktualne[co]
        if minlat<=lat<=maxlat and minlng<=lng<=maxlng:
            if teraz == 'Good':
                good_lng.append(lng)
                good_lat.append(lat)
            if teraz == 'Moderate':
                moderate_lng.append(lng)
                moderate_lat.append(lat)
            if teraz == 'Unhealthy':
                unhealthy_lng.append(lng)
                unhealthy_lat.append(lat)
            if teraz == 'Very Unhealthy':
                very_lng.append(lng)
                very_lat.append(lat)
            if teraz == 'Unhealthy for Sensitive Groups':
                sensitive_lng.append(lng)
                sensitive_lat.append(lat)
    plt.scatter(good_lng, good_lat, color='green', s=1, transform=ccrs.PlateCarree())
    plt.scatter(moderate_lng, moderate_lat, color='orange', s=1, transform=ccrs.PlateCarree())
    plt.scatter(unhealthy_lng, unhealthy_lat, color='red', s=1, transform=ccrs.PlateCarree())
    plt.scatter(very_lng, very_lat, color='black', s=1, transform=ccrs.PlateCarree())
    plt.scatter(sensitive_lng, sensitive_lat, color='yellow', s=1, transform=ccrs.PlateCarree())
    print(len(good_lng))


regions = {
    "World": (-90, -180, 90, 180),
    "North America": (5, -170, 83, -50),
    "South America": (-56, -82, 13, -34),
    "Europe": (35, -25, 72, 45),
    "Africa": (-35, -20, 37, 52),
    "Asia": (5, 25, 80, 180),
    "Oceania": (-50, 110, 0, 180),
}
currentregion = "Asia"
draw(3, regions[currentregion][0], regions[currentregion][1], regions[currentregion][2], regions[currentregion][3])
print('ok')
plt.savefig("world.png")
print("ok")
plt.show()