const canvas = document.getElementsByTagName("canvas")[0];
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

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
 * 导演类
 */
class Director {
    /**当前场景 */
    static scene = null;

    /** 每帧画面移动速度 */
    static speed = 2;

    /** 一帧多少毫秒 */
    static MSPF = 1000 / 60;

    /** 背景 */
    static background = null;

    /** 地面 */
    static base = null;

    /** 小鸟 */
    static bird = null;

    /** 水管对组成的数组 */
    static pipes = [];

    /**gameover */
    static gameover = null;

    /**message */
    static message = null;
};

/******************************************* ↓ 场景 ↓ *************************************************/

/**
 * 场景类
 */
class Scene {
    /**
     * 
     * @param  {[Iterable|Sprite]} sprites 待渲染之所有sprite
     */
    constructor(sprites) {
        this.run_timer = null;
        this.render_timer = null;
        /**所有待渲染sprite及其集合所组成的数组 */
        this.sprites = sprites;
        /**判定是否是可迭代对象函数 */
        this.isIterable = obj => obj != null && typeof obj[Symbol.iterator] === 'function';
    }

    start_render(interval) {
        let that = this;
        this.render_timer = setInterval(this.render, interval, that);
    }

    stop_render() {
        if (this.render_timer != null) {
            clearInterval(this.render_timer);
            this.render_timer = null;
        }
    }

    start_run(interval) {
        let that = this;
        this.run_timer = setInterval(this.run, interval, that);
    }

    stop_run() {
        if (this.run_timer != null) {
            clearInterval(this.run_timer);
            this.run_timer = null;
        }
    }

    /**
     * 迭代渲染
     * @param {Iterable|Sprite} obj 待渲染的sprite或可迭代对象
     */
    iter_render(obj) {
        if (!this.isIterable(obj)) obj.render();
        // 注意 for of 的使用，别错用成 for in 了！！
        else for (let o of obj) this.iter_render(o);
    }

    /**
     * 场景每帧渲染之内容
     * @param {Scene} instance 本类实例引用
     */
    render(instance) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        instance.iter_render(instance.sprites);
    }

    /**
     * 场景每帧所进行之操作
     * @param {Scene} instance 因为run作为参数在setinterval里运行，
     * 因此其中this指向setinterval函数本身，将原来的类实例传入，使其
     * 能够访问原本类实例的各种属性
     */
    run(instance) { }
}

/**
 * 游戏开始场景
 */
class StartScene extends Scene {
    constructor() {
        super([Director.background, Director.base, Director.bird, Director.message]);
        Director.bird.init();
        Director.bird.x = Director.message.x + Director.message.width / 2 - Director.bird.width / 2 - 50;
        Director.bird.y = Director.message.y + Director.message.height / 2 + 35;

        // 点击鼠标进入游戏场景
        let that = this;
        document.onclick = function () {
            that.stop_render();
            that.stop_run();
            Director.scene = new GameScene();
            Director.scene.start_render(Director.MSPF);
            Director.scene.start_run(Director.MSPF);
        }
    }

    run(instance) {
        Director.bird.ani_change();
        Director.background.run();
        Director.base.run();
    }
};

/**
 * 游戏场景
 */
class GameScene extends Scene {
    constructor() {
        super([Director.background, Director.pipes, Director.base, Director.bird]);
        Director.bird.init();
    }

    /**
     * 
     * @param {GameScene} instance 
     */
    run(instance) {

        // 判定小鸟是否撞上障碍物
        let f = false;
        if (Director.bird.y <= 0 ||
            Director.bird.y + Director.bird.height > Director.base.y) {
            f = true;
        }
        else {
            for (let o of Director.pipes) {
                if (Director.bird.collide(o[0]) || Director.bird.collide(o[1])) {
                    f = true;
                    break;
                }
            }
        }
        if (f) { // 撞上则停止
            instance.stop_run();
            instance.stop_render();
            Director.scene = new EndScene();
            Director.scene.start_render(Director.MSPF);
            Director.scene.start_run(Director.MSPF);
            return;
        }

        Director.background.run();
        Director.base.run();
        for (let o of Director.pipes) {
            o[0].run();
            o[1].run();
        }
        Director.bird.auto_down();
        Director.bird.ani_change();
        Director.bird.click_react();

        /**水管过去后出现新的水管 */
        for (let i = 0; i < Director.pipes.length;) {
            let eup = Director.pipes[i][0], edown = Director.pipes[i][1];
            if (eup.x + eup.width <= 0) {
                Director.pipes.splice(i, 1);
            } else {
                if (eup.x + eup.width <= Director.bird.x && !eup.isleftbird) {
                    eup.isleftbird = edown.isleftbird = true;
                    Director.pipes.push(get_pipes());
                }
                i++;
            }
        }
    }
}

/**
 * 游戏结束场景
 */
class EndScene extends Scene {
    constructor() {
        super([Director.background, Director.pipes, Director.base, Director.bird, Director.gameover]);
    }

    run(instance) {
        Director.gameover.run();
    }
};

/******************************************* ↑ 场景 ↑ *************************************************/

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
        super(Res_img.background_day);
        this.width = canvas.height / this.height * this.width;
        this.height = canvas.height;
    }

    render() {
        super.render();
        let end = this.x + this.width;
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, 0, this.width, this.height);
            end += this.width;
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
        super(Res_img.base);
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
        super(Res_img.redbird_upflap);

        // 动画
        this.ani = new Array();
        this.ani.push(Res_img.redbird_upflap);
        this.ani.push(Res_img.redbird_midflap);
        this.ani.push(Res_img.redbird_downflap);
        this.ani.push(Res_img.redbird_midflap);

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
        let that = this;
        document.onclick = function () {
            that.click = true;
        }
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
        }
    }
};

/**
 * 水管
 */
class Pipe extends Sprite {
    constructor(img) {
        super(img);
        /**是否已经被小鸟通过 */
        this.isleftbird = false;
    }

    run() {
        this.x -= Director.speed;
    }
};

/**
 * gameover
 */
class Gameover extends Sprite {
    constructor() {
        super(Res_img.gameover);
        this.x = canvas.width / 2 - this.width / 2;
        this.y = 0 - this.height;
    }

    run() {
        if (this.y + this.height < (canvas.height - Director.base.height) / 2) {
            this.y += Director.speed;
        }
    }
};

/**
 * message
 */
class Message extends Sprite {
    constructor() {
        super(Res_img.message);
        this.x = canvas.width / 2 - this.width / 2;
        this.y = canvas.height / 2 - this.height;
    }
};

/******************************************* ↑ 精灵 ↑ *************************************************/

/**
 * 获取一对随机高度的水管
 * @returns 上、下 水管
 */
function get_pipes() {
    let up = new Pipe(Res_img.pipe_green_up), down = new Pipe(Res_img.pipe_green_down);
    up.x = down.x = canvas.width;

    /**两水管之间的高度距离 */
    let dist = Math.max(canvas.height - Res_img.base.height - up.height - down.height, Res_img.bluebird_downflap.height + 200);
    /**水管最低边界 */
    let minbottom = Math.max(5, canvas.height - Res_img.base.height - up.height - dist);
    /**水管最高边界 */
    let maxbottom = Math.min(down.height, canvas.height - Res_img.base.height - 5 - dist);

    /**区间随机数函数 */
    let get_random = (min, max) => { return Math.floor(Math.random() * (max + 1 - min) + min); };

    let dist_y = get_random(minbottom, maxbottom);
    down.y = dist_y - down.height;
    up.y = dist_y + dist;

    return [up, down];
}

Res_img.load(main);

function main() {

    Director.background = new Background();
    Director.base = new Base();
    Director.bird = new Bird();
    Director.pipes.push(get_pipes());
    Director.gameover = new Gameover();
    Director.message = new Message();

    Director.scene = new StartScene();
    Director.scene.start_render(Director.MSPF);
    Director.scene.start_run(Director.MSPF);
}