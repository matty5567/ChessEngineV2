
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



let piece = document.createElement('div');
piece.className = 'piece bk';
piece.draggable="true";
piece.id = 'bk'
piece.addEventListener('dragstart', onDragStart)
let position = document.getElementById('square77');
position.appendChild(piece);

