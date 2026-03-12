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