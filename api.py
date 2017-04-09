import os
import sys
from pymongo import MongoClient
from clarifai.client import ClarifaiApi

client = MongoClient()
db = client.ThinkingGame

def add(filename):
    tagHolder=[]
    i=0
    #ClarifaiApi stuff
    pathC = os.path.join("images_raw/",filename)
    pathM = os.path.join("images/",filename)
    clarifai_api = ClarifaiApi("5ufSEyCVOzwUzNX5nDWPFXaTHbOTkbS3NzAGyrNa",
        "JbqnMT_wofMV1IS-QZ0jIsYo-60tdHkQOFfqGxM7")
    result = clarifai_api.tag_images(open(pathC, 'rb'))
    for tag in result['results'][0]['result']['tag']['classes']:
        tag = tag.encode('ascii', 'ignore')
        tagHolder.append(tag)
    #MongoDB stuff
    ##Adding stuff
    print pathM
    print tagHolder[:5]
    result = db.photos.insert_one(
        {
            "path":pathM,
            "tags":tagHolder[:5]
        }
    )

def getAllPaths():
    paths = []
    cursor = db.photos.find({})
    for document in cursor:
        print(document["path"])
        paths.append(document["path"])
    return paths

def getAllTags(path):
    cursor = db.photos.find({"path":path})
    return cursor[0]['tags']

if __name__ == "__main__":
    '''
    #for adding to the db
    for file in os.listdir('images_raw'):
        print(file)
        add(file)
    '''
    #print(getAllTags("images/0.jpg"))
