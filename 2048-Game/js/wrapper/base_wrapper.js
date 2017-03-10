function Base_Wrapper() {
	this.direction = {
		"up": 0,
		"right": 1,
		"down": 2,
		"left": 3,
	}
	this.game_manager = null;
	this.grid = null;
}

Base_Wrapper.prototype.start_game = function() {
	this.game_manager = new GameManager(4,KeyboardInputManager,HTMLActuator,LocalStorageManager);
	this.clone_grid();
};

Base_Wrapper.prototype.clone_grid = function() {
	this.grid = JSON.parse(JSON.stringify(this.game_manager.grid));
};

Base_Wrapper.prototype.move = function(move) {
	this.game_manager.inputManager.emit("move",move);
};

Base_Wrapper.prototype.equalize_tiles = function() {
	this.clone_grid();	
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
};
Base_Wrapper.prototype.current_game_state = function() {
	return this.game_manager.serialize();
};
