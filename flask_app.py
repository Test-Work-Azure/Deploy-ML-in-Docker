from flask import Flask,request,redirect,url_for,flash,jsonify
import numpy as np
import json
import pyspark_code as pc
import pandas as pd

app = Flask(__name__)
@app.route('/api',methods = ['POST'])
def makepreds():
    data = request.get_json(force = True)
    #json_data = { i:v for i,v in enumerate(data) }
    preds = pc.model_run(data,df_index = [0])
    return jsonify({'preds' : preds['prediction'].values[0]})


if __name__ == '__main__':
    app.run(debug = True,port='5000')
