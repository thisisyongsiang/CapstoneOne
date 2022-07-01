import json

dir="yelpAPIData.json"
f=open(dir,encoding='utf-8')
data=json.load(f)
f.close()

f=open("yelpAPIDataNew.json",encoding='utf-8')
data+=json.load(f)
f.close()

f=open("yelpAPIDataNewSouth.json",encoding='utf-8')
data+=json.load(f)
f.close()

ids=set()
uniqueData=[]
for d in data:
    if not d['id'] in ids:
        ids.add(d['id'])
        uniqueData.append(d)

with open("yelpAPIDataMerged.json",mode='w',encoding='utf-8') as f:
    json.dump(uniqueData, f, ensure_ascii=False, indent=4)