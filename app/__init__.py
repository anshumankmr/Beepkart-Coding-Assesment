from flask import Flask
import os
#from waitress import serve


app = Flask(__name__,template_folder='../templates/',static_folder='../static')
app.config['SECRET_KEY'] = b"\x90\xa2\xaa=\x85\xa7\x1d'W\xc0/\xf7+\xe8\xde\x04\x99\xbd\xb5\xf8[\nB\x14" #os.urandom(24)#need to set up config file  
#For Demo Purpose Only https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),"uploads")


from app import host