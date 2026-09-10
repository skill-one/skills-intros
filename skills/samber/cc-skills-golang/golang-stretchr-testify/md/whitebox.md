# golang-stretchr-testify (`samber/cc-skills-golang/golang-stretchr-testify`)

## whitebox

- 触发条件: 代码库 import 了 github.com/stretchr/testify, 或用户要求用 testify 写测试/审查现有测试
- 先判定模式: Write 模式 (新增测试或 mock) 或 Review 模式 (审计既有测试代码)
- 写断言: 用 assert.New(t)/require.New(t) 建立断言器, 入口始终是 *testing.T; require 管前置条件, assert 管结果验证
- 按需扩展: 需要隔离依赖时用 mock (嵌入 mock.Mock + m.Called()); 需要共享 setup/teardown 时用 suite (SetupTest 生命周期 + suite.Run() 启动器)
- 收尾: 用 testifylint 扫一遍, 抓参数顺序颠倒、assert/require 误用等典型错误

- 断言双轨机制: assert 记录失败后继续执行 (一次看全部失败), require 直接 t.FailNow() 终止 (防 nil 空指针); 关键校验规则: 参数固定 (expected, actual) 顺序, 比较错误用 ErrorIs 走错误链而非 Equal
- mock 验证机制: 嵌入 mock.Mock 实现接口方法, m.Called() 记录调用并返回预设值; 配套匹配器 mock.Anything/AnythingOfType/MatchedBy 和调用修饰符 .Once()/.Times()/.Maybe(); 必须显式调 AssertExpectations(t) 否则期望不校验、静默通过
- 外部依赖: go 工具链和 gotests (github.com/cweill/gotests) 为必需二进制; testifylint (经 golangci-lint) 做静态检查; godig 查包文档/版本/漏洞, gopls (LSP) 定位定义与调用点, Context7 仅作文档兜底; 全程本地运行, 不依赖外部模型 API
