import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import cartopy.crs as ccrs
import cartopy.feature as cfeature


root = tk.Tk()
root.geometry("800x600")


# Create matplotlib figure with Cartopy projection
fig = plt.Figure(figsize=(8,6))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

# Add map features
ax.coastlines()
ax.add_feature(cfeature.BORDERS)

# Embed matplotlib figure into Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=100,y=0,width = 800, height=600)
def test():
    print('ok')
tk.Button(text='Pokus', command=test).pack()
lb = tk.Listbox(selectmode='multiple', width=10,height=15)
lb.pack()
lb.insert(0, 'Toto vkladam na zaciatok (vrch) listboxu')

root.mainloop()
with open('airpollution.csv') as f:
    f.readline()
    udaje = f.read().strip().split("\n")

# dictionaries
stations_in_countries = {}
least_polluted_cities = {}
AQI_in_countries = {}
average_AQI_in_country = {}
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
    # rata kolko stanic je v danej krajine
    if country not in stations_in_countries:
        stations_in_countries[country] = 1
    elif country in stations_in_countries:
        stations_in_countries[country] += 1

    # least polluted cities
    if AQI_value <= 10:
        least_polluted_cities[city] = AQI_value

    # countries by pollution per city
    if country not in AQI_in_countries:
        AQI_in_countries[country] = AQI_value
    elif country in AQI_in_countries:
        AQI_in_countries[country] += AQI_value

for country in AQI_in_countries:
    average = AQI_in_countries[country]/stations_in_countries[country]
    average_AQI_in_country[country] = average

print(average_AQI_in_country)
print(least_polluted_cities)
print(stations_in_countries)
print(AQI_in_countries)