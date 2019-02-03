const express = require('express');
const bodyparser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 3001;
os = require('os');
fs = require('fs');
var Busboy = require('busboy');
app.use(cors());

app.listen(port);


app.post('/', (req,res) => {
    console.log("hi")
    
    var busboy = new Busboy({ headers: req.headers});
    busboy.on('image', (fieldname, image, filename, encoding, mimetype) => {
        var saveTo = path.join(os.tmpDir(), path.basename(fieldname));
        file.pipe(fs.createWriteStream(saveTo));
    });

    busboy.on('finish', () => {
        res.writeHead(200, {'Connection' : 'close'});
        res.end("That's all folks");
    });

    return req.pipe(busboy);
    //var image = req.body.image;
    //var imagepath = req.body.imagepath;
    
    

});

console.log('Server is running');