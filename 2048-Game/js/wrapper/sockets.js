window.onload = function() {

	b = new Base_Wrapper
        b.start_game()
	
        var s = new WebSocket("ws://localhost:9876/");
        s.onopen = function(e) { console.log("opened"); }
        s.onclose = function(e) { console.log("closed"); }
        s.onmessage = function(e) { 
        
		if (e.data === "A")
		{
		    b.move(0)
		    if (!b.gameManager.grid.cells[0][0])
    		    s.send("NULL")
    		else
    		    s.send((b.gameManager.grid))    
    	}
    	else if (e.data === "C")
		{
		    b.move(1)
		    if (!b.gameManager.grid.cells[0][0])
    		    s.send("NULL")
    		else
    		    s.send(b.gameManager.grid)  
    	}
		else if (e.data === "B")
		{
		    b.move(2)
		    if (!b.gameManager.grid.cells[0][0])
    		    s.send("NULL")
    		else
    		    s.send(String(b.gameManager.grid.cells[0][0].value))    
    	}
		else if (e.data === "D")
		{
		    b.move(3)
		    if (!b.gameManager.grid.cells[0][0])
    		    s.send("NULL")
    		else
    		    s.send(String(b.gameManager.grid.cells[0][0].value))    
    	}
        else
        {
            s.send("INVALID")
        }
      }	
    };

