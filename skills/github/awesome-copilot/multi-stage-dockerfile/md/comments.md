# multi-stage-dockerfile (`github/awesome-copilot/multi-stage-dockerfile`)

## comments

- user: 前端新手, category: 坑, comment: COPY . . 写在 npm install 前面，改一行代码就重装全部依赖。把装依赖放前面，现在重建只要几秒。
- user: 后端老兵, category: 妙用, comment: 在 builder 后加个 test 阶段跑完单测再拷产物进 runtime，测试工具一点不进线上镜像，CI 里 build 即验证。
- user: 运维老哥, category: 注意, comment: 加了 USER 非 root 后挂载卷全报权限错。用 COPY --chown 建镜像时就把属主设好，别指望运行时 chmod。
- user: 转行自学的新手, category: 坑, comment: 贪小换 alpine，两个要原生编译的包全装不上，查半天是 musl 的锅。换 3.11-slim 一次通过。
- user: 独立开发者, category: 妙用, comment: 只拆了 builder/runtime 两段，镜像从 1.1G 瘦到 130M，推送快了十倍。记得只拷产物，别整目录搬。
- user: 安全工程师, category: 注意, comment: tag 别写 latest，半年后重建环境变了直接报错，锁具体小版本；运行阶段能上 distroless 就尽量上。
