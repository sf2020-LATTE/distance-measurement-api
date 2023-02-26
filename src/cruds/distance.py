import math

from app import config

def calculate_distance(start_longitude, start_latitude, end_longitude, end_latitude):

    # ラジアンに変換
    lat1 = math.radians(start_latitude)
    lat2 = math.radians(end_latitude)
    lon1 = math.radians(start_longitude)
    lon2 = math.radians(end_longitude)

    # ハーベイの公式
    distance = config.EARTH_RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

    return distance