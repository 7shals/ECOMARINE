from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return R * c

ais_found = False

for index, row in ais_data.iterrows():
    distance = haversine(detected_lat, detected_lon, row["lat"], row["lon"])
    
    if distance < 1:  # within 1 km
        ais_found = True
        print("AIS ON - Matched MMSI:", row["mmsi"])
        break

if not ais_found:
    print("Potential Dark Vessel - AIS OFF")
5
