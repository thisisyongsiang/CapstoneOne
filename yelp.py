import requests
import json

key="your-api-key"
lat,long=1.35644,103.83297
url='https://api.yelp.com/v3'
extension='/businesses/search'
header={
    "Authorization": "Bearer "+key
}
params={
    "term":"food",
    "latitude":lat,
    "longitude":long,
    "radius":10000,
    "limit":50,
    "sort_by":"distance",
    "offset":0
}
total=9999
dataCount=0
overallObj=[]
while dataCount<1000 and dataCount<total:
    res=requests.get(url+extension,params=params,headers=header)
    jsonObj=json.loads(res.text)
    overallObj+=(jsonObj['businesses'])
    if total==9999:
        total=jsonObj['total']
    print(jsonObj['total'])
    print(dataCount)
    params["offset"]+=len(jsonObj['businesses'])
    dataCount+=len(jsonObj['businesses'])
print(total)
with open("yelpAPIData2.json",mode='w',encoding='utf-8') as f:
    json.dump(overallObj, f, ensure_ascii=False, indent=4)
print(jsonObj['total'])