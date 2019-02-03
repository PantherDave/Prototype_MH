import os
import io
from flask import request
from flask import Flask
from flask import Response



app = Flask(__name__)
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
#UPLOAD_FOLDER = 'C:\\Users\\Maurice\\Documents\\GitHub\\Prototype_MH\\selfie-saver\\tmp'
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Maurice\\Documents\\GitHub\\Prototype_MH\\selfie-saver\\tmp'

@app.route('/', methods = ['POST'])
def file_upload():    


    #if request.method == 'POST':
    f = request.files['']
    print(f)
    
    
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    fpath = (os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    
    #upload_blob('testbarnes2197', fpath, f.filename,)
    return "It worked"





if __name__ == '__main__':
    app.run(debug='true')
    
