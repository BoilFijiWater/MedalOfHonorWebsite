from flask import Flask, url_for, render_template, request, Markup, flash, Markup
import os
import json

app = Flask(__name__)

with open('medal_of_honor.json') as usmilitary_data:
        military = json.load(usmilitary_data)
        
def toOption(s):
    return "<option value=" + s + " >" + s + "</option>"
    
def show_place_fought():
    LocationFaught = []
    print(type(LocationFaught))
    for p in position:
        if p["location name"] not in LocationFaught:
            LocationFaught.append(p["location name"])
    print(LocationFaught)
    return LocationFaught

@app.route("/")
def render_creed():
    str = ""
    for po in get_location_opions():
        str += toOption(po)
    

    
    print(str)
    return render_template('GMYM.html', strr = Markup(str))

def Loc(state):
    SP = 0
    for pop in counties:
        if pop["State"] == state:
            Sp = Sp + pop["Population"]["2014 Population"]
    return "Population:" + " " + str(Sp)    
    

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('index.html')

@app.route("/GMYM")
def render_page1():
    return render_template('GMYM.html')

@app.route("/CocoB")
def render_page2():
    return render_template('CocoB.html')
    
@app.route("/fufu")
def render_page3():
    return render_template('fufu.html')
  
@app.route("/CCFR")
def render_page4():
    return render_template('CCFR.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)