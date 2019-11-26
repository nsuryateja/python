import json
import difflib

def data_loader():
    """Loads the data into dictionary from a JSON file"""
    with open("data.json") as f:
        data = f.read()
    return json.loads(data)

def close_finder(word):
    """Returns the close matches in the dictionary"""
    return difflib.get_close_matches(word,data_loader(),n=1)

def translator(input,confirmation):
    """Checks for the respective definition in the dictionary and displays to the user"""
    while True:
        #Checks for rain like words
        if input in data:
            return "\n".join(data[input])
        #Checks for India like words i.e., Proper nouns
        if input.title() in data:
            return "\n".join(data[input.title()])
        #Checks for USA like words i.e., Fullforms
        if input.upper() in data:
            return "\n".join(data[input.upper()])
        #Checks for close matches
        input = "".join(close_finder(input))
        if input in data:
            while True:
                if confirmation == "y":
                    return "\n".join(data[input])
                elif confirmation == "n":
                    return "Word doesn't exist"
                else:
                    return "We didn't understand your input! Sorry! Try again"
        else:
            return "Word doesn't exist"
data = data_loader()
print(translator("Main","y"))

##################################

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/result")
def result():
  output = result.get
  return render_template("result.html")

if __name__ == "__main__":
  app.run()
  
 #################################
 
 <!DOCTYPE html>
<html>
<head>
	<title>Python Rocks!</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha3js84-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="{{url_for('home')}}"><strong>Home</strong></a>
</nav>
 
  {%block content%}
  {%endblock content%}
</body>
</html>

###################################

{%extends "base.html"%}

 {%block content%}
 <div class = "jumbotron">
 <h1> Hi there! How you doing? </h1>
 <h1> Enter any word to know the meaning: </h1>
 <form action = "{{url_for('result')}}">
   <label for = "word">
   <input type = "text" name= "word" placeholder = "Enter here">
   <input type = "submit" value = "Enter">
  </form>
 </div>
 {%endblock content%}
 
 ##################################
 
 {%extends "base.html"%}

 {%block content%}
 <div class = "jumbotron">
 <a href = "{{url_for('home')}}">Click here to check for another one</a>
 </div>
 {%endblock content%}
 
 #####################################
