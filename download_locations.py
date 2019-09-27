import requests
import json
countries = [
"Afghanistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba",
"Australia","Austria","Azerbaijan","Bahamas, The","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cabo Verde",
"Cambodia","Cameroon","Canada","Cayman Islands","Central African Republic","Chad","Chile","China (excludes SARs and Taiwan Province)",
"Christmas Island","Cocos (Keeling) Island","Colombia","Comoros","Congo, Democratic Republic of the","Congo, Republic of the","Cook Islands",
"Costa Rica","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Faeroe Islands (Denmark)","Falkland Islands","Fiji","Finland",
"France","French Guiana","French Polynesia","Gabon","Gambia, The","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada",
"Guadeloupe","Guam","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Holy See, The","Honduras","Hong Kong (SAR of China)","Hungary",
"Iceland","India","Indonesia","Iran","Iraq","Ireland, Republic of (Eire)","Israel","Italy","Ivory Coast (Cote D’Ivoire)","Jamaica","Japan",
"Jordan","Kazakhstan","Kenya","Kiribati","Korea, Democratic People's Republic of (North Korea)","Kosovo","Kuwait","Kyrgyzstan",
"Laos, The Lao People’s Democratic Republic","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg",
"Macau (SAR of China)","Madagascar, Republic of","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands, Republic of","Martinique",
"Mauritania","Mauritius","Mexico","Micronesia, Federated States of","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco",
"Mozambique","Myanmar","Namibia","Nauru, Republic of","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria",
"Niue","Northern Mariana Islands","Norway","Oman","Pakistan","Palau","Palestinian Territories","Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Pitcairn Islands","Poland","Portugal","Puerto Rico","Qatar","Republic of Korea (South Korea)","Republic of North Macedonia",
"Reunion","Romania","Russian Federation","Rwanda","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles",
"Sierra Leone","Singapore","Slovak Republic","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","St Helena",
"St Kitts and Nevis","St Lucia","St Pierre and Miquelon","St Vincent and the Grenadines","Sudan","Suriname","Sweden","Switzerland","Syria",
"Tahiti","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan",
"Turks and Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay",
"Uzbekistan","Vanuatu","Venezuela","Vietnam","Virgin Islands, British","Virgin Islands, United States","Wallis and Futuna","Yemen",
"Zambia","Zimbabwe"]


request_url = "https://immi.homeaffairs.gov.au/_layouts/15/api/Data.aspx/GetLocationsByCountry"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
"Accept": "application/json;odata=verbose",
"Content-Type": "application/json;odata=verbose",
}
with open("location.json", "r") as f:
    extracted = json.load(f)

for country in countries:
    print(country)
    r = requests.post(request_url, json={"country":country}, headers=headers)

    if(not r):
        raise "error requesting!"
    content =  json.loads(r.content)["d"]["data"]


    for collection in content:
        if(not "features" in collection):
            continue
        for feature in collection["features"]:
            location = {
                "coordinates": feature["geometry"]["coordinates"],
                "country": feature["properties"]["country"],
                "name": feature["properties"]["name"],
                "website":feature["properties"]["website"],
            }
            extracted.append(location)

    with open("location.json", "w") as f:
        json.dump(extracted, f)

