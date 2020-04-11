const express = require('express');
const multer = require('multer');
const app = express();
var bodyParser = require('body-parser');
// let {PythonShell} = require('python-shell');
const pythonDir = ('./../'); // Path of python script folder
const pythonPdfEnv = pythonDir + "nlp_env/bin/python3"; // Path of the Python interpreter
const pythonDocxEnv = pythonDir + "nlp_env/bin/python3"; // Path of the Python interpreter
const { spawn } = require('child_process');
var path = require('path');
const json2csv = require('json2csv').parse;
const fs = require('fs');

var output = {};
var field = ['college_name',
'company_names',
'degree',
'designation',
'email',
'mobile_number',
'name',
'no_of_pages',
'skills',
'total_experience'] 

//allow cross origin requests
app.use(function(req, res, next) {
    res.setHeader("Access-Control-Allow-Methods", "POST, PUT, OPTIONS, DELETE, GET");
    res.header("Access-Control-Allow-Origin", req.headers.origin);
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Credentials", true);
    next();
});

app.use(express.static('../client'));
app.use(bodyParser.json()); 

var storage = multer.diskStorage({
    destination: function(req, file, callback){
        callback(null, './../resumes');
    },
    filename: function(req, file, callback){
        callback(null, file.fieldname + "_" + Date.now() + path.extname(file.originalname))
    }
});


var upload = multer({
    storage : storage,
}).single('file')

//mypdf -> attribute of file in view

// app.get('/', function(req,res){
//     res.render('upload');
// })


function cleanWarning(error) {
    return error.replace(/Detector is not able to detect the language reliably.\n/g,"");
}

let callPython = async function (scriptName,flag) {
    return new Promise(function(success, reject) {
        const script = pythonDir + scriptName;
        var pyprog = spawn(pythonPdfEnv, [script] );
        // const pyArgs = [script, JSON.stringify(args) ]
        if(flag == 'pdf'){
             pyprog = spawn(pythonPdfEnv, [script] );
        }
        if(flag == 'docx'){
             pyprog = spawn(pythonDocxEnv, [script] );
        }
        let result = "";
        let resultError = "";
        pyprog.stdout.on('data', function(data) {
            result += data.toString();
            success(result);
            console.log("Success");
            
        });

        pyprog.stderr.on('data', (data) => {
            resultError += cleanWarning(data.toString());
        });


   });
}


app.get('/Output', function(req,res){
    // res.write("Output of Pdf- \n");
    console.log(`${output} + ****************************`);
    output = JSON.parse(JSON.stringify(output));
    res.send(output);
})


app.post('/uploadPdf', function(req, res, next){

    upload(req,res,function(err){
        console.log(req.file);
        if(err){
            console.log(err);
            res.send(err)
        }
        else{
            // res.redirect('/pdfOuptut');
            const result = callPython('nlp.py','pdf').then((data)=>{
                output=data;
                res.send.bind(data);
                console.log(data);
                console.log("Pdf Input");
                res.send(data);
            })
            .catch((err)=>{
                console.log(err);
            });
        }
            
    })
})


app.post('/uploadDocx', function(req, res, next){

    upload(req,res,function(err){
        console.log(req.file);
        if(err){
            console.log(err);
            res.send(err)
        }
        else{
            // res.redirect('/pdfOuptut');
            const result = callPython('nlp.py','docx').then((data)=>{
                output=data;
                res.send.bind(data);
                console.log(data);
                console.log("Docx Input");
                res.send(data);
            })
            .catch((err)=>{
                console.log(err);
            });
        }
            
    })
})

app.get("/downloadCSV", function (req, res) {
    console.log("download called");
    const csv =  json2csv({ data: output , fields: field});
        // , function(err, csv) {
        // if (err) console.log(err);
        // console.log(csv);
    fs.writeFile('./../downloads/output.csv', csv, function(err) {
        if (err) throw err;
        console.log('csv file saved');
    });
    // });
    console.log(csv);

})

app.listen(8080, function(err){
    if(err)throw err
    console.log("listening at PORT 8080")
})
