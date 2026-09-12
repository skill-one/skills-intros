# godot-gdscript-patterns (`wshobson/agents/godot-gdscript-patterns`)

## comments

- user: Godot 3 迁移老手, category: 注意, comment: 示例里信号是 health_changed.emit(), 这是 4.x 新语法; 照 Godot 3 教程抄 emit_signal 会直接报错, 先确认版本。
- user: 第一次做游戏的新手, category: 坑, comment: 以为正文就是全部, 自己硬写状态机卡了两天; 状态机等进阶模式其实在 references/details.md, 记得去读。
- user: 独立游戏开发者, category: 妙用, comment: 把陷阱、敌人、毒圈伤害全收进 take_damage() 一个入口, 后来加无敌帧和减伤只改这一处, 别的代码全不用动。
- user: 美术转策划, category: 妙用, comment: 速度血量都用 @export 暴露到属性面板, 配合 @export_range 限范围, 我不碰代码就能调数值试手感。
- user: 计算机系学生, category: 坑, comment: _health 的下划线只是约定不强制; 我写成 health 让别的场景直接改, 后期一重构全线报错, 老实走方法改。
- user: 前 Web 开发程序员, category: 启发, comment: 血条连 health_changed 信号刷新, 不用每帧轮询玩家状态; 思路和我写前端事件解耦一样, 全项目照此推广了。
