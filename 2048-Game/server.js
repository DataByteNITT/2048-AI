var app = require('express')
//var http = require('http');
//var fs = require('fs');
//var index = fs.readFileSync('index.html');
app.get('/test', function(req, res) {
    res.sendfile('index.html', {root: __dirname })
});

