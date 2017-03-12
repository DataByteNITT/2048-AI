var express = require('express');
var path = require('path');
var router = express.Router();
var PythonShell = require('python-shell');

// var pyshell = new PythonShell(asdf);
//var pyshell = new PythonShell("test.py");
// pyshell = new PythonShell(path.join(__dirname, "../public/ai_brain/eval.py"));
//pyshell = new PythonShell("./test.py");

// sends a message to the Python script via stdin

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.post('/compute', function(req,res){
var pyshell = new PythonShell( 'public/ai_brain/eval.py'  );
	console.log("received data from JS",req.body);


	pyshell.send('2');
	// res.sendStatus(200);

pyshell.on('message', function (message) {
	  // received a message sent from the Python script (a simple "print" statement)
	  console.log(message);
	   res.status(200).send(message);
	   //res.render('index',{'move':message})
	});

});



module.exports = router;
