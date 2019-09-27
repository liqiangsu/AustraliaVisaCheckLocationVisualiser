import gmaps
import json
import subprocess
from ipywidgets.embed import embed_minimal_html

with open("location.json", "r") as f:
    data = json.load(f)

gmaps.configure(api_key = "")

police_location = []
police_rows = []
locations = []
rows = []
for row in data:
    item = row["name"]
    country = row["country"]
    if(item == country or item.startswith("No panel physician")):
        continue
    lat = row["coordinates"][1]
    lon = row["coordinates"][0]
    loc = (lat, lon)
    if item.startswith("Police"):
        police_location.append(loc)
        police_rows.append(row)
    else:
        locations.append(loc)
        rows.append(row)


figure_layout = {
    'height': '900px'
}

info_box_template = """
<dl>
    <dt>Name</dt><dd>{name}</dd>
    <dt>Website</dt><dd>{website}</dd>
</dl>
"""


health_check_text = [item["name"] for item in rows]
health_check_content = [info_box_template.format(**item) for item in rows]
health_check_layer = gmaps.marker_layer(locations, hover_text= health_check_text, info_box_content= health_check_content)

police_text = [item["name"] for item in police_rows]
police_content = [info_box_template.format(**item) for item in police_rows]
police_layer = gmaps.symbol_layer(police_location, fill_color="#006699", stroke_color="#006699", hover_text=police_text, info_box_content= police_content )


fig = gmaps.figure(layout=figure_layout)
fig.add_layer(health_check_layer)
fig.add_layer(police_layer)
embed_minimal_html('map.html', views=[fig])