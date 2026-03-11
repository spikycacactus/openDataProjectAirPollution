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
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)



# Embed matplotlib figure into Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


root.mainloop()