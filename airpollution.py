# source https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates/data
from operator import index
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import tkinter

from matplotlib.pyplot import nipy_spectral
from ttkwidgets.autocomplete import AutocompleteCombobox

root = tkinter.Tk()
cnv = tkinter.Canvas(root, bg='white', width=550, height=300)
cnv.grid(column=1,row=0,rowspan=2,columnspan=3)

# fonty
velmi_hruby = ("Arial", 12, 'bold')
hruby = ("Arial", 10, 'bold')
normalny = ("Arial", 10)
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
        'Unhealthy for Sensitive Groups':{'coords' : [], 'color' : 'blue'},
        'Hazardous':{'coords' : [], 'color' : 'purple'},
    }

    # bunusove listy
    # least_polluted_cities
    least_poll = []
    least_poll_v = []
    least_pollutted_cities = []
    # most polluted cities
    most_poll = []
    most_poll_v = []
    most_pollutted_cities = []
    stations_in_countries = {}
    AQI_in_countries = {}
    average_AQI_in_country = {}
    value_for_avr = 0
    number_of_values = 0
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
            #if country not in stations_in_countries:
               # stations_in_countries[country] = 1
           # elif country in stations_in_countries:
                #stations_in_countries[country] += 1

            # least polluted cities, vytvori zoznam desiatich miest a ich hodnot a nahradza ich ked maju mensie znecistenie
            if len(least_poll) < 10 and city not in least_poll_v:
                least_poll.append(int(aktualne[co-1]))
                least_poll_v.append(city)
            elif int(aktualne[co-1]) < max(least_poll) and city not in least_poll_v:
                ind = least_poll.index(max(least_poll))
                least_poll[ind] = int(aktualne[co-1])
                least_poll_v[ind] = city

            # most polluted cities, vytvori zoznam desiatich miest a ich hodnot a nahradza ich ked maju vacsie znecistenie
            if len(most_poll) < 10 and city not in most_poll_v:
                most_poll.append(int(aktualne[co-1]))
                most_poll_v.append(city)
            elif int(aktualne[co-1]) > min(most_poll) and city not in most_poll_v:
                ind = most_poll.index(min(most_poll))
                most_poll[ind] = int(aktualne[co-1])
                most_poll_v[ind] = city
            value_for_avr += int(aktualne[co-1])
            number_of_values += 1
            # countries by pollution per city
            #if country not in AQI_in_countries:
                #AQI_in_countries[country] = AQI_value
            #elif country in AQI_in_countries:
               # AQI_in_countries[country] += AQI_value
    #for country in AQI_in_countries:
       # average = AQI_in_countries[country] // stations_in_countries[country]
        #average_AQI_in_country[country] = average

    # spravi jeden zoznam z miest a hodnot namjmensieho znecistenia
    for i in range(len(least_poll)):
        least_pollutted_cities.append((least_poll[i], least_poll_v[i]))
    #sortne najmenej polluted cities
    least_pollutted_cities.sort()

    # spravi jeden zoznam z miest a hodnot najvacsieho znecistenia
    for i in range(len(least_poll)):
        most_pollutted_cities.append((most_poll[i], most_poll_v[i]))
    #sortne najviac polluted cities
    most_pollutted_cities.sort(reverse=True)

    #print(average_AQI_in_country)
    #print(stations_in_countries)
   # print(AQI_in_countries)

    # vykresli mapu
    dokopy_stanic = 0
    for value in climate:
        dokopy_stanic += len(climate[value]['coords']) // 2
        plt.scatter(climate[value]['coords'][::2], climate[value]['coords'][1::2], color=climate[value]['color'], s=1, transform=ccrs.PlateCarree())

    # vymaze Canvas
    cnv.delete("all")

    # kresli graf poctu stanic a legendu
    posledne=0
    y = 160
    for typ in climate:
        y+=15
        kolko = len(climate[typ]['coords'])//2
        percenta = (len(climate[typ]['coords'])/2) / dokopy_stanic
        if percenta == 1:
            cnv.create_oval(25, 25, 150, 150, fill=climate[typ]['color'], outline='')
            cnv.create_text(10, y, fill=climate[typ]['color'], text = 'Only Good' +': ' + str(kolko), anchor = 'w', font=normalny)
            return
        else:
            cnv.create_arc(25, 25, 150, 150, start=posledne, extent=percenta * 360, fill=climate[typ]['color'], outline="")
        posledne += percenta * 360
        if typ == 'Unhealthy for Sensitive Groups':
            cnv.create_text(10, y, fill=climate[typ]['color'], text = 'Unhealthy for Senstive' +': ' + str(kolko), anchor = 'w', font=normalny)
        else:
            cnv.create_text(10, y, fill=climate[typ]['color'], text= typ + ': ' + str(kolko), anchor='w', font=normalny)
    y = 30
    cnv.create_text(200, y-5, fill='black', text="Least polluted", anchor='w', font=hruby)
    cnv.create_text(350, y-5, fill='black', text="Most polluted", anchor='w', font=hruby)
    # kresli najmenej znecistene mesta nazvy
    for i in range(len(least_pollutted_cities)):
        y+=15
        cnv.create_text(200, y, fill='black', text=least_pollutted_cities[i][1] + ': ' + str(least_pollutted_cities[i][0]), anchor='w', font= normalny)
        cnv.create_text(350, y, fill='black', text=most_pollutted_cities[i][1] + ': ' + str(most_pollutted_cities[i][0]), anchor='w', font = normalny)
    average= int(value_for_avr)/ number_of_values
    cnv.create_text(200, y+50, fill='black', text= 'Average value: ' + str(average), anchor='w')
    # kresli mapu
    plt.show()

regions = {
    "World": (-90, -180, 90, 180),
    "North America": (5, -170, 83, -50),
    "South America": (-56, -82, 13, -34),
    "Europe": (35, -25, 72, 45),
    "Africa": (-35, -20, 37, 52),
    "Asia": (5, 25, 80, 180),
    "Oceania": (-50, 110, 0, 180),
    "Western Europe": (43, -10, 56, 15),
    "Central Europe": (45, 5, 55, 25),
    "Eastern Europe": (44, 20, 60, 45),
    "Northern Europe": (54, -10, 72, 35),
    "Southern Europe": (35, -10, 45, 30),
    "Balkans": (37, 13, 47, 29),
    "Scandinavia": (55, 5, 72, 32),
    "USA West": (30, -125, 50, -105),
    "USA East": (25, -105, 50, -65),
    "Canada": (45, -140, 75, -50),
    "Central America": (5, -95, 23, -75),
    "Caribbean": (10, -85, 25, -60),
    "South America North": (-5, -80, 15, -45),
    "South America South": (-55, -75, -5, -35),
    "North Africa": (15, -20, 37, 35),
    "West Africa": (-5, -20, 20, 15),
    "East Africa": (-12, 30, 15, 52),
    "Central Africa": (-10, 10, 10, 35),
    "Southern Africa": (-35, 10, -10, 40),
    "Middle East": (12, 30, 40, 65),
    "Central Asia": (35, 50, 55, 85),
    "South Asia": (5, 65, 35, 95),
    "East Asia": (20, 100, 50, 145),
    "Southeast Asia": (-10, 95, 25, 135),
    "China Region": (18, 73, 54, 135),
    "Japan & Korea": (30, 120, 47, 150),
    "Australia": (-45, 110, -10, 155),
}

type = {
    "AQI":3,
    "CO":5,
    "Ozone":7,
    "NO2":9,
    "PM2_5":11
}

pomoc_text = [
    'Pomoc',
    '',
    'Program slúži na vykresľovanie miest, ',
    'v ktorých je stanica merajúca hodnoty znečistenia rôznych plynov.',
    '',
    'Na ľavo sú dva zoznamy:',
    'v hornom vieme nastaviť región na vykreslenie',
    'V spodnom plyn, ktorého údaje chceme zistiť. ',
    '',
    'Program spustíme tlačítkom Kresli, ktoré sa nachádza dole pod plátnom. ',
    '',
    '',
    'Na pravej strane sa nachádza políčko na písanie,',
    'kde vieme zistiť hodnoty jednotlivých plynov pre mesto nášho výberu.',
    '',
    'Na vypísanie musíme kliknúť na malú šípku vedľa vpisovacieho políčka ',
    'a kliknúť na naše vybrané mesto.',
]
pomoc_text_bold = [2,5,9,12,15,16]
def Pomoc():
    cnv.delete("all")
    y=15
    i=0
    for napisane in pomoc_text:
        y+=15
        if i == 0:
            cnv.create_text(10, y, text=napisane, anchor="w", font=velmi_hruby)
        elif i in pomoc_text_bold:
            cnv.create_text(10, y, text=napisane, anchor="w", font=hruby)
        else:
            cnv.create_text(10, y, text=napisane,anchor="w", font=normalny)
        i+=1

Pomoc()
currentregion = "World"
def spusti():
    #zisti selktnuty index a povie aky region/krajina su oznacene, nasledne spusti funkciu an vykreslovanie
    index_region = lb.curselection()[0]
    currentregion = lb.get(index_region)
    typ = lb2.curselection()[0]
    co = lb2.get(typ)
    draw(type[co], regions[currentregion][0], regions[currentregion][1], regions[currentregion][2],regions[currentregion][3])

#spravi tlacidlo
tkinter.Button(text='Kresli', command=spusti).grid(column=2, row=2)
tkinter.Button(text='Pomoc', command=Pomoc).grid(column=3,row=2)
# spravi listbox a prida regiony
lb = tkinter.Listbox(exportselection=False, selectmode='single', width=10,height=10)
for region in regions:
    lb.insert(tkinter.END, region)
lb.grid(column=0,row=0)

lb2 = tkinter.Listbox(exportselection=False,selectmode='single', width=10,height=8)
for typ in type:
    lb2.insert(tkinter.END, typ)
lb2.grid(column=0,row=1)

lb.selection_set(0)   # vyberie "World"
lb2.selection_set(0)  # vyberie prvý typ

cnv2 = tkinter.Canvas(root, bg='white', width=300, height=100)
cnv2.grid(column=5,row=1 ,sticky=tkinter.N)

def vyber(event):
    vybrane = combobox.get()
    cnv2.delete("all")
    for riadok in udaje:
        aktualne = riadok.split(',')
        if aktualne[1] == vybrane:
            y=0
            for typ in type:
                y += 15
                print(str(aktualne[type[typ]]))
                cnv2.create_text(0, y, fill='black',
                                text=typ + ': ' + str(aktualne[type[typ]]) + ', value: ' + str(aktualne[type[typ]+1]), anchor='w')
            break
# vytvori databazu miest
nazvy_miest = []
for riadok in udaje:
    aktualne = riadok.split(',')
    nazvy_miest.append(aktualne[1])

combobox = AutocompleteCombobox(root, completevalues=nazvy_miest)
combobox.bind("<<ComboboxSelected>>", vyber)
combobox.grid(column=5,row=0, sticky=tkinter.S)
cnv.mainloop()