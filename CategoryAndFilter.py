import json
from re import T
from typing import Dict, List

def getCategories(data:List[str]):
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
        if d['is_closed']:
            continue

        dCat = d['categories']
        for c in dCat:
            food=c["title"].lower()
            
            if not food in cat:
                cat[food]=[d]
            else:
                cat[food].append(d)
    return cat


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
        if type(d[field]) is str and type(valueRange[0]) is str:
            if len(d[field])>=len(valueRange[0]) and len(d[field])<=len(valueRange[1]):
                output.append(d)
            continue
        if d[field]>=valueRange[0] and d[field]<=valueRange[1]:
            output.append(d)
    return output    


def showExample():
    dir="yelpAPIData.json"
    f=open(dir,encoding='utf-8')
    data=json.load(f)
    cat=getCategories(data)
    # print(cat)
    caf= cat['cafes']
    #print(caf)
    #print(filterDataByFieldAndValue(caf,"price","$"))
    [print(c['name'],c['price']) for c in filterDataByFieldAndValueRange(caf,"price",['$','$$$'])]
    [print(c['name'],c['distance']) for c in filterDataByFieldAndValueRange(caf,"distance",[0,2000])]