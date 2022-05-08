let last_timestamp = 0;
let x = 0;
let y = 0;
function $$(id){
    return document.getElementById(id);
}
function pageLoad(timedelta){
    var can = $$('can');
    var cansback = can.getContext('2d');
    cansback.fillStyle = "rgba(1, 1, 1, 0.2)";
    cansback.fillRect(0, 0, 1600, 1200);

    var can1 = $$('can');
    var cans = can1.getContext('2d');
    cans.beginPath();
    cans.arc(x+timedelta/50,y+timedelta/50,70,0,Math.PI*0.5,true);
    cans.closePath();
    cans.fillStyle = 'pink';//本来这里最初使用的是red，截图一看，傻眼了，怕上街被爱国者打啊，其实你懂的~~
    cans.fill();
}

let AC_GAME_ANIMATION = function(timestamp) {
    if(last_timestamp == 0){
        last_timestamp = timestamp;
    }
    timedelta = timestamp - last_timestamp;
    pageLoad(timedelta)
    requestAnimationFrame(AC_GAME_ANIMATION);
}  
function render() {
    requestAnimationFrame(AC_GAME_ANIMATION);
}