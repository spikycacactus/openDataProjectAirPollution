# source https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates/data
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import tkinter
cnv = tkinter.Canvas(bg='white', width=500, height=200)
cnv.grid(column=1,row=0)

#country = aktualne[0]
#city = aktualne[1]
#AQI_value = int(aktualne[2])
#CO_AQI_value = int(aktualne[4])
#Ozone_AQI_value = int(aktualne[6])
#NO2_AQI_value = int(aktualne[8])
#PM2_5_AQI_value = int(aktualne[10])
#lat = float(aktualne[12])
#lng = float(aktualne[13])


with open('airpollution.csv') as f:
    f.readline()
    udaje = f.read().strip().split("\n")

def draw(co, minlat, minlng, maxlat, maxlng):
    # vymaze staru mapku
    plt.clf()
    # vykresli mapku
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)

    # spravi zoznamy na ukladanie pozicii bodov
    climate = {
        'Good': {'coords' : [], 'color' : 'green'},
        'Moderate':{'coords' : [], 'color' : 'orange'},
        'Unhealthy':{'coords' : [], 'color' : 'red'},
        'Very Unhealthy':{'coords' : [], 'color' : 'black'},
        'Unhealthy for Sensitive Groups':{'coords' : [], 'color' : 'yellow'},
        'Hazardous':{'coords' : [], 'color' : 'purple'},
    }

    # bunusove listy
    stations_in_countries = {}
    least_polluted_cities = {}
    AQI_in_countries = {}
    average_AQI_in_country = {}
    for riadok in udaje:
        # udaje co potrebujeme
        aktualne = riadok.split(',')
        country = aktualne[0]
        city = aktualne[1]
        AQI_value = int(aktualne[2])
        lat = float(aktualne[12])
        lng = float(aktualne[13])
        teraz = aktualne[co]
        # pridava body do zoznamov
        if minlat<=lat<=maxlat and minlng<=lng<=maxlng:
            climate[teraz]['coords'].append(lng)
            climate[teraz]['coords'].append(lat)
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
        average = AQI_in_countries[country] // stations_in_countries[country]
        average_AQI_in_country[country] = average
    print(average_AQI_in_country)
    print(least_polluted_cities)
    print(stations_in_countries)
    print(AQI_in_countries)
    dokopy_stanic = 0
    for value in climate:
        dokopy_stanic += len(climate[value]['coords']) // 2
        plt.scatter(climate[value]['coords'][::2], climate[value]['coords'][1::2], color=climate[value]['color'], s=1, transform=ccrs.PlateCarree())
    cnv.delete("all")
    posledne=0
    x = 0
    y = 0
    for typ in climate:
        percenta=(len(climate[typ]['coords'])/2) / dokopy_stanic
        if percenta == 1:
            cnv.create_oval(25, 25, 150, 150, fill=climate[typ]['color'])
            return
        else:
            cnv.create_arc(25, 25, 150, 150, start=posledne, extent=percenta * 360, fill=climate[typ]['color'], outline="")

        posledne += percenta * 360
    plt.show()
    # kresli graf

regions = {
    "World": (-90, -180, 90, 180),
    "North America": (5, -170, 83, -50),
    "South America": (-56, -82, 13, -34),
    "Europe": (35, -25, 72, 45),
    "Africa": (-35, -20, 37, 52),
    "Asia": (5, 25, 80, 180),
    "Oceania": (-50, 110, 0, 180),
}
type = {
    "AQI_category":3,
    "CO_AQI_category":5,
    "Ozone_AQI_category":7,
    "NO2_AQI_category":9,
    "PM2_5_AQI_category":11
}

currentregion = "World"
def spusti():
    #zisti selktnuty index a povie aky region/krajina su oznacene
    index_region = lb.curselection()[0]
    currentregion = lb.get(index_region)
    typ = lb2.curselection()[0]
    co = lb2.get(typ)
    print(type[co])
    draw(type[co], regions[currentregion][0], regions[currentregion][1], regions[currentregion][2],regions[currentregion][3])

#spravi tlacidlo
tkinter.Button(text='Pokus', command=spusti).grid(column=1, row=1)

# spravi listbox a prida regiony
lb = tkinter.Listbox(exportselection=False, selectmode='single', width=10,height=10)
for region in regions:
    lb.insert(tkinter.END, region)
lb.grid(column=0,row=0)

lb2 = tkinter.Listbox(exportselection=False,selectmode='single', width=10,height=10)
for typ in type:
    lb2.insert(tkinter.END, typ)
lb2.grid(column=0,row=1)

lb.selection_set(0)   # vyberie "World"
lb2.selection_set(0)  # vyberie prvý typ

cnv.mainloop()