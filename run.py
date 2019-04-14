import os
import json
from flask import Flask, render_template, request, flash 

#We're then creating an instance of this and storing it in a variable called app 
#The first argument of the Flask class is the name of the applications module - our package. 
# Since we're just using a single module, we can use __name__ which is a built-in Python variable

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    

#advanced routing    
@app.route('/about/<member_name>') #here is for when we click on the names, there be a route that will show the name
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member) #Why member=member????
    # return only the member name : "<h1>" + member["name"] +"</h1>" 
    



@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
        # flash has a function called get_flashed_messages()
        
    return render_template("contact.html", page_title="Contact")

@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)