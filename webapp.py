from flask import Flask,render_template
app=Flask(__name__)

@app.route("/home.htm")
def home():
    #return "My home page"
    return render_template("home.htm")

#if(__name__=="__main__"):
 #   app.run()   



@app.route("/about.htm")
def about():
    #return "My about page"
    return render_template("about.htm")


@app.route("/")
def layout():
    #return "My courses page"
    return render_template("layout.htm")

@app.route("/service.htm")
def services():
    #return "My courses page"
    return render_template("service.htm")

if(__name__=="__main__"):
    app.run()
