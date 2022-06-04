let canvas = document.getElementById("main-window");
let ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

/**
 * 设置
 */
class Config {

    /**
     * 帧数
     */
    static FPS = 60;

    /**
     * 每帧的更新时间
     */
    static frameUpdateTime = 1000 / this.FPS;

    /**
     * 背景在每帧中移动的距离
     */
    static background_dx = 0.5;
};


let img = new Image();
img.src = "../asset/image/background-day.png";
img.onload = function () {

    let arr = new Array();

    let num = (Math.floor(canvas.width / img.width) + 1) * 2;
    for (let i = 0; i < num; i++) {
        arr.push(i * img.width);
    }

    setInterval(() => {

        for (let i = 0; i < arr.length; i++) {
            ctx.drawImage(img, arr[i], 0, img.width, canvas.height);
            arr[i] -= Config.background_dx;
        }
        if (arr[0] <= -img.width) {
            for (let i = 0; i < arr.length; i++) {
                arr[i] += img.width;
            }
        }

    }, Config.frameUpdateTime);
};