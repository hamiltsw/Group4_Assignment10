from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    '''
    Returns the distance between two geographic coordinate points
    @param lat1: first point's latitude
    @param lon1: first point's longitude
    @param lat2: second point's latitude
    @param lon2: second point's longitude
    @return: distance between two points in miles
    '''
    r = 6371 # km
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 2 * r * asin(sqrt(a)) * 0.621371
