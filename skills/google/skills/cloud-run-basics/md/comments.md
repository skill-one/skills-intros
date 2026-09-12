# cloud-run-basics (`google/skills/cloud-run-basics`)

## comments

- user: 第一次部署的新手, category: 坑, comment: 本地跑 Flask 用 127.0.0.1，一部署就起不来。改成监听 0.0.0.0 并读环境变量 $PORT，立刻通了。
- user: 跑批任务的后端老兵, category: 妙用, comment: 大表清洗拆成 --tasks 100 并行跑，每个任务里读 CLOUD_RUN_TASK_INDEX 领自己的分片，调度代码全省了。
- user: 第一次配权限的实习生, category: 坑, comment: 部署反复报权限错误，查了半天代码。其实是 Cloud Build 服务账号没绑 roles/run.builder 角色，先绑再发就好。
- user: 做数仓 ETL 的工程师, category: 注意, comment: job 默认只跑 10 分钟就超时。长任务记得加 --task-timeout，最长 7 天；GPU 任务上限只有 1 小时，别照抄。
- user: 从虚机搬来的老运维, category: 妙用, comment: 把 Kafka 消费者打成 worker pool 常驻跑，不用再守几台虚机怕半夜挂，拉取式消费托管给它很省心。
- user: 追求秒发的独立开发者, category: 注意, comment: 想用 --no-build 秒级发布前注意：Node/Python 带原生依赖会缺编译产物起不来，改用 --source . 编译就正常。
