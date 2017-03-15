var k = null
window.onload = function() {

	b = new Base_Wrapper
    b.start_game();
	
    var s = new WebSocket("ws://localhost:9876/");
    k = s;
        s.onopen = function(e) { console.log("opened"); }
        s.onclose = function(e) { console.log("closed"); }
        s.onmessage = function(e) { 
			// triggered when data is received from the server
			s.send(JSON.stringify(b.current_game_state()));        
			console.log(e.data);
			
      }
      
   	
      	
    };
function send_data(){
   		k.send(JSON.stringify(b.current_game_state()));
   	}
