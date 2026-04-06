# source = https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates/data
# zdroj pravdepodobne nie je zrovna najlepsi, v povodnom csv subori bolo vela miest, ktore mali vsetko rovnake okrem polohy (Delhi bolo aj v Europe), dal som to prefiltrovat umelej inteligencii(vymazalo 2738 riadkov)
# obcas sa stane, ze sa canvas alebo matplotlib neaktualizuje ked sa ma
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import tkinter
from ttkwidgets.autocomplete import AutocompleteCombobox
from constants import *

root = tkinter.Tk()
cnv = tkinter.Canvas(root, bg='white', width=550, height=300)
cnv.grid(column=1, row=0, rowspan=2, columnspan=3)

with open('airpollution.csv') as f:
    f.readline()
    data = f.read().strip().split("\n")

def draw(which_AQI, minlat, minlng, maxlat, maxlng):
    # pozicia ake AQI chceme v csv subore
    requested_AQI_position = TYPES[which_AQI]["number"]
    # vymaze staru mapku
    plt.clf()
    # vykresli mapku s brehmi a hranicami statov
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)

    # dictionary na ukladanie pozicii bodov
    climate = {
        'Good': {'coords': [], 'color': CLIMATE_COLORS["Good"]},
        'Moderate': {'coords': [], 'color': CLIMATE_COLORS["Moderate"]},
        'Unhealthy': {'coords': [], 'color': CLIMATE_COLORS["Unhealthy"]},
        'Very Unhealthy': {'coords': [], 'color': CLIMATE_COLORS["Very Unhealthy"]},
        'Unhealthy for Sensitive Groups': {'coords': [], 'color': CLIMATE_COLORS["Unhealthy for Sensitive Groups"]},
        'Hazardous': {'coords': [], 'color': CLIMATE_COLORS["Hazardous"]},
    }

    # least_polluted_cities
    least_poll = []
    least_poll_v = []
    least_pollutted_cities = []
    # most polluted cities
    most_poll = []
    most_poll_v = []
    most_pollutted_cities = []
    # average
    value_for_avr = 0
    number_of_values = 0
    for riadok in data:
        # udaje co potrebujeme
        actual = riadok.split(',')
        city = actual[1]
        lat = float(actual[12])
        lng = float(actual[13])
        current_AQI = actual[requested_AQI_position]
        # pridava body do climate dictionary
        if minlat <= lat <= maxlat and minlng <= lng <= maxlng:
            climate[current_AQI]['coords'].append(lng)
            climate[current_AQI]['coords'].append(lat)

            # least polluted cities, vytvori zoznam desiatich miest a ich AQI hodnot a nahradza ich ked maju mensie znecistenie
            if len(least_poll) < 10 and city not in least_poll_v:
                least_poll.append(int(actual[requested_AQI_position - 1]))
                least_poll_v.append(city)
            elif int(actual[requested_AQI_position - 1]) < max(least_poll) and city not in least_poll_v:
                ind = least_poll.index(max(least_poll))
                least_poll[ind] = int(actual[requested_AQI_position - 1])
                least_poll_v[ind] = city

            # most polluted cities, vytvori zoznam desiatich miest a ich AQI hodnot a nahradza ich ked maju vacsie znecistenie
            if len(most_poll) < 10 and city not in most_poll_v:
                most_poll.append(int(actual[requested_AQI_position - 1]))
                most_poll_v.append(city)
            elif int(actual[requested_AQI_position - 1]) > min(most_poll) and city not in most_poll_v:
                ind = most_poll.index(min(most_poll))
                most_poll[ind] = int(actual[requested_AQI_position - 1])
                most_poll_v[ind] = city
            value_for_avr += int(actual[requested_AQI_position - 1])
            number_of_values += 1

    # spravi jeden zoznam z miest a hodnot najmensieho znecistenia
    for i in range(len(least_poll)):
        least_pollutted_cities.append((least_poll[i], least_poll_v[i]))
    # zoradi najmenej znecistene mesta
    least_pollutted_cities.sort()

    # spravi jeden zoznam z miest a hodnot najvacsieho znecistenia
    for i in range(len(least_poll)):
        most_pollutted_cities.append((most_poll[i], most_poll_v[i]))
    # zoradi najviac znecistene mesta
    most_pollutted_cities.sort(reverse=True)

    # vykresli mapu a zrata pocet stanic v regione
    total_number_of_stations = 0
    for value in climate:
        total_number_of_stations += len(climate[value]['coords']) // 2
        plt.scatter(climate[value]['coords'][::2], climate[value]['coords'][1::2], color=climate[value]['color'], s=1,
                    transform=ccrs.PlateCarree())

    # vymaze platno
    cnv.delete("all")

    # kresli graf poctu stanic podla AQI a legendu
    start_of_arc = 0
    y = 160
    for typ in climate:
        y += 15
        current_number_of_stations = len(climate[typ]['coords']) // 2
        percentage = (len(climate[typ]['coords']) / 2) / total_number_of_stations
        if percentage == 1:
            cnv.create_oval(25, 25, 150, 150, fill=climate[typ]['color'], outline='')
            cnv.create_text(10, y, fill=climate[typ]['color'],
                            text='Only Good' + ': ' + str(current_number_of_stations), anchor='w', font=NORMAL)
            break
        else:
            cnv.create_arc(25, 25, 150, 150, start=start_of_arc, extent=percentage * 360, fill=climate[typ]['color'],
                           outline="")
        start_of_arc += percentage * 360
        if typ == 'Unhealthy for Sensitive Groups':
            cnv.create_text(10, y, fill=climate[typ]['color'],
                            text='Unhealthy for Senstive' + ': ' + str(current_number_of_stations), anchor='w',
                            font=NORMAL)
        else:
            cnv.create_text(10, y, fill=climate[typ]['color'], text=typ + ': ' + str(current_number_of_stations),
                            anchor='w', font=NORMAL)

    # kresli najmenej a najviac znecistene mesta
    y = 30
    cnv.create_text(200, y - 5, fill='black', text="Least polluted", anchor='w', font=BOLD)
    cnv.create_text(350, y - 5, fill='black', text="Most polluted", anchor='w', font=BOLD)
    for i in range(len(least_pollutted_cities)):
        y += 15
        cnv.create_text(200, y, fill='black',
                        text=least_pollutted_cities[i][1] + ': ' + str(least_pollutted_cities[i][0]), anchor='w',
                        font=NORMAL)
        cnv.create_text(350, y, fill='black',
                        text=most_pollutted_cities[i][1] + ': ' + str(most_pollutted_cities[i][0]), anchor='w',
                        font=NORMAL)

    # vypise priemernu hodnotu AQI
    average = int(value_for_avr) / number_of_values
    cnv.create_text(200, y + 50, fill='black', text='Average value: ' + str(average), anchor='w', font=BOLD)
    cnv.create_text(15, y + 100, text=TYPES[which_AQI]["description"], anchor='w', font=BOLD)

    # kresli mapu
    plt.show()

# kresli Pomoc
def help():
    cnv.delete("all")
    y = 15
    i = 0
    for text in HELP_TEXT:
        y += 15
        if i == 0:
            cnv.create_text(10, y, text=text, anchor="w", font=BLACK)
        elif i in HELP_TEXT_BOLD:
            cnv.create_text(10, y, text=text, anchor="w", font=BOLD)
        else:
            cnv.create_text(10, y, text=text, anchor="w", font=NORMAL)
        i += 1

help()

def draw_action():
    # zisti oznacene indexy v lisboxoch a povie aky region je oznaceny, a aky plyn. Nasledne spusti funkciu na vykreslovanie
    index_region = lb.curselection()[0]
    currentregion = lb.get(index_region)
    typ = lb2.curselection()[0]
    co = lb2.get(typ)
    draw(co, REGIONS[currentregion][0], REGIONS[currentregion][1], REGIONS[currentregion][2], REGIONS[currentregion][3])

# spravi tlacidla
tkinter.Button(text='Kresli', command=draw_action).grid(column=2, row=2)
tkinter.Button(text='Pomoc', command=help).grid(column=3, row=2)

# spravi listbox a prida regiony
lb = tkinter.Listbox(exportselection=False, selectmode='single', width=18, height=10)
for region in REGIONS:
    lb.insert(tkinter.END, region)
lb.grid(column=0, row=0)

# spravi listbox a prida plyny
lb2 = tkinter.Listbox(exportselection=False, selectmode='single', width=18, height=8)
for typ in TYPES:
    lb2.insert(tkinter.END, typ)
lb2.grid(column=0, row=1)

# vyberie World
lb.selection_set(0)
# vyberie AQI
lb2.selection_set(0)

# spravi Platno pre udaje jedneho mesta
cnv2 = tkinter.Canvas(root, bg='white', width=350, height=90)
cnv2.grid(column=5, row=1, sticky=tkinter.N)

def choose(event):
    # zisti ktore mesto sa vybralo a vypise jeho hodnoty AQI
    chosen = combobox.get()
    cnv2.delete("all")
    for line in data:
        current = line.split(',')
        if current[1] == chosen:
            y = 0
            for typ in TYPES:
                y += 15
                cnv2.create_text(10, y, fill=CLIMATE_COLORS[current[TYPES[typ]["number"]]],
                                 text=typ + ': ' + str(current[TYPES[typ]["number"]]), anchor='w', font=NORMAL)
                cnv2.create_text(255, y, fill=CLIMATE_COLORS[current[TYPES[typ]["number"]]],
                                 text='value: ' + str(current[TYPES[typ]["number"] - 1]), anchor='w', font=NORMAL)
            break


# vytvori databazu miest
names_of_cities = []
for line in data:
    current = line.split(',')
    names_of_cities.append(current[1])

# vytvori combobox s automatickym dopisovanim miest
combobox = AutocompleteCombobox(root, completevalues=names_of_cities)
# pri vybrani mesta spusti funkciu choose
combobox.bind("<<ComboboxSelected>>", choose)
combobox.grid(column=5, row=0, sticky=tkinter.S)
cnv.mainloop()