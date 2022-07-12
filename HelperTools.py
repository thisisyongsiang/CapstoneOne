from http.client import SWITCHING_PROTOCOLS
import json

def ConvertTSVtoJson(tsvFilePath,jsonFilePath):
    """
    Converts TSV file to JSON
    """
    jsonObjs=[]
    with open(tsvFilePath,mode='r',encoding='utf-8') as f:
        line=f.readline()
        titles=[l.strip() for l in line.split('\t')]
        # print(titles)
        for ln in f.readlines():

            fields=[l.strip()for l in ln.split('\t')]
            # print(fields)
            toInclude=True
            obj={}
            for i in range(len(titles)):
                # if titles[i]=='rating':
                #     #filter for businesses with ratings available
                #     if fields[i]=='':
                #         toInclude=False
                #         break
                if fields[i]=='':continue

                if titles[i]=='fsq_category_ids':
                    #filter for only food category
                    cats = fields[i].strip('[]').split(',')
                    isFnB=False
                    for c in cats:
                        if int(c)>=13000 and int(c)<14000:
                            isFnB=True
                            break        
                    if not isFnB:
                        toInclude=False
                        break
                val=fields[i]
                if  titles[i]=='price':
                    if val=='Cheap':val=1
                    elif val=='Moderate':val=2
                    elif val=='Expensive':val=3
                    elif val=='Very Expensive':val=4
                elif titles[i]=='name':
                    val=fields[i]
                elif val[0]=='{':
                    val=(json.loads(val))
                elif fields[i][0]=='[':
                    val=(json.loads(val))
                obj[titles[i]]=val
            if toInclude:
                jsonObjs.append(obj)
        print(len(jsonObjs))
    with open(jsonFilePath,mode='w',encoding='utf-8') as f:
        json.dump(jsonObjs, f, ensure_ascii=False, indent=4)
ConvertTSVtoJson('singapore.tsv','singaporeFnBAll.json')