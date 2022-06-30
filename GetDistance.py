from typing import List
import math

def GetDistanceFromCoordinates(origin:List[float],target:List[float]):
    """
    uses the haversine formula to get the
    distance between two lat long coordinates
    in decimal degrees
    """
    #earth radius
    r= 6371000     
    lat1=math.radians(origin[0])
    lat2=math.radians(target[0])
    lon1=math.radians(origin[1])
    lon2=math.radians(target[1])
    a=math.sin((lat2-lat1)/2)
    b=math.cos(lat1)*math.cos(lat2)
    c=math.sin((lon2-lon1)/2)
    return 2*r*math.asin(math.sqrt(a*a+b*c*c))
print(GetDistanceFromCoordinates([1.35644,103.83297],[1.35377165898043,103.834249377251]))

