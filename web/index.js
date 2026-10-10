/**
 * 接管全部触摸默认行为：对 touchstart 调用 preventDefault 后，
 * 浏览器不再对该页面做任何触摸手势识别（单击判定/双击缩放/长按菜单），
 * 从事件层面杜绝 Chromium 在手势判定期间暂停渲染导致的点按画面冻结。
 * （touchstart 在文档级默认是被动监听，不声明 passive: false 则无法 preventDefault）
 */
document.addEventListener('touchstart', (ev) => ev.preventDefault(), { passive: false });

/**
 * 首次用户手势时将各音效静音试播一次以解锁音频：
 * 部分移动端浏览器要求音频在用户手势内播放过一次，之后才允许游戏循环中程序化播放
 */
let unlock_audio = () => {
    for (let a of [Res.die, Res.hit, Res.point, Res.wing]) {
        a.muted = true;
        a.play().then(() => {
            a.pause();
            a.currentTime = 0;
            a.muted = false;
        }).catch(() => { a.muted = false; });
    }
    document.removeEventListener('pointerdown', unlock_audio);
    document.removeEventListener('keydown', unlock_audio);
};
document.addEventListener('pointerdown', unlock_audio);
document.addEventListener('keydown', unlock_audio);

// 资源全部加载之后运行主函数
Res.load(function () {

    Director.background = new Background();
    Director.base = new Base();
    Director.bird = new Bird();
    Director.gameover = new Gameover();
    Director.message = new Message();
    Director.grade = new Grade();

    Director.scene = new StartScene();
    Director.scene.start_render(Director.MSPF);
    Director.scene.start_run(Director.MSPF);

});