
// Variables for ID's listed under PixelArt.html.
let boxHeight = document.getElementById('inputHeight');

let boxWidth = document.getElementById('inputWidth');

let colorPicker = document.getElementById('colorPicker');

let sizePicker = document.getElementById('sizePicker');

let gridCanvas = document.getElementById('pixelCanvas');

// Function to create a grid based on width and height values.
/**
  * @desc create a grid of squares
  * @param int $boxWidth - number of squares representing the width of the grid
  * @param int $boxHeight - number of squares representing the height of the grid
*/
function makeGrid(boxHeight, boxWidth) {
  gridCanvas.innerHTML= "";
  for (var c = 0; c <= (boxHeight.value-1); c++){
    var tableColumn = document.createElement("tr");
    for (var r = 0; r <= (boxWidth.value-1); r++){
      var tableCell = document.createElement("td");
      tableColumn.appendChild(tableCell);
    };
  gridCanvas.appendChild(tableColumn);
  // Event listener to paint the cell.
  tableColumn.addEventListener('click',function(color){
    if (color.target.style.backgroundColor){
      color.target.removeAttribute('style');
    } else {
      color.target.style.backgroundColor = colorPicker.value;
    };
  });
  };
};


// When grid size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function (event) {
  event.preventDefault();
  makeGrid(boxHeight, boxWidth);
});
