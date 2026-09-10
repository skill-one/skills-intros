# git-commit (`github/awesome-copilot/git-commit`)

## comments

- user: 前端新手, category: 坑, comment: 改了 6 个文件只 add 了 1 个，结果提交信息只描述那一个。有 staged 就只看 staged，提交前要么全 add，要么明确说提交哪些文件。
- user: 开源库维护者, category: 妙用, comment: 删废弃接口时它主动写成 feat! 带感叹号。我的发版脚本靠这个标记自动升 major 版本，再没漏标过 breaking change。
- user: 后端老兵, category: 注意, comment: 提交被 pre-commit hook 拦下后它不改历史，修好会新建 commit。若 hook 自动格式化了文件，记得让它先重新 add，否则新提交会漏掉格式化改动。
- user: 独立开发者, category: 坑, comment: 它认得 .env、私钥这类常见敏感文件，但 secrets.py 这种自命名的不一定拦得住。含密钥的文件提交前自己过一遍 git status。
- user: 技术组长, category: 启发, comment: 群里强调提交规范三年没人听。用它从 diff 推 type 和 scope，描述统一祈使句，提交历史终于一眼能懂。规范靠工具比靠自觉靠谱。
- user: 接活的自由程序员, category: 妙用, comment: 一次混改了新功能和 bug 修复，它建议用 git add -p 分块暂存拆成两个 commit。现在每个提交都是单一变更，回滚不再误伤。
