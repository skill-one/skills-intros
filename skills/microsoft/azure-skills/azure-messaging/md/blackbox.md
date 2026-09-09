# azure-messaging (`microsoft/azure-skills/azure-messaging`)

## blackbox

**function**: 帮开发者排查 Azure 消息服务 (Event Hubs / Service Bus) 程序里的连接、认证、收发消息、锁丢失等问题, 给出原因和修复建议。

- input: 一段报错文本, 如 "The connection was inactive for more than the allowed idle timeout", output: 原因分析 + 具体的代码级修复建议 (改哪个配置、怎么改)
- input: 一句话描述现象, 如 "Event Hub 消费者程序跑着跑着就不收消息了, 重启又好了", output: 一份排查清单: 最可能的原因排序 + 每个原因对应的验证和解决办法
- input: 提问, 如 "Service Bus 处理消息时报 MessageLockLostException 怎么回事?", output: 通俗解释这个错误的含义, 并给出避免锁丢失的配置/代码改法
