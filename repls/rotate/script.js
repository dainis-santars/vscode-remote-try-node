var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.translate(300, 295);
ctx.rotate(-90 * Math.PI / 180);
ctx.fillRect(0, 0, 290, 10);
ctx.translate(-300, -295);

ctx.fillRect(300, 300, 10, 290);

ctx.arc(300, 300, 100, 0, 90 * Math.PI / 180);
ctx.stroke();


// ctx.arc(0, 0, 5, 0, 2 * Math.PI);
// ctx.fillStyle = "blue";
// ctx.fill();

// Math.PI + (Math.PI * j) / 2