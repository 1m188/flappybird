/**
 * 图片资源
 */
class Res {

    /**
     * 资源加载数目
     */
    static num = 0;

    /**
     * 0-9的数字，应是一个数组存储
     */
    static numbers = new Array();

    /**
     * 白天背景
     */
    static background_day = new Image();

    /**
     * 黑夜背景
     */
    static background_night = new Image();

    /**
     * 地面
     */
    static base = new Image();

    /**
     * 游戏结束标志
     */
    static gameover = new Image();

    /**
     * 游戏开始信息
     */
    static message = new Image();

    /**
     * 水管 绿色 向上
     */
    static pipe_green_up = new Image();

    /**
     * 水管 绿色 向下
     */
    static pipe_green_down = new Image();

    /**
     * 水管 红色 向上
     */
    static pipe_red_up = new Image();

    /**
     * 水管 红色 向下
     */
    static pipe_red_down = new Image();

    /**
     * 蓝鸟 翅膀向下
     */
    static bluebird_downflap = new Image();

    /**
     * 蓝鸟 翅膀向中
     */
    static bluebird_midflap = new Image();

    /**
     * 蓝鸟 翅膀向上
     */
    static bluebird_upflap = new Image();

    /**
     * 红鸟 翅膀向下
     */
    static redbird_downflap = new Image();

    /**
     * 红鸟 翅膀向中
     */
    static redbird_midflap = new Image();

    /**
     * 红鸟 翅膀向上
     */
    static redbird_upflap = new Image();

    /**
     * 黄鸟 翅膀向下
     */
    static yellowbird_downflap = new Image();

    /**
     * 黄鸟 翅膀向中
     */
    static yellowbird_midflap = new Image();

    /**
     * 黄鸟 翅膀向上
     */
    static yellowbird_upflap = new Image();

    /**死亡音乐 */
    static die = new Audio();

    /**碰壁音乐 */
    static hit = new Audio();

    /**得分音乐 */
    static point = new Audio();

    /**扇翅膀音乐 */
    static wing = new Audio();

    /**
     * 加载所有资源
     */
    static load(afterload) {
        if (Res.numbers.length != 0) return; // 已经加载完了就不必再加载了

        for (let i = 0; i <= 9; i++) {
            let img = new Image();
            img.src = "./asset/image/" + String(i) + ".png";
            img.onload = function () { Res.num++; };
            Res.numbers.push(img);
        }

        Res.background_day.src = "./asset/image/background_day.png";
        Res.background_day.onload = function () { Res.num++; };

        Res.background_night.src = "./asset/image/background_night.png";
        Res.background_night.onload = function () { Res.num++; };

        Res.base.src = "./asset/image/base.png";
        Res.base.onload = function () { Res.num++; };

        Res.gameover.src = "./asset/image/gameover.png";
        Res.gameover.onload = function () { Res.num++; };

        Res.message.src = "./asset/image/message.png";
        Res.message.onload = function () { Res.num++; };

        Res.pipe_green_up.src = "./asset/image/pipe_green_up.png";
        Res.pipe_green_up.onload = function () { Res.num++; };

        Res.pipe_green_down.src = "./asset/image/pipe_green_down.png";
        Res.pipe_green_down.onload = function () { Res.num++; };

        Res.pipe_red_up.src = "./asset/image/pipe_red_up.png";
        Res.pipe_red_up.onload = function () { Res.num++; };

        Res.pipe_red_down.src = "./asset/image/pipe_red_down.png";
        Res.pipe_red_down.onload = function () { Res.num++; };

        Res.bluebird_downflap.src = "./asset/image/bluebird_downflap.png";
        Res.bluebird_downflap.onload = function () { Res.num++; };

        Res.bluebird_midflap.src = "./asset/image/bluebird_midflap.png";
        Res.bluebird_midflap.onload = function () { Res.num++; };

        Res.bluebird_upflap.src = "./asset/image/bluebird_upflap.png";
        Res.bluebird_upflap.onload = function () { Res.num++; };

        Res.redbird_downflap.src = "./asset/image/redbird_downflap.png";
        Res.redbird_downflap.onload = function () { Res.num++; };

        Res.redbird_midflap.src = "./asset/image/redbird_midflap.png";
        Res.redbird_midflap.onload = function () { Res.num++; };

        Res.redbird_upflap.src = "./asset/image/redbird_upflap.png";
        Res.redbird_upflap.onload = function () { Res.num++; };

        Res.yellowbird_downflap.src = "./asset/image/yellowbird_downflap.png";
        Res.yellowbird_downflap.onload = function () { Res.num++; };

        Res.yellowbird_midflap.src = "./asset/image/yellowbird_midflap.png";
        Res.yellowbird_midflap.onload = function () { Res.num++; };

        Res.yellowbird_upflap.src = "./asset/image/yellowbird_upflap.png";
        Res.yellowbird_upflap.onload = function () { Res.num++; };

        Res.die.src = "./asset/audio/die.ogg";
        Res.hit.src = "./asset/audio/hit.ogg";
        Res.point.src = "./asset/audio/point.ogg";
        Res.wing.src = "./asset/audio/wing.ogg";

        let timer = setInterval(function () {
            if (!Res.is_ready()) return;
            clearInterval(timer);
            afterload();
        }, 10);
    }

    static is_ready() {
        return Res.num == 28;
    }
};