from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/") #annotation tells the url that will make this function run
def render_main():
    return render_template('index.html')

@app.route("/GMYM")
def render_page1():
    return render_template('GMYM.html')

@app.route("/CocoB")
def render_page2():
    return render_template('CocoB.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)