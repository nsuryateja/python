#Flask Dynamic Routing Example: Puppy latin Conversion - puppy to puppiful and pupp to puppy
from flask import Flask
app = Flask(__name__)

@app.route("/some_page/<naem>")
def hello(name):
    if not name.endswith("y"):
        return name + "y"
    else:
        return name[:-1] + "iful"
     
if __name__ == "__main__":
    app.run(debug=True)
       
