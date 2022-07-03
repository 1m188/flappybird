const canvas = document.getElementsByTagName("canvas")[0];
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const speed = 2;

/**
 * 图片资源
 */
class Res_img {

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

    /**
     * 加载所有图片资源
     */
    static load(afterload) {
        if (Res_img.numbers.length != 0) return; // 已经加载完了就不必再加载了

        for (let i = 0; i <= 9; i++) {
            let img = new Image();
            img.src = "./asset/image/" + String(i) + ".png";
            img.onload = function () { Res_img.num++; }
            Res_img.numbers.push(img);
        }

        Res_img.background_day.src = "./asset/image/background_day.png"
        Res_img.background_day.onload = function () { Res_img.num++ };

        Res_img.background_night.src = "./asset/image/background_night.png"
        Res_img.background_night.onload = function () { Res_img.num++ };

        Res_img.base.src = "./asset/image/base.png"
        Res_img.base.onload = function () { Res_img.num++ };

        Res_img.gameover.src = "./asset/image/gameover.png"
        Res_img.gameover.onload = function () { Res_img.num++ };

        Res_img.message.src = "./asset/image/message.png"
        Res_img.message.onload = function () { Res_img.num++ };

        Res_img.pipe_green_up.src = "./asset/image/pipe_green_up.png"
        Res_img.pipe_green_up.onload = function () { Res_img.num++ };

        Res_img.pipe_green_down.src = "./asset/image/pipe_green_down.png"
        Res_img.pipe_green_down.onload = function () { Res_img.num++ };

        Res_img.pipe_red_up.src = "./asset/image/pipe_red_up.png"
        Res_img.pipe_red_up.onload = function () { Res_img.num++ };

        Res_img.pipe_red_down.src = "./asset/image/pipe_red_down.png"
        Res_img.pipe_red_down.onload = function () { Res_img.num++ };

        Res_img.bluebird_downflap.src = "./asset/image/bluebird_downflap.png"
        Res_img.bluebird_downflap.onload = function () { Res_img.num++ };

        Res_img.bluebird_midflap.src = "./asset/image/bluebird_midflap.png"
        Res_img.bluebird_midflap.onload = function () { Res_img.num++ };

        Res_img.bluebird_upflap.src = "./asset/image/bluebird_upflap.png"
        Res_img.bluebird_upflap.onload = function () { Res_img.num++ };

        Res_img.redbird_downflap.src = "./asset/image/redbird_downflap.png"
        Res_img.redbird_downflap.onload = function () { Res_img.num++ };

        Res_img.redbird_midflap.src = "./asset/image/redbird_midflap.png"
        Res_img.redbird_midflap.onload = function () { Res_img.num++ };

        Res_img.redbird_upflap.src = "./asset/image/redbird_upflap.png"
        Res_img.redbird_upflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_downflap.src = "./asset/image/yellowbird_downflap.png"
        Res_img.yellowbird_downflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_midflap.src = "./asset/image/yellowbird_midflap.png"
        Res_img.yellowbird_midflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_upflap.src = "./asset/image/yellowbird_upflap.png"
        Res_img.yellowbird_upflap.onload = function () { Res_img.num++ };

        let timer = setInterval(function () {
            if (!Res_img.is_ready()) return;
            clearInterval(timer);
            afterload();
        }, 10);
    }

    static is_ready() {
        return Res_img.num == 28;
    }
};

/**
 * 精灵类
 */
class Sprite {
    constructor(img) {
        this.img = img;
        this.x = 0;
        this.y = 0;
        this.width = img.width;
        this.height = img.height;
    }

    draw() {
        ctx.drawImage(this.img, this.x, this.y, this.width, this.height);
    }

    before_draw() {
    }

    after_draw() {
    }

    run() {
        this.before_draw();
        this.draw();
        this.after_draw();
    }

    move(dx, dy) {
        this.x += dx;
        this.y += dy;
    }

    moveTo(x, y) {
        this.x = x;
        this.y = y;
    }
};

/**
 * 背景
 */
class Background extends Sprite {
    constructor() {
        super(Res_img.background_day);
        this.width = canvas.height / this.height * this.width;
        this.height = canvas.height;
    }

    after_draw() {
        let end = this.x + this.width;
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, 0, this.width, this.height);
            end += this.width;
        }

        this.move(-speed, 0);

        if (this.x + this.width <= 0) {
            this.moveTo(0, 0);
        }
    }
};

/**
 * 地面
 */
class Base extends Sprite {
    constructor() {
        super(Res_img.base);
        this.moveTo(0, canvas.height - this.height);
    }

    after_draw() {
        let end = this.x + this.width;
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, this.y, this.width, this.height);
            end += this.width;
        }

        this.move(-speed, 0);

        if (this.x + this.width <= 0) {
            this.moveTo(0, this.y);
        }
    }
};

/**
 * 小鸟
 */
class Bird extends Sprite {
    constructor() {
        super(Res_img.redbird_upflap);

        // 动画
        this.ani = new Array();
        this.ani.push(Res_img.redbird_upflap);
        this.ani.push(Res_img.redbird_midflap);
        this.ani.push(Res_img.redbird_downflap);
        this.ani.push(Res_img.redbird_midflap);

        this.ani_idx = 0; // 当前动画显示图片

        let that = this;

        // 每隔一定时间图片变换，达到动画放映的效果
        this.ani_timer = setInterval(function () {
            that.ani_idx = (that.ani_idx + 1) % that.ani.length;
            that.img = that.ani[that.ani_idx];
        }, 200);

        this.dy = 0.5;
        this.acc = 0.9;

        // 按键监听
        document.onclick = function () {
            that.move(0, -8);
            that.dy = -8;
        }

        this.moveTo(canvas.width / 6, canvas.height / 4);
    }

    after_draw() {
        this.move(0, this.dy);
        this.dy += this.acc;
    }

    /**
     * 碰撞检测
     * @param {Sprite} rect 待检测矩形
     * @return 是否撞上 true/false
     */
    collide(rect) {
        let x1 = this.x + this.width / 2;
        let y1 = this.y + this.height / 2;
        let x2 = rect.x + rect.width / 2;
        let y2 = rect.y + rect.height / 2;
        return Math.abs(x1 - x2) < this.width / 2 + rect.width / 2 &&
            Math.abs(y1 - y2) < this.height / 2 + rect.height / 2;
    }
};

class Pipe {
    constructor() {
        this.up = new Sprite(Res_img.pipe_green_up);
        this.down = new Sprite(Res_img.pipe_green_down);
        this.up.x = this.down.x = canvas.width;
        this.dist = Math.max(canvas.height - Res_img.base.height - this.up.height - this.down.height, Res_img.bluebird_downflap.height + 200);
        this.minbottom = Math.max(5, canvas.height - Res_img.base.height - this.up.height - this.dist);
        this.maxbottom = Math.min(this.down.height, canvas.height - Res_img.base.height - 5 - this.dist);
        this.get_random_pos();
        this.isleftbird = false;
    }

    get_random(min, max) {
        return Math.floor(Math.random() * (max + 1 - min) + min);
    }

    get_random_pos() {
        let dist_y = this.get_random(this.minbottom, this.maxbottom);
        this.down.y = dist_y - this.down.height;
        this.up.y = dist_y + this.dist;
    }

    run() {
        this.up.draw();
        this.down.draw();
        this.up.x -= speed;
        this.down.x -= speed;
    }
};

Res_img.load(main);

function main() {

    let background = new Background();
    let base = new Base();
    let bird = new Bird();

    let pipes = new Array();
    pipes.push(new Pipe());

    setInterval(function () {

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        background.run();
        for (let i = 0; i < pipes.length;) {
            let e = pipes[i];
            e.run();
            if (e.up.x + e.up.width <= 0) {
                pipes.splice(i, 1);
            } else {
                if (e.up.x + e.up.width <= bird.x && !e.isleftbird) {
                    e.isleftbird = true;
                    pipes.push(new Pipe());
                }
                i++;
            }
        }

        base.run();
        bird.run();

    }, 1000 / 60);
}