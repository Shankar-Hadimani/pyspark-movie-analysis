import folium
import pandas as pd

# read volcanoes flat file
data = pd.read_csv("tesla\\pyLearnMegaCourse\\webmap\\Volcanoes.txt")

# create list with latitude and longitude individually
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def icon_color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 2000:
        return 'orange'
    else:
        return 'red'

#create a map object to locate the latitudes and longitudes on map
map = folium.Map(location=[35.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

 # create a feature group and assign markers and icon color
fgv = folium.FeatureGroup("volcanoes")

# add markers on map for each latitudes and longitudes from respective lists
for lt,ln,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name,name,el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=icon_color_producer(el),)))
    #fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup(iframe),fill_color=icon_color_producer(el),color='grey',fill_capacity=0.6))

# add polygons in the map
fgp = folium.FeatureGroup("population")
fgp.add_child(folium.GeoJson(data=open("tesla\\pyLearnMegaCourse\\webmap\\world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# add feature group to as a child object
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
# save as html 
map.save("tesla\\pyLearnMegaCourse\\Map_html_popup_simple.html")
