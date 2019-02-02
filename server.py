from flask import request
from flask import Flask
from flask import Response
from google.cloud import storage

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])



def file_upload():

    
    try:

        if request.method == "POST":
            f = request.files['the_img']
            upload_blob('testbarnes2197', f, 'newfile')
            return 'Upload Success'
            #return Response('Upload Sucessful')
    except:
        return 'Upload Faield'
        #return Response('Upload Failed')

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

print(file_upload())