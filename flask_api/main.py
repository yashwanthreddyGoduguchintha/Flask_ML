from flask import Flask,render_template

#intitialise the app
app =Flask(__name__)


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

"""