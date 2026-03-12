# source https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates/data
import tkinter
cnv = tkinter.Canvas(bg='white', width=400, height=500) #nezabudnúť veľké C v Canvas
cnv.pack()
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
lb = tkinter.Listbox(selectmode='multiple', width=10,height=15)
lb.pack()
lb.insert(0, 'Toto vkladam na zaciatok (vrch) listboxu')

cnv.mainloop()

