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

    /**分数 */
    static grade = null;
};