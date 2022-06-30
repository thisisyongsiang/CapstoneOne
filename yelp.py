import requests
import json
import GetDistance

key="jbVyRyrgR8rFfBUlTBHzdapsZoi1RMIxkWpKbhzSDrxdHQlckHn2qm3UYafILzK75SATVm2nGv6ypJzdwfOKy2TaZ5nRP4RfsQkf41yR-V9QOPoGopzK8feCtEGxYnYx"
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

overallObj=[]
ids=set()

for i in range(3):
    lat,long=GetDistance.GetCoordinatesFromStart([lat,long],3000,180)
    params["latitude"]=lat
    params["longitude"]=long
    params['offset']=0
    total=0
    dataCount=0

    while dataCount<1000 and dataCount<=total:
        res=requests.get(url+extension,params=params,headers=header)
        jsonObj=json.loads(res.text)
        for item in jsonObj['businesses']:
            if not item['id'] in ids:
                overallObj.append(item)
                ids.add(item['id'])
        if total==0:
            total=jsonObj['total']
        print(jsonObj['total'])
        print(dataCount)
        params["offset"]+=len(jsonObj['businesses'])
        dataCount+=len(jsonObj['businesses'])
print(len(overallObj))
with open("yelpAPIDataNewSouth.json",mode='w',encoding='utf-8') as f:
    json.dump(overallObj, f, ensure_ascii=False, indent=4)