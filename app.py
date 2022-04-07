import email
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email #we importes send email fuction from the class
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234Abcd@localhost/height_collector'  # SPESCEFING THE ADDRESS OF THE DATABASE in the computer
db=SQLAlchemy(app) 

class Data(db.Model): # we created a class  (the class inherests db.model) << this class is caaled automaticlly by the sequence of lines, you dont have to call it (not sure)
    
    #1- we created th table and columns
     
    #this class creates a table in the DB
    tablename_="data"
    id=db.Column(db. Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)
    
    
    #2- we fill the columns with values from the constructer

    # i did not understand why we made this constructer
    def __init__(self,email_,height_):
        self.email_=email_
        self.height_ =height_

        
    #now in cmd we we import the db(from app import db) and then we create the table( db.create_all()) <<< this way this class will be called

#render index.html from templates folder in the home page
@app.route("/")
def index():
    return render_template("index.html")











@app.route("/success",methods = ['POST'])
def success():
    if request.method=='POST': # if the user came to this page by vompleteing the for, not by typing the url manually
        email= request.form['email_name']
        height= request.form['height_name']
        
        
        if db.session.query(Data).filter(Data.email_==email).count() == 0:# if the email dose not exist before  
            data= Data(email_ = email,height_= height)#
            db.session.add (data)#
            db.session.commit()#
            
            average_height =db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height)
            
            count=db.session.query(Data.height_).count() #no. of heights

            send_email(email,height,average_height,count)
            
            return render_template("success.html")
    return render_template('index.html', text= "email already existed")















# if the scrpt is excuted not imported(a devaloper is running the code, not a regular user using the app):
if __name__ == '__main__':
    app.debug= True #show errors and spescefications of the errors
    app.run()
    