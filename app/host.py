from flask import render_template,flash, request, redirect, url_for,session,send_from_directory
from werkzeug.utils import secure_filename
import os
from datetime import date
import glob
from app import app
import pandas as pd
"""
CODE FOR THE FIRST PAGE UPLOAD.HTML
"""
@app.route('/', methods = ['GET'])
def upload_file():
    return render_template('upload.html')

@app.route('/', methods=['POST'])#POST Request is sent if both files are uploaded
def saveFile():
    try:
        print(request.files)
        file1 = request.files["file1"]#('file1', None)
        file2 = request.files["file2"]#
        print(file1.filename)
        if file1 != None and file2 != None:
            file1.save(file1.filename)
            file2.save(file2.filename)
            df1 = pd.read_csv(file1.filename)
            df2 = pd.read_csv(file2.filename)
            df1 =  df1.append(df2,ignore_index = False)#concatenate the two dataframe
            df = pd.DataFrame()
            df["Total"] = df1['PickPack Fee'] +  df1['Payment Gateway'] + df1['Commission']
            df["Profit"] =(df1["Sale Amount"] - df1["Cost Price"] - df["Total"])/(df1["Cost Price"] + df["Total"])*100
            df["Transfer"] = df1['Transferred Amount']
            return df.to_html()
            
        return redirect(url_for('upload_file'))
    except Exception as e:
        return str(e)
 
