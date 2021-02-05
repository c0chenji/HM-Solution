

loadDirections = (lst, arrowCtx) => {
  for (let item of lst) {
    joinArrowPoints(arrowCtx, item[0], item[1]);
  }
}

function joinArrowPoints(targetCanvasCtx, start, end) {
  var headlen = 10;
  targetCanvasCtx.beginPath();
  targetCanvasCtx.moveTo(start[0], start[1]);
  //horizontal, x aixs' distance > y aixs' distance
  if (Math.abs(start[0] - end[0]) >= Math.abs(start[1] - end[1])) {
    //starts from left and goes up
    if (start[0] < end[0] && start[1] > end[1]) {
      var dx = end[0] - (start[0] + (end[0] - start[0]) * .5);
      var dy = end[1] - (start[1] - (start[1] - end[1]) * .2);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] + (end[0] - start[0]) * .4, start[1] - (start[1] - end[1]) * .1, start[0] + (end[0] - start[0]) * .5, start[1] - (start[1] - end[1]) * .2, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
    }
    //starts from left and goes down
    if (start[0] < end[0] && start[1] < end[1]) {
      var dx = end[0] - (start[0] + (end[0] - start[0]) * .5);
      var dy = end[1] - (start[1] + (start[1] - end[1]) * .2);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] + (end[0] - start[0]) * .4, start[1] + (start[1] - end[1]) * .1, start[0] + (end[0] - start[0]) * .5, start[1] + (start[1] - end[1]) * .2, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
      
    }
    //starts from right and goes up
    if (start[0] > end[0] && start[1] > end[1]) {
      var dx = end[0] - (start[0] - Math.abs(end[0] - start[0]) * .5);
      var dy = end[1] - (start[1] - (start[1] - end[1]) * .2);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] - Math.abs(end[0] - start[0]) * .4, start[1] - (start[1] - end[1]) * .1, start[0] - Math.abs(end[0] - start[0]) * .5, start[1] - (start[1] - end[1]) * .2, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
      
    }
    //starts from right and goes down
    if (start[0] > end[0] && start[1] < end[1]) {
      var dx = end[0] - (start[0] - Math.abs(end[0] - start[0]) * .5);
      var dy = end[1] - (start[1] + (start[1] - end[1]) * .2);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] - Math.abs(end[0] - start[0]) * .4, start[1] + (start[1] - end[1]) * .1, start[0] - Math.abs(end[0] - start[0]) * .5, start[1] + (start[1] - end[1]) * .2, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
      
    }
  }
  //vertically, x aixs' distance < y aixs' distance
  if (Math.abs(start[0] - end[0]) <= Math.abs(start[1] - end[1])) {
    //starts from top and goes to left
    if (start[1] < end[1] && start[0] > end[0]) {
      var dx = end[0] - (start[0] - Math.abs(end[0] - start[0]) * .4);
      var dy = end[1] - (start[1] + Math.abs(start[1] - end[1]) * .6);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] - Math.abs(end[0] - start[0]) * .2, start[1] + Math.abs(start[1] - end[1]) * .5, start[0] - Math.abs(end[0] - start[0]) * .4, start[1] + Math.abs(start[1] - end[1]) * .6, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
    }
    //starts from top and goes right
    if (start[1] < end[1] && start[0] < end[0]) {
      var dx = end[0] - (start[0] + Math.abs(end[0] - start[0]) * .4);
      var dy = end[1] - (start[1] + Math.abs(start[1] - end[1]) * .6);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] + Math.abs(end[0] - start[0]) * .2, start[1] + Math.abs(start[1] - end[1]) * .5, start[0] + Math.abs(end[0] - start[0]) * .4, start[1] + Math.abs(start[1] - end[1]) * .6, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
      
    }
    //starts from botton and goes left
    if (start[1] > end[1] && start[0] > end[0]) {
      var dx = end[0] - (start[0] - Math.abs(end[0] - start[0]) * .4);
      var dy = end[1] - (start[1] - Math.abs(start[1] - end[1]) * .6);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] - Math.abs(end[0] - start[0]) * .2, start[1] - Math.abs(start[1] - end[1]) * .5, start[0] - Math.abs(end[0] - start[0]) * .4, start[1] - Math.abs(start[1] - end[1]) * .6, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
      
    }
    //starts from botton and goes right
    if (start[1] > end[1] && start[0] < end[0]) {
      var dx = end[0] - (start[0] + Math.abs(end[0] - start[0]) * .4);
      var dy = end[1] - (start[1] - Math.abs(start[1] - end[1]) * .65);
      var angle = Math.atan2(dy, dx);
      targetCanvasCtx.bezierCurveTo(start[0] + Math.abs(end[0] - start[0]) * .2, start[1] - Math.abs(start[1] - end[1]) * .55, start[0] + Math.abs(end[0] - start[0]) * .4, start[1] - Math.abs(start[1] - end[1]) * .65, end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle - Math.PI / 6), end[1] - headlen * Math.sin(angle - Math.PI / 6));
      targetCanvasCtx.lineTo(end[0], end[1]);
      targetCanvasCtx.lineTo(end[0] - headlen * Math.cos(angle + Math.PI / 6), end[1] - headlen * Math.sin(angle + Math.PI / 6));
      targetCanvasCtx.stroke();
     
    }
  }
}

function loadText(mapResult,targetCanvasCtx){
  targetCanvasCtx.font = "10px Georgia";
  targetCanvasCtx.fillStyle = "white";
  for(let value of mapResult.values()){
    let text=(value[0]*100).toString();
    let result =text+"%";
    let endX= value[1][1][0];
    let endY = value[1][1][1];
    targetCanvasCtx.fillText(result, endX+10, endY+10);
  }
}

//arr the array of points,
//ctx document.getElementById(...)
function loadPolygons(arr, ctx) {
  // console.log("hi ", arr[0].points[0]);
  // var testCenter = get_polygon_centroid(arr[0].points);
  // console.log("the centroid is ", testCenter);
  // ctx.font = "20px Arial";
  // ctx.fillText("Zone 1", testCenter.x - 20, testCenter.y);
  for (let item of arr) {
    temp = item.points;
    // console.log(temp);
    // console.log("temp center is ", item.center);
    ctx.beginPath();
    ctx.moveTo(temp[0][0], temp[0][1]);
    for (let i = 1; i < temp.length; i++) {
      ctx.lineTo(temp[i][0], temp[i][1]);
    }
    ctx.lineTo(temp[0][0], temp[0][1]);
    ctx.stroke();
    // ctx.fill();
    ctx.fillText(item.zoneName, item.center.x - 15, item.center.y);
    // ctx.closePath();
  }
}

function loadImg(imgSource, imgCxt) {
  var image = new Image();
  image.onload = function () {
    imgCxt.drawImage(image, 0, 0, imgCanvas.width, imgCanvas.height);
  };
  // image.src = "{% static '/images/imgpsh_fullsize.jpg' %}";
  image.src = imgSource;
}
// draw circles in hc_ctx target
function drawCircle(x, y, radius, hc_ctx) {
  hc_ctx.beginPath();
  hc_ctx.arc(x, y, radius, 0, 2 * Math.PI);
  hc_ctx.stroke();
}

//load circles of dwelling time
function loadCircles(arr) {
  for (let item of arr) {
    drawCircle(item[0], item[1], item[2], hc_ctx);
  }
}

//calculate the center of polygon.
function get_polygon_centroid(pts) {
  var first = pts[0], last = pts[pts.length - 1];
  if (first[0] != last[0] || first[1] != last[1]) pts.push(first);
  var twicearea = 0,
    x = 0, y = 0,
    nPts = pts.length,
    p1, p2, f;
  for (var i = 0, j = nPts - 1; i < nPts; j = i++) {
    p1 = pts[i]; p2 = pts[j];
    f = (p1[1] - first[1]) * (p2[0] - first[0]) - (p2[1] - first[1]) * (p1[0] - first[0]);
    twicearea += f;
    x += (p1[0] + p2[0] - 2 * first[0]) * f;
    y += (p1[1] + p2[1] - 2 * first[1]) * f;
  }
  f = twicearea * 3;
  return { x: Math.round(x / f + first[0]), y: Math.round(y / f + first[1]) };
}