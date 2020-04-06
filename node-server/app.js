const express = require('express');
const multer = require('multer');
const app = express();

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
}).single("mypdf")

//mypdf -> attribute of file in view

app.post("/uploadPdf", function(req, res, next){

    upload(req,res,function(err){
        if(err)res.send(err)
        else res.send("success")
    })
})

app.listen(8080, function(err){
    if(err)throw err
    console.log("listening at PORT 8080")
})
