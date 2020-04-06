const express = require('express');
const multer = require('multer');
const app = express();

//allow cross origin requests
app.use(function(req, res, next) {
    res.setHeader("Access-Control-Allow-Methods", "POST, PUT, OPTIONS, DELETE, GET");
    res.header("Access-Control-Allow-Origin", req.headers.origin);
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Credentials", true);
    next();
});


var storage = multer.diskStorage({
    destination: function(req, file, callback){
        callback(null, './../resumes');
    },
    filename: function(req, file, callback){
        callback(null, file.fieldname + "_" + Date.now() + ".pdf")
    }
});


var upload = multer({
    storage : storage,
}).single('file')

//mypdf -> attribute of file in view

app.post("/uploadPdf", function(req, res, next){

    upload(req,res,function(err){
        console.log(req.file);
        if(err)res.send(err)
        else res.send("success")
    })
})

app.listen(8080, function(err){
    if(err)throw err
    console.log("listening at PORT 8080")
})
