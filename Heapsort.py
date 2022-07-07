import sys

class Heap:

    def __init__(self, arr):
        self.maxsize = sys.maxsize
        self.size = len(arr)
        self.Heap = arr
        self.FRONT = 0

    
    def parent(self, pos):
        return (pos-1)//2 if pos != 0 else 0
    
    def leftChild(self, pos):
        return (2*pos)+1

    def rightChild(self, pos):
        return (2*pos)+2
    
    def isLeaf(self, pos):
        return (2*pos)+1 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    
    def bubbleDown(self, pos, comparer):

        child = self.leftChild(pos)
        done = False

        while child < self.size and not done:
            rightC = self.rightChild(pos)
            if rightC < self.size and comparer(self.Heap[child], self.Heap[rightC]):
                child = rightC

            if comparer(self.Heap[pos], self.Heap[child]):
                self.swap(pos, child)
            else:
                done = True
            
            pos = child
            child = self.leftChild(pos)

    
    def insert(self, item, comparer):
        if self.size >= self.maxsize:
            return
        self.Heap[self.size] = item
        curr = self.size

        self.size += 1

        while comparer(self.Heap[self.parent(curr)],self.Heap[curr]):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
    
    def generateHeap(self, comparer):

        for pos in range(self.parent(self.size-1), -1, -1):
            self.bubbleDown(pos, comparer)
    
    def remove(self, comparer):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT]= self.Heap[self.size-1]
        self.size -= 1
        self.bubbleDown(self.FRONT, comparer)
        return popped

    def Print(self):
        for i in range(0, self.parent(self.size-1), 1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))



def getFirstN(arr, field, topN, isAscending=True):

    """
    Takes in list of dictionaries, field for sorting and boolean value for ascending/descending order of sort and returns top N items in a list of dictionaries
    """

    topN = min(topN, len(arr))
    sortedList = []
    newHeap = Heap(arr)
    
    if isAscending == True:
        newHeap.generateHeap(lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance']))
        print(newHeap[0])
        for j in range(topN):
            sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance'])))
    else:
        newHeap.generateHeap(lambda a,b: a[field]+(1/a['distance'])<b[field]+(1/b['distance']))
        print(newHeap[0])
        for j in range(topN):
            sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])<b[field]+(1/b['distance'])))

    # if isAscending == True:
    #     newHeap = Heap(len(arr))
    #     for i in range(len(arr)):
    #         newHeap.insert(arr[i],lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance']))
    #     for j in range(topN):
    #         sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])>b[field]+(1/b['distance'])))
        
    # else:
    #     newHeap = Heap(len(arr))
    #     for i in range(len(arr)):
    #         newHeap.insert(arr[i], lambda a,b: a[field]+(1/a['distance'])<b[field]+(1/b['distance']))
    #     for j in range(topN):
    #         sortedList.append(newHeap.remove(lambda a,b: a[field]+(1/a['distance'])<b[field]+(1/b['distance'])))
        
    return sortedList

yelp_data = [
    {
        "id": "mF15iVbRW2lclgq72ImU3g",
        "alias": "ikura-japanese-singapore-2",
        "name": "Ikura Japanese",
        "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/JqZ9BLqaBVRVftSx1rkMCA/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/ikura-japanese-singapore-2?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "japanese",
                "title": "Japanese"
            }
        ],
        "rating": 4.0,
        "coordinates": {
            "latitude": 1.354883374106,
            "longitude": 103.831147204462
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#01-43",
            "address3": "",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#01-43",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6562532792",
        "display_phone": "+65 6253 2792",
        "distance": 266.4921670007933
    },
    {
        "id": "9iFzziJA_2MfsY3-OqzrfQ",
        "alias": "omoté-singapore",
        "name": "Omoté",
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/e2184YHr4SckCnvmdDhTrA/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/omot%C3%A9-singapore?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 3,
        "categories": [
            {
                "alias": "japanese",
                "title": "Japanese"
            },
            {
                "alias": "sushi",
                "title": "Sushi Bars"
            }
        ],
        "rating": 4.5,
        "coordinates": {
            "latitude": 1.354783,
            "longitude": 103.831162
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#03-24A",
            "address3": "null",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#03-24A",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6594501020",
        "display_phone": "+65 9450 1020",
        "distance": 272.6582616649959
    },
    {
        "id": "v6G1wagOHOjFuFR1PpDFSA",
        "alias": "elemen-singapore-2",
        "name": "Elemen",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/cPwq18bIH_MkySFybptMdw/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/elemen-singapore-2?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 3,
        "categories": [
            {
                "alias": "vegetarian",
                "title": "Vegetarian"
            },
            {
                "alias": "chinese",
                "title": "Chinese"
            }
        ],
        "rating": 3.5,
        "coordinates": {
            "latitude": 1.35469,
            "longitude": 103.83098
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#01-113 Thomson Plaza",
            "address3": "",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#01-113 Thomson Plaza",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6564520351",
        "display_phone": "+65 6452 0351",
        "distance": 290.43584879272186
    },
    {
        "id": "obnTklPESFUeaORlw1h55w",
        "alias": "sushi-tei-singapore-18",
        "name": "Sushi Tei",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/LW-j-0oLIPaEvCv34K9FuA/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/sushi-tei-singapore-18?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "japanese",
                "title": "Japanese"
            },
            {
                "alias": "sushi",
                "title": "Sushi Bars"
            }
        ],
        "rating": 1.0,
        "coordinates": {
            "latitude": 1.34182,
            "longitude": 103.8358307
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Road",
            "address2": "# 03-46,Thomson Plaza",
            "address3": "",
            "city": "Singapore",
            "zip_code": "",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Road",
                "# 03-46,Thomson Plaza",
                "Singapore",
                "Singapore"
            ]
        },
        "phone": "+6564576678",
        "display_phone": "+65 6457 6678",
        "distance": 290.43584879272186
    },
    {
        "id": "e1vJ26tcaDyriMbCm3ihvw",
        "alias": "starbucks-singapore-49",
        "name": "Starbucks",
        "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/KKtWm9kA_1fScSEQNxpf2Q/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/starbucks-singapore-49?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 2,
        "categories": [
            {
                "alias": "coffee",
                "title": "Coffee & Tea"
            }
        ],
        "rating": 5.0,
        "coordinates": {
            "latitude": 1.35502323027523,
            "longitude": 103.830770216882
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#01-37A",
            "address3": "",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#01-37A",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6569101149",
        "display_phone": "+65 6910 1149",
        "distance": 290.8881004294777
    },
    {
        "id": "PXZnnKdshvGEqFI0zYU01A",
        "alias": "peach-garden-singapore-9",
        "name": "Peach Garden",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/-rYtmPFw5hU0oY3uA7UuGA/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/peach-garden-singapore-9?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 6,
        "categories": [
            {
                "alias": "chinese",
                "title": "Chinese"
            }
        ],
        "rating": 3.5,
        "coordinates": {
            "latitude": 1.3548791,
            "longitude": 103.8308643
        },
        "transactions": [],
        "price": "$$",
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#01-88",
            "address3": "null",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#01-88",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6564513233",
        "display_phone": "+65 6451 3233",
        "distance": 291.40463580383386
    },
    {
        "id": "UVc9ACOrOangaSzzXxWoaQ",
        "alias": "grumpy-bear-singapore",
        "name": "Grumpy Bear",
        "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/5ni0H0Wz1YX6DjYIiuq4_g/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/grumpy-bear-singapore?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 3,
        "categories": [
            {
                "alias": "tradamerican",
                "title": "American (Traditional)"
            }
        ],
        "rating": 3.5,
        "coordinates": {
            "latitude": 1.35504490870714,
            "longitude": 103.830736573066
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#02-10",
            "address3": "null",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#02-10",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6582996261",
        "display_phone": "+65 8299 6261",
        "distance": 292.7546787775351
    },
    {
        "id": "boeEHinAcS5C_YAVNS2dHw",
        "alias": "the-good-trio-singapore",
        "name": "The Good Trio",
        "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/oQLYzAzxhrTzmBdbhOQ0cg/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/the-good-trio-singapore?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "chinese",
                "title": "Chinese"
            }
        ],
        "rating": 4.0,
        "coordinates": {
            "latitude": 1.3547439164137,
            "longitude": 103.830800284722
        },
        "transactions": [],
        "price": "$$",
        "location": {
            "address1": "6F Marigold Drive",
            "address2": "",
            "address3": "",
            "city": "Singapore",
            "zip_code": "576402",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "6F Marigold Drive",
                "Singapore 576402",
                "Singapore"
            ]
        },
        "phone": "",
        "display_phone": "",
        "distance": 306.1742232479605
    },
    {
        "id": "Ivv8q67iI1wUEnaHcu0X4A",
        "alias": "ritz-apple-strudel-and-pastry-singapore-4",
        "name": "Ritz Apple Strudel & Pastry",
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/-st21TQ453zHlNT7Dj73kg/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/ritz-apple-strudel-and-pastry-singapore-4?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "bakeries",
                "title": "Bakeries"
            },
            {
                "alias": "coffee",
                "title": "Coffee & Tea"
            }
        ],
        "rating": 4.0,
        "coordinates": {
            "latitude": 1.34182,
            "longitude": 103.8358307
        },
        "transactions": [],
        "location": {
            "address1": "267 Upper Thomson Rd",
            "address2": "null",
            "address3": "null",
            "city": "Singapore",
            "zip_code": "574394",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "267 Upper Thomson Rd",
                "Singapore 574394",
                "Singapore"
            ]
        },
        "phone": "+6564586935",
        "display_phone": "+65 6458 6935",
        "distance": 311.84985357638044
    },
    {
        "id": "6Zw3k6UkJcBuOlZq3UtcRQ",
        "alias": "the-roti-prata-house-singapore-2",
        "name": "The Roti Prata House",
        "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/1iI99CZZQW4pQx5fr-AKyg/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/the-roti-prata-house-singapore-2?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 31,
        "categories": [
            {
                "alias": "indpak",
                "title": "Indian"
            }
        ],
        "rating": 3.5,
        "coordinates": {
            "latitude": 1.35377165898043,
            "longitude": 103.834249377251
        },
        "transactions": [],
        "price": "$",
        "location": {
            "address1": "246M Upper Thomson Road",
            "address2": "",
            "address3": "",
            "city": "Singapore",
            "zip_code": "574422",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "246M Upper Thomson Road",
                "Singapore 574422",
                "Singapore"
            ]
        },
        "phone": "+6564595260",
        "display_phone": "+65 6459 5260",
        "distance": 329.0301866841851
    },
    {
        "id": "bwXQkJY2t21x9OKZU0PPBw",
        "alias": "dino-cake-house-and-cafe-singapore",
        "name": "Dino Cake House & Cafe",
        "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/rSzxq-vZX2O3pstDF59UTw/o.jpg",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/dino-cake-house-and-cafe-singapore?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "bakeries",
                "title": "Bakeries"
            }
        ],
        "rating": 4.0,
        "coordinates": {
            "latitude": 1.34182,
            "longitude": 103.8358307
        },
        "transactions": [],
        "price": "$",
        "location": {
            "address1": "257 Upper Thomson Rd",
            "address2": "null",
            "address3": "null",
            "city": "Singapore",
            "zip_code": "574384",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "257 Upper Thomson Rd",
                "Singapore 574384",
                "Singapore"
            ]
        },
        "phone": "+6565525088",
        "display_phone": "+65 6552 5088",
        "distance": 329.36879912981175
    },
    {
        "id": "zCqmRH-jVBT_KUfcB9vdkA",
        "alias": "paradise-inn-singapore-14",
        "name": "Paradise Inn",
        "image_url": "",
        "is_closed": False,
        "url": "https://www.yelp.com/biz/paradise-inn-singapore-14?adjust_creative=I9XO1lu26wC-yRCjIHYyRg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=I9XO1lu26wC-yRCjIHYyRg",
        "review_count": 1,
        "categories": [
            {
                "alias": "chinese",
                "title": "Chinese"
            }
        ],
        "rating": 4.0,
        "coordinates": {
            "latitude": 1.35457386852026,
            "longitude": 103.830634823982
        },
        "transactions": [],
        "location": {
            "address1": "301 Upper Thomson Rd",
            "address2": "#01-110, Thomson Plaza Fairprice Town",
            "address3": "",
            "city": "Singapore",
            "zip_code": "574408",
            "country": "SG",
            "state": "SG",
            "display_address": [
                "301 Upper Thomson Rd",
                "#01-110, Thomson Plaza Fairprice Town",
                "Singapore 574408",
                "Singapore"
            ]
        },
        "phone": "+6564556977",
        "display_phone": "+65 6455 6977",
        "distance": 332.33003907750265
    }]

print('TOP 3 ITEMS ARE')

output = getFirstN(yelp_data[0:9], 'rating', 5 , False)
# print(output)

for i in range(len(output)):
    print(output[i]['name'], output[i]['rating'])

