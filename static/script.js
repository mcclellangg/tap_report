/* static/script.js */

// GLOBALS
let counter = 0;

// FUNCTIONS
function updateCount(c) {
  const display = document.getElementById("countDisplay");
  display.textContent = c;
}

function tapCounter() {
  counter++;
  const message = `Total clicks: ${counter}`;
  console.log("Click event occurred, " + message);
  updateCount(counter);
}
