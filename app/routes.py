from flask import render_template,request
from app import app
#app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html",title="Home")
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",title="About Us",)
@app.route("/frequentlyaskquestions")
def frequentlyaskquestions():
    return render_template("frequentlyaskquestions.html",title="Frequently Ask Questions")
@app.route("/routes")
def routes():
    return render_template("routes.html",title="Routes")
@app.route("/login",methods=['GET','POST'])
def login():
   # post_username=str(request.form['uname'])
    #post_password=str(request.form['psw'])
    return render_template("login.html",title="Login") 


@app.route("/register",methods=['GET','POST'])
def register():
    usertype={"1":"shipper","2":"traveller","3":"middleman"}
    if request.method == "POST":
        post_email = str(request.form["email"])
        post_password= str(request.form["password"])
        #usertype=str(request.form["usertype"] )
        print(post_email,post_password)
        return redirect(url_for("home"))
    else:
        return render_template("register.html", usertype=usertype,title="Register")


@app.route("/traveler",methods=['GET','POST'])
def traveler():
    return render_template("traveler.html",title="Traveler")
@app.route("/shipper",methods=['GET','POST'])
def shipper():
    return render_template("shipper.html",title="Shipper")
@app.route("/middleman",methods=['GET','POST'])
def middleman():
   return render_template("middleman.html",title="Middleman")


