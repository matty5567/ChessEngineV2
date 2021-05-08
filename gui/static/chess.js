
function onDragStart(event) {
    event
      .dataTransfer
      .setData('text/plain', event.target.id);
  }

function dragEnter(event) {
    event.preventDefault();
    }

function onDragOver(event) {
    event.preventDefault();
  }

function onDrop(event) {

      event.target.classList.remove('drag-over');
      const id = event.dataTransfer.getData('text/plain');
      const draggable = document.getElementById(id);
      event.target.appendChild(draggable);

      fetch('/move')
      .then(function (response) {
          return response.json();
      }).then(function (text) {
          console.log('GET response:');
          console.log(text.body); 
      });
  }


let board = document.getElementById('chessboard');

for (var rank=1; rank<9; rank++){
    for (var file=1; file<9; file++){
        let square = document.createElement('div');
        square.id = "square" + String(rank) + String(file);
        square.addEventListener('dragenter', dragEnter)
        square.addEventListener('dragover', onDragOver)
        square.addEventListener('drop', onDrop)
        board.appendChild(square);
    }
}

function fenToBoard(fen){
  rows = fen.split('/');
  console.log(rows)
  
  for (var i=0; i<8; i++){
    if (rows[i] == '8'){
      continue
    }
    for (var j=0; j<8; j++){
      let piece = document.createElement('div');
      piece.className = 'piece ' + rows[i][j];
      piece.id = 'piece ' + rows[i][j] + ' ' + i + j;
      piece.draggable="true";
      piece.addEventListener('dragstart', onDragStart)
      let position = document.getElementById('square' + String(i+1) + String(j+1));
      console.log(rows[i][j])
      position.appendChild(piece);
    }

  }
}

function setup(){
  fetch('/start').then(function (response) {
    return response.json();
}).then(function (text) {
    console.log(text.body); 
    fenToBoard(text.body);

});
}

setup();

