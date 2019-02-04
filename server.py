import os
import io
from flask import request
from flask import Flask
from flask import Response
from google.cloud import storage


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
    
    upload_blob('testbarnes2197', fpath, f.filename,)
    return "It worked"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)


    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.' .format(
        destination_blob_name,
        bucket_name
    ))



if __name__ == '__main__':
    app.run(debug='true')
    
