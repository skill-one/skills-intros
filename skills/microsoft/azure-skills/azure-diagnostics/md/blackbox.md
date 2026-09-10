# azure-diagnostics (`microsoft/azure-skills/azure-diagnostics`)

## blackbox

**function**: 你告诉我 Azure 云上哪个服务出了什么故障,我帮你查清原因并给出可执行的修复方案。

- input: 「我的 App Service 网站突然很卡,CPU 逼近 100%」+ Azure 资源名, output: 一份诊断结论:CPU 飙高的根因(如某次部署引发、流量激增、内存泄漏)+ 对应的处置建议
- input: 「AKS 容器集群里 Pod 一直 Pending 或反复崩溃重启」, output: 定位结果:是镜像拉取失败、资源不足还是配置错误,并附每一步的修复操作
- input: 「虚拟机 SSH/RDP 连不上,一直超时」, output: 检查结论:是 Azure 平台故障、安全规则(NSG,相当于云上的防火墙)拦截还是账号凭据问题,以及恢复连接的具体步骤
