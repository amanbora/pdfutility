const express = require('express');
const multer = require('multer');
const app = express();

var storage = multer.diskStorage({
    destination: function(req, file, callback){
        callback(null, './../resumes');
    },
    filename: function(req, file, callback){
        callback(null, file.fieldname + "_" + Date.now())
    }
});



