# fonty
BLACK = ("Arial", 12, 'bold')
BOLD = ("Arial", 10, 'bold')
NORMAL = ("Arial", 10)

CLIMATE_COLORS = {
        'Good': 'green',
        'Moderate': 'orange',
        'Unhealthy': 'red',
        'Very Unhealthy': 'black',
        'Unhealthy for Sensitive Groups': 'blue',
        'Hazardous': 'purple'
}
REGIONS = {
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

TYPES = {
    "AQI":{"cislo":3, "popisok":"AQI (Air Quality Index) – celkový index kvality ovzdušia."},
    "CO":{"cislo":5, "popisok":"CO (oxid uhoľnatý) – jedovatý plyn zo spaľovania, znižuje prenos kyslíka v krvi."},
    "Ozone":{"cislo":7, "popisok":"O₃ (prízemný ozón) - škodlivý pre pľúca."},
    "NO2":{"cislo":9, "popisok":"NO₂ (oxid dusičitý) – znečistenie z dopravy, dráždi dýchacie cesty."},
    "PM2_5":{"cislo":11, "popisok":"Jemné prachové častice, prenikajú do pľúc."}
}

HELP_TEXT = [
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
# Kresli Pomoc text
HELP_TEXT_BOLD = [2, 5, 9, 12, 15, 16]