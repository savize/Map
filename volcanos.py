import pandas
import folium
# dir(folium)

data = pandas.read_csv("projects/Volcanoes.txt")
lat= list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colorProducer(elevs):
    if elevs < 1000:
        return 'green'
    elif 1000 <=elevs < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=6 , tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, elv in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup =str(elv) + " m", icon = folium.Icon(color =colorProducer(elv))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("projects/world.json", "r", encoding= "utf-8-sig").read(),
style_function=lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red" }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("map2.html")