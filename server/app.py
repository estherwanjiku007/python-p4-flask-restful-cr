#!/usr/bin/env python3
from flask_migrate import Migrate
from flask import Flask,request,make_response
from flask_restful import Api,Resource
from models import db, Newsletter
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate=Migrate(app,db)
db.init_app(app)
api=Api(app)
# class NewsLetter(Resource):
#     def get(self):
#         return {"newsletter": "it's a beautiful 108 out in Austin today"}

class Home(Resource):
    def get(self):
        res_dict={
           "message": "Welcome to the Newsletter RESTful API", 
        }
        
        return make_response(res_dict,200)

class NewsLetters(Resource):
    def get(self):
        res_dict_list=[l.to_dict() for l in Newsletter.query.all()]
        return make_response(res_dict_list,200)
    
    def post(self):
        new_record=Newsletter(
            title=request.form["title"],
            body=request.form["body"],
        )
        return make_response(new_record.to_dict(),201)

class NewsletterById(Resource):
    def get(self,id):
        newsletter=Newsletter.query.filter(Newsletter.id==id).first().to_dict()
        return make_response(newsletter,200)
    
api.add_resource(Home,"/")
api.add_resource(Newsletter,"/newsletter")
api.add_resource(NewsLetters,"newsletters")
api.add_resource(NewsletterById,"/newsletters/<int:id>")
if __name__=="__main__":
    app.run(port=5555)

