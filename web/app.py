from flask import Flask,request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.Books
authors = db["Authors"]

class Show(Resource):
    def get(self):
        retJson=[]
        for author in authors.find():
            retJson.append({
                "id":author['Id'],
                "authorname":author['Authorname'],
                "birthyear":author["Birthyear"],
                "books":author['Books']
            })
        return retJson

def generReturnJson(status, msg):
    retJson = {
        "status": status,
        "msg":msg
    }
    return retJson

class Register(Resource):
    def post(self):
        postedData = request.get_json()

        id = postedData["id"]
        authorname = postedData["authorname"]
        birthyear = postedData["birthyear"]
        books = postedData["books"]

        authors.insert({
            "Id":id,
            "Authorname":authorname,
            "Birthyear":birthyear,
            "Books":books
        })

        return generReturnJson(200, "An author save successfully!")

class ShowOneAuthor(Resource):
    def get(self, id):
        author = authors.find_one({'Id':id})
        retJson = {
            'id':author['Id'],
            "authorname":author["Authorname"],
            "birthyear":author["Birthyear"],
            "books":author['Books']
        }
        return retJson

class ShowBook(Resource):
    def get(self, id):
        author = authors.find_one({'Id':id})
        books = author["Books"]
        # retJson = {
        #     "bookid":books["bid"],
        #     "bookname":books["bookname"]
        # }
        return books

class ShowOneBook(Resource):
    def get(self,id,bid):
        author = authors.find_one({'Id':id})
        books = author["Books"]
        book = books[bid]
        return book

class Detect(Resource):
    def post(self):
        postedData = request.get_json()

        text1 = postedData["text1"]
        text2 = postedData["text2"]

        import spacy
        nlp = spacy.load('en_core_web_sm')
        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        retJson = {
            'status':200,
            'ratio':ratio,
            'msg':"Similarity score calculated successfully!"
        }

        return retJson



api.add_resource(Show,'/show')
api.add_resource(Register,'/register')
api.add_resource(ShowOneAuthor,'/show/<int:id>',endpoint='author_by_id')
api.add_resource(ShowBook,'/show/<int:id>/books',endpoint ='books_by_id')
api.add_resource(ShowOneBook, '/show/<int:id>/books/<int:bid>', endpoint ='book_by_id')
api.add_resource(Detect,'/detect')

if __name__=="__main__":
    app.run(host='0.0.0.0')
