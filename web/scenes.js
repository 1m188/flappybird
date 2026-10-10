/**
 * 获取一对随机高度的水管
 * @returns 上、下 水管
 */
function get_pipes() {

    /**区间随机数函数 */
    let get_random = (min, max) => { return Math.floor(Math.random() * (max + 1 - min) + min); };

    // 随机颜色水管。绿色为普通水管，红色为垂直移动水管
    let up = null, down = null; // 上下两对水管。up为朝上的水管（即下方的水管），down为朝下的水管（即上方的水管）
    if (Math.random() < 0.5) {
        up = new Pipe(Res.pipe_green_up, true);
        down = new Pipe(Res.pipe_green_down, false);
    }
    else {
        let a = 0, b = 0;
        let minv = -5, maxv = 5;
        while (a == 0) a = get_random(minv, maxv);
        while (b == 0) b = get_random(minv, maxv);
        up = new Pipe(Res.pipe_red_up, true, a);
        down = new Pipe(Res.pipe_red_down, false, b);
    }

    up.x = down.x = canvas.width;

    /**两水管之间的高度距离 */
    let dist = Math.max(canvas.height - Res.base.height - up.height - down.height, Res.bluebird_downflap.height + 200);
    /**水管最低边界 */
    let minbottom = Math.max(5, canvas.height - Res.base.height - up.height - dist);
    /**水管最高边界 */
    let maxbottom = Math.min(down.height, canvas.height - Res.base.height - 5 - dist);

    let dist_y = get_random(minbottom, maxbottom);
    down.y = dist_y - down.height;
    up.y = dist_y + dist;

    return [up, down];
}

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

        // 消息位置
        Director.message.x = canvas.width / 2 - Director.message.width / 2;
        Director.message.y = canvas.height / 2 - Director.message.height;

        // 小鸟位置
        Director.bird.x = Director.message.x + Director.message.width / 2 - Director.bird.width / 2 - 50;
        Director.bird.y = Director.message.y + Director.message.height / 2 + 35;

        // 点击鼠标或按下空格键进入游戏场景
        let startGame = (ev) => {
            if (ev.type === 'click' || (ev.type === 'keydown' && ev.keyCode === 32)) {

                // 取消之前的监听事件
                document.onclick = null;
                document.onkeydown = null;

                this.stop_render();
                this.stop_run();
                Director.scene = new GameScene();
                Director.scene.start_render(Director.MSPF);
                Director.scene.start_run(Director.MSPF);
            }
        }
        document.onclick = startGame;
        document.onkeydown = startGame;
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
        super([Director.background, Director.pipes, Director.base, Director.bird, Director.grade]);

        // 重新设定小鸟的各方面参数
        Director.bird.init();

        // 水管内容的重新设定
        Director.pipes.length = 0;
        Director.pipes.push(get_pipes());

        // 分数清零
        Director.grade.score = 0;
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

            // 清空小鸟监听函数
            document.onclick = null;
            document.onkeydown = null;

            Res.hit.play();
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
                    // 分数+1
                    Director.grade.score++;
                    Res.point.play();
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
        super([Director.background, Director.pipes, Director.base, Director.bird, Director.gameover, Director.grade]);

        // gameover位置
        Director.gameover.x = canvas.width / 2 - Director.gameover.width / 2;
        Director.gameover.y = 0 - Director.gameover.height;

        /**动画是否演完 */
        this.is_ani_finished = false;

        /**是否已经播放声音 */
        this.is_voice_played = false;
    }

    run(instance) {
        // gameover动画
        if (Director.gameover.y + Director.gameover.height < (canvas.height - Director.base.height) / 2) {
            Director.gameover.y += Director.speed;
        } else if (!instance.is_ani_finished) {
            instance.is_ani_finished = true; // 演完动画，设置点击事件，且只此一次

            // 单击鼠标或按下空格切换场景
            let getinStartScene = (ev) => {
                if (ev.type === 'click' || (ev.type === 'keydown' && ev.keyCode === 32)) {

                    // 取消之前的监听事件
                    document.onclick = null;
                    document.onkeydown = null;

                    instance.stop_render();
                    instance.stop_run();
                    Director.scene = new StartScene();
                    Director.scene.start_render(Director.MSPF);
                    Director.scene.start_run(Director.MSPF);
                }
            }
            document.onclick = getinStartScene;
            document.onkeydown = getinStartScene;
        }

        if (!instance.is_voice_played) {
            instance.is_voice_played = true;
            Res.die.play();
        }
    }
};

/******************************************* ↑ 场景 ↑ *************************************************/