# docker-expert (`sickn33/agentic-awesome-skills/docker-expert`)

## comments

- user: 第一次容器化的前端, category: 坑, comment: 我拿它写 Kubernetes 部署文件, 它直接停下让我去找 kubernetes-expert。镜像和 Compose 它很专业, 但编排不归它管, 别问错对象。
- user: 后端老兵, category: 妙用, comment: 它把我的 COPY . . 挪到依赖安装之后, 改一行代码不再全量重装 npm 包, 构建 8 分钟变 1 分钟, 调整层顺序这招是真值钱。
- user: 运维老哥, category: 注意, comment: 按它的方案加固后容器用 UID 1001 跑, 挂载宿主机目录前记得 chown 成 1001, 不然应用写日志直接 permission denied, 我排查了半天。
- user: 独立开发者, category: 妙用, comment: 以前把 API key 写在 ARG 里, docker history 一翻就露。它教我改用 --mount=type=secret 构建时注入, 镜像层里彻底查不到痕迹。
- user: 刚装 Docker 的新手, category: 注意, comment: 它收尾会真跑 docker build 验证, 前提是本机 Docker Desktop 得先启动。没开守护进程时最后一步全是报错, 先确认环境再开工。
- user: 两人小团队技术负责人, category: 启发, comment: 用 target 区分 dev/prod 后, 本地和线上跑同一份镜像, 「我电脑上是好的」这种扯皮直接消失, 现在新项目我都要求这么干。
