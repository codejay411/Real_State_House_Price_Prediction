  
from pickle import TRUE
from flask import Flask, request, jsonify,render_template
import util
import pandas as pd

app = Flask(__name__)

# @app.route('/', methods=['GET','POST'])
# def form():
#         list2=util.get_location_names()
#         return render_template('index.html',list=list2)
#         # return render_template('index.html')
@app.route('/', methods=['GET','POST'])
def result():
        if request.method=='POST':
                sqft = float(request.form['uiSqft'])
                location = request.form['uiLocations']
                bhk = int(request.form['uiBHK'])
                bath = int(request.form['uiBath'])
                balcony = int(request.form['uiBalcony'])
                result=util.get_estimated_price(location,sqft,bath,balcony,bhk)
                return render_template('index.html',score=result)
        else:
              list2=util.get_location_names()
              return render_template('index.html',list=list2)  


    
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=TRUE)