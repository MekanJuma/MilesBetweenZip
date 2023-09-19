import pandas as pd
from uszipcode import SearchEngine
from geopy.distance import geodesic
import googlemaps

GOOGLE_MAPS_API_KEY = ''
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_zip_details(zip_code):
    search = SearchEngine()
    result = search.by_zipcode(zip_code)
    if result and result.city:
        return {
            "city": result.city,
            "state": result.state,
            "latitude": result.lat,
            "longitude": result.lng
        }
    return None

def get_driving_distance(origin_zip, destination_zip):
    origin = f"{origin_zip}, USA"
    destination = f"{destination_zip}, USA"

    directions = gmaps.directions(origin, destination, mode="driving")

    if directions and 'legs' in directions[0]:
        return directions[0]['legs'][0]['distance']['value'] / 1609.34  # Convert meters to miles
    return None

df = pd.read_excel("data.xlsx")

for index, row in df.iterrows():
    origin = str(row['Origin Zip']).replace(",", "")
    dest = str(row['Destination Zip']).replace(",", "")
    
    # Distance
    distance = get_driving_distance(origin, dest)
    if distance is not None:
        df.at[index, 'TOTAL MILES'] = distance
    
    # Origin Address
    origin_details = get_zip_details(origin)
    if origin_details:
        df.at[index, 'OriginAddress'] = f"{origin_details['city']}, {origin_details['state']}"
    
    # Destination Address
    destination_details = get_zip_details(dest)
    if destination_details:
        df.at[index, 'DestinationAddress'] = f"{destination_details['city']}, {destination_details['state']}"

df.to_excel("modified_file.xlsx", index=False)