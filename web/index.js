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