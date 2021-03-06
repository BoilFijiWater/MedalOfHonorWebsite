from flask import Flask, url_for, render_template, request, Markup, flash, Markup
import os
import json

app = Flask(__name__)

with open('medal_of_honor.json') as usmilitary_data:
        position = json.load(usmilitary_data)
        
def toOption(s):
    return Markup('<option value="' + s + '" >' + s + "</option>")
    
def get_location_opions():
    LocationFaught = []
    print(type(LocationFaught))
    for p in position:
        if p["awarded"]["location"]["name"] not in LocationFaught:
            LocationFaught.append(p["awarded"]["location"]["name"])
    
    return LocationFaught

@app.route("/GMYM")
def render_creed():
    str = ""
    for loc in get_location_opions():
        str += toOption(loc)
        
    
    return render_template('GMYM.html', strr = Markup(str))

def Loc(state):
    SP = ""
    for loc in position:
        if loc["awarded"]["location"]["name"] == state:
            SP = SP + loc["name"] + loc["awarded"]["date"]["full"]+ loc["awarded"]["issued"] + loc["awarded"]["citation"]
    
    return "name:" + " " + str(SP)  

@app.route("/wutu")
def render_ahj():
    str = ""
    for co in get_location_opions():
        str += toOption(co)
    chosenplace = request.args["name"]
    funfact = Loc(chosenplace)

    
    return render_template('GMYM.html', strr = Markup(str), angh = funfact)    

# this python code is for page 2 for the rank   
def get_ranks_opions():
    MilitaryRanks = []
    for r in position:
        if r["military record"]["rank"] not in MilitaryRanks:
            MilitaryRanks.append(r["military record"]["rank"])
    
    return MilitaryRanks
    
@app.route("/CocoB")
def render_fred():
    str = ""
    print(get_ranks_opions())
    for ran in get_ranks_opions():
        str += toOption(ran)
        
    return render_template('CocoB.html', strr = Markup(str))
    
def ran(Mreward):
    Mr = ""
    for ran in position:
        if ran["military record"]["rank"] == Mreward:
            Mr = Mr + ran["name"] + ran["military record"]["entered service at"] + ran["military record"]["company"] + ran["military record"]["organization"]
    
    return "name:" + " " + str(Mr)  

@app.route("/kutu")
def render_ajh():
    str = ""
    for pa in get_ranks_opions():
        str += toOption(pa)
    chosenrank = request.args["rank"]
    ff = ran(chosenrank)

    
    return render_template('CocoB.html', strr = Markup(str), angh = ff) 
   
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
  
    
if __name__=="__main__":
    app.run(debug=False, port=54321)