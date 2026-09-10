# golang-data-structures (`samber/cc-skills-golang/golang-data-structures`)

## comments

- user: 后端老兵, category: 坑, comment: 我写过依赖 slice 容量翻倍时机的代码，Go 升级后直接踩雷——增长算法版本间会变。官方明确说别依赖 cap 何时扩容，我只信 len。
- user: 第一次用的新手, category: 坑, comment: 循环里 append 五十万行没预分配，接口 p99 高了一截。改成 make([]T, 0, n) 后分配次数从几千降到 1。数量可估就先给 cap。
- user: 日志处理脚本仔, category: 坑, comment: 拿 bytes.Buffer 拼大日志字符串，String() 每次都复制底层字节。换 strings.Builder 后内存明显降。Buffer 留给要边读边写的场景。
- user: 泛型工具库作者, category: 注意, comment: container/list 和 heap 存取全是 any，取出来靠类型断言，写错要运行时才炸。我在外面包了层泛型 wrapper，编译期就能拦住。
- user: 缓存服务开发, category: 妙用, comment: map 删光千万 key 内存也不还——它从不收缩，我重建新 map 整体替换才释放。Go 1.24+ 换 weak.Pointer 做缓存，GC 自动回收更省心。
- user: 带团队的 tech lead, category: 启发, comment: 复制语义那张表改变了我的 review 习惯：现在看到赋值先问一句——这是独立副本还是共享底层数组？slice/map 类 bug 少了一大半。
