/******************************************* ↓ 精灵 ↓ *************************************************/

/**
 * 精灵类
 */
class Sprite {
    constructor(img) {
        this.img = img;
        this.x = this.y = 0;
        this.width = img.width;
        this.height = img.height;
    }

    /**
     * 每帧渲染操作
     */
    render() {
        ctx.drawImage(this.img, this.x, this.y, this.width, this.height);
    }

    /**
     * 每帧逻辑操作
     */
    run() { }

    /**
     * 碰撞检测
     * @param {Sprite} sprite 待检测矩形
     * @return 是否撞上 true/false
     */
    collide(sprite) {
        let x1 = this.x + this.width / 2;
        let y1 = this.y + this.height / 2;
        let x2 = sprite.x + sprite.width / 2;
        let y2 = sprite.y + sprite.height / 2;
        return Math.abs(x1 - x2) < this.width / 2 + sprite.width / 2 &&
            Math.abs(y1 - y2) < this.height / 2 + sprite.height / 2;
    }
};

/**
 * 背景
 */
class Background extends Sprite {
    constructor() {

        // 随机背景
        let x = Math.random();
        if (x < 0.5) super(Res.background_day);
        else super(Res.background_night);

        this.width = canvas.height / this.height * this.width;
        this.height = canvas.height;
    }

    render() {
        super.render();
        let end = this.x + this.width - 1; // 此处-1修复背景图片之间的细小间隔
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, 0, this.width, this.height);
            end += this.width - 1; // 此处-1同上
        }
    }

    run() {
        this.x -= Director.speed;

        if (this.x + this.width <= 0) {
            this.x = this.y = 0;
        }
    }
};

/**
 * 地面
 */
class Base extends Sprite {
    constructor() {
        super(Res.base);
        this.x = 0;
        this.y = canvas.height - this.height;
    }

    render() {
        super.render();
        let end = this.x + this.width;
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, this.y, this.width, this.height);
            end += this.width;
        }
    }

    run() {
        this.x -= Director.speed;

        if (this.x + this.width <= 0) {
            this.x = 0;
        }
    }
};

/**
 * 小鸟
 */
class Bird extends Sprite {
    constructor() {

        // 随机颜色小鸟
        let x = Math.random() * 3;
        if (x < 1) super(Res.redbird_upflap);
        else if (x < 2) super(Res.bluebird_upflap);
        else super(Res.yellowbird_upflap);


        // 动画
        this.ani = new Array();
        if (x < 1) {
            this.ani.push(Res.redbird_upflap);
            this.ani.push(Res.redbird_midflap);
            this.ani.push(Res.redbird_downflap);
            this.ani.push(Res.redbird_midflap);
        } else if (x < 2) {
            this.ani.push(Res.bluebird_upflap);
            this.ani.push(Res.bluebird_midflap);
            this.ani.push(Res.bluebird_downflap);
            this.ani.push(Res.bluebird_midflap);
        } else {
            this.ani.push(Res.yellowbird_upflap);
            this.ani.push(Res.yellowbird_midflap);
            this.ani.push(Res.yellowbird_downflap);
            this.ani.push(Res.yellowbird_midflap);
        }

        this.ani_idx = 0; // 当前动画显示图片索引
        this.ani_cnt = 0; // 帧数计数
        this.ani_num = 220 / Director.MSPF; // 目标帧数

        this.dy = 0.5; // 速度
        this.acc = 0.9; // 加速度
    }

    /**
     * 小鸟的某些参数初始化
     */
    init() {
        this.ani_idx = 0;
        this.img = this.ani[this.ani_idx];
        this.ani_cnt = 0;

        // 按键监听
        this.click = false;
        let func = (ev) => {
            if (ev.type === 'click' || (ev.type === 'keydown' && ev.keyCode === 32))
                this.click = true;
        }
        document.onclick = func;
        document.onkeydown = func;

        this.dy = 0.5; // 速度
    }

    /**
     * 小鸟自动掉下去
     */
    auto_down() {
        this.y += this.dy;
        this.dy += this.acc;
    }

    /**
     * 每隔一定时间图片变换，达到动画放映的效果
     */
    ani_change() {
        if (++this.ani_cnt >= this.ani_num) {
            this.ani_idx = (this.ani_idx + 1) % this.ani.length;
            this.img = this.ani[this.ani_idx];
            this.ani_cnt = 0;
        }
    }

    /**
     * 按键事件
     */
    click_react() {
        if (this.click) {
            this.click = false;
            this.y -= 8;
            this.dy = -8;
            Res.wing.play();
        }
    }
};

/**
 * 水管
 */
class Pipe extends Sprite {
    /**
     * 
     * @param {*} img 
     * @param {boolean} up 是否是朝上的水管（即上方的水管）
     * @param {number} move 水管垂直移动的速度
     */
    constructor(img, up, move = 0) {
        super(img);

        /**是否已经被小鸟通过 */
        this.isleftbird = false;

        this.up = up;
        this.move = move;
    }

    run() {
        this.x -= Director.speed;

        // 水管的垂直移动
        this.y += this.move;
        if (this.up) {
            if ((this.move > 0 && this.y + 5 >= canvas.height - Res.base.height) ||
                (this.move < 0 && this.y + this.height - 5 <= canvas.height - Res.base.height))
                this.move *= -1;
        } else {
            if ((this.move > 0 && this.y >= 0) ||
                (this.move < 0 && this.y + this.height - 5 <= 0))
                this.move *= -1;
        }
    }
};

/**
 * gameover
 */
class Gameover extends Sprite {
    constructor() {
        super(Res.gameover);
    }
};

/**
 * message
 */
class Message extends Sprite {
    constructor() {
        super(Res.message);
    }
};

/**
 * 分数
 */
class Grade extends Sprite {
    constructor() {
        super(Res.numbers[0]);
        this.num = [0];
        this.sw = this.img.width;
        this.sh = this.img.height;
        this.x += this.sw;
        this.y += this.sw;
    }

    render() {
        for (let i = 0; i < this.num.length; i++) {
            ctx.drawImage(Res.numbers[this.num[i]], this.x + i * this.sw, this.y, this.sw, this.sh);
        }
    }

    /**
     * @param {number} val
     */
    set score(val) {
        this.num.length = 0;
        if (val == 0) this.num.push(0);
        else {
            while (val) {
                this.num.unshift(val % 10);
                val = Math.floor(val / 10);
            }
        }
    }

    get score() {
        let res = 0;
        for (let i = 0; i < this.num.length; i++) {
            res = res * 10 + this.num[i];
        }
        return res;
    }
};

/******************************************* ↑ 精灵 ↑ *************************************************/