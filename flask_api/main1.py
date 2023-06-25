from flask import Flask,render_template,request
import joblib

#intitialise the app
app =Flask(__name__)

#load the model
model = joblib.load('joblib_model.pkl')


#@app.route('/')  #/(root)->route executed and excute hello world
#def home():
 #   return "hello world"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/event') #reroute to event page
def event():
   return render_template('event.html')


@app.route('/aboutus')
def aboutus():
    return render_template('about.html')


@app.route('/contact')
def contact():
   return render_template('contactus.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/predict', methods=['POST'])
def predict():
    preg = request.form.get('preg') #get method from dictionary
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    columns = [float(x) for x in [preg, plas, pres, skin, test, mass, pedi, age]] #float or Integer
    result = model.predict([columns])
    if result[0] ==0:
        return "You are safe!!"
    return "OOps!! you are Diabetic!"

    #return"Hola!form is submitted"
#run
app.run(port=9090, host='0.0.0.0') #python to pick automatic domain name




@app.route('/images')
def images():
    return render_template('images.html')

#run
app.run()

"""

https://127.0.0.1:5000/
http-hypertexttransfer protocal
127.0.0.1-ip address
5000-port
/-route(or) root

Rules:-
new directory->"templates"(all html pages should be present here)
#render template ->use .html
HTTP METHOD:
1)GET:backend to frontend(retive data from DB)
2)Post :sending data from frontend to backend(send message) (insert)
3)Delete: delete entire operation
4)put: update the existing data(sending data from frontend to backend)
#<form style="padding: 0.5;font-weight: bold;text-align: center;display: block;" method="post" action="/predict"> ->home.html
<p><label>Name <input type="text" name="first_name" placeholder="first name" required></label></p>
<p><label> Email<input type="email" name="mail" placeholder="Mail address" required></label></p>
<p><label> Pin code<input type="number" name="pin code" placeholder="pin code" required></label></p>
<p><label>Description<input type="text" name="description" placeholder="description" required></label></p>
(optional)
<form method="post" action="/predict">
      <p><label> preg<input type="number" name="preg" placeholder="preg" required></label></p>
      <p><label> plas<input type="number" name="plas" placeholder="plas" required></label></p>
      <p><label> pres<input type="number" name="pres" placeholder="pres" required></label></p>
      <p><label> skin<input type="number" name="skin" placeholder="skin" required></label></p>
      <p><label> test<input type="number" name="test" placeholder="test" required></label></p>
      <p><label> mass<input type="number" name="mass" placeholder="mass" required></label></p>
      <p><label> pedi<input type="number" name="pedi" placeholder="pedi" required></label></p>
      <p><label> age<input type="number" name="age" placeholder="age" required></label></p>
      <p><button>Submit</button></p>
    </form>
    #step allow decimal number
"""