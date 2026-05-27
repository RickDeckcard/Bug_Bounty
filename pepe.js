// logger.js
fetch('https://deckcard23.com/logger.php')
  .then(response => response.text())
  .then(data => console.log(data));
