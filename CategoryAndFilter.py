from codecs import getdecoder
import json
import GetDistance
from re import T
from typing import Dict, List
import ProbabilityRatingModel as prm

def getCategories(data:List[str],origin:List[float]=None ):
    """
    Returns dictionary with key as food category in lowercase
    and value as a list of objects belonging to category
    eg.
    {
        'japanese':[{obj1},{obj2}...]
        'american'
    }
    """

    cat={}
    for d in data:
        # if d['is_closed']:            ### Can remove? 
        #     continue
        # if 'price' in d:
        #     if type(d['price'])==str:
        #         d["price"]=len(d['price'])
        # if origin:
        #     d['distance']=GetDistance.GetDistanceFromCoordinates(origin,[d['coordinates']['latitude'],d['coordinates']['longitude']])
        dCat = d['categories']
        for c in dCat:
            food=c["title"].lower()
            
            if not food in cat:
                cat[food]=[d]
            else:
                cat[food].append(d)
    return cat

def simplifyData(data:List[str],origin:List[float]=None ):
    """
    Makes the data leaner
    Adds an additional recommendation_value
    and calculated distance field
    only includes fields:
    id
    categories
    coordinates
    rating
    name
    review_count
    price
    """ 
    output=[]
    for d in data:
        obj={}
        obj['id']=d['id']
        obj['name']=d['name']
        obj['categories']=d['categories']
        cat = []
        for c in d['categories']:
            cat.append(c["title"].lower())
        obj['category'] = cat
        obj['coordinates']=d['coordinates']
        obj['location'] = d['location']
        if 'price' in d:
            obj['price'] = len(d['price'])
            obj['display_price']= len(d['price']) * "$"
        else:
            obj["price"] = 0
            obj['display_price']= "NA"
        obj['rating']=d['rating']
        obj['review_count']=d['review_count']
        obj['recommendation']=prm.exponential(obj['review_count'],obj['rating'])
        if origin:
            if (d['coordinates']['latitude'] and d['coordinates']['longitude']):
                obj['distance']=GetDistance.GetDistanceFromCoordinates(origin,[float(d['coordinates']['latitude']),float(d['coordinates']['longitude'])]) # Cast to Float
            else:
                continue
        else:
            obj['distance']=d['distance']
        if d['is_closed']:
            obj['is_closed']=d['is_closed']
        else:
            obj['is_closed']=False
        output.append(obj)
    return output


def filterDataByFieldAndValue(data:List[Dict],field:str,value):
    """
    filters data by field value
    """
    value=str(value).lower()
    field=field.lower()
    output=[]
    for d in data:
        if d['is_closed']:
            continue
        if not field in d:
            continue
        if str(d[field]).lower()==value:
            output.append(d)
    return output

def filterDataByFieldAndValueRange(data:List[Dict],field:str,valueRange):
    """
    filters data by field and value range
    valueRange to be in a List of 2 values, 
    First item being the start of the Range,
    Second value being the End of the range
    """
    field=field.lower()
    output=[]
    for d in data:
        if d['is_closed']:
            continue
        if not field in d:
            continue
        if d[field]>=valueRange[0] and d[field]<=valueRange[1]:
            output.append(d)
    return output    

def getMultipleFoodCategories(data:List[Dict],categories:List[str]):
    """
    Get entries which are part of a desired list of categories
    """
    cats=set(categories)
    output=[]
    for d in data:
        chosen=False
        for c in d['categories']:
            if c['title'].lower() in cats:
                chosen=True
        if chosen:
            output.append(d)
    return output

def filterVisited(data:List[Dict], visited:List[str]):
    cats=set(visited)
    output=[]
    for d in data:
        if d['name'] not in cats:
            output.append(d)
    return output

def filterDataByFieldsAndValueRanges(data:List[Dict],fields:List[str],valueRanges):
    """
    filters data by field and value range
    valueRange to be in a List of 2 values, 
    First item being the start of the Range,
    Second value being the End of the range
    """
    output=[]
    for d in data:
        if d['is_closed']:
            continue

        toInclude=True
        for i,field in enumerate(fields):
            if not field in d:
                toInclude=False
                break
            field=field.lower()
            if d[field]<valueRanges[i][0] or d[field]>valueRanges[i][1]:
                toInclude=False
        if toInclude:
            output.append(d)
    return output 

def showExample():
    dir="yelpAPIDataNew.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    print(len(data))
    cat=getCategories(data)
    print(cat.keys())
    caf=cat['cafes']
    #print(filterDataByFieldAndValue(caf,"price","$"))
    foods = getMultipleFoodCategories(data,categories=['pizza','italian'])
    #[print(f['name'],f['categories']) for f in foods]
    filtered=filterDataByFieldsAndValueRanges(data,['rating','price'],[[3.0,5.0],[2,3]])
    #[print (f['name'],'price :',f['price'],'rating :',f['rating']) for f in filtered]
    #[print(c['name'],c['price']) for c in filterDataByFieldAndValueRange(caf,"price",[1,3])]
    #[print(c['name'],c['distance']) for c in filterDataByFieldAndValueRange(caf,"distance",[0,2000])]
#showExample()
