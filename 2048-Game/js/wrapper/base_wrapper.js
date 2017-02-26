function Base_Wrapper() {
	this.direction = {
		"up": 0,
		"right": 1,
		"down": 2,
		"left": 3,
	}
	this.gameManager = null;
	this.grid = null;
}

Base_Wrapper.prototype.start_game = function() {
	this.gameManager = new GameManager(4,KeyboardInputManager,HTMLActuator,LocalStorageManager);
	this.grid = this.gameManager.grid;
};

Base_Wrapper.prototype.move = function(move) {
	this.gameManager.inputManager.emit("move",move);
};

Base_Wrapper.prototype.equalize_tiles = function() {
	
	var max = -1;
	for (var i = 0; i < 4; i++) {
		for (var j = 0; j <4 ; j++) {
			if(this.grid.cells[i][j]!=null){
				this.grid.cells[i][j].value = Math.log2(this.grid.cells[i][j].value);
				if(max < this.grid.cells[i][j].value){
					max = this.grid.cells[i][j].value;
				}
			}
		}
	}
	for (var i = 0; i < 4; i++) {
		for (var j = 0; j <4 ; j++) {
			if(this.grid.cells[i][j]!=null){
				this.grid.cells[i][j].value = (this.grid.cells[i][j].value/max).toFixed(2);
				
			}
		}
	}
	this.gameManager.actuate();
};