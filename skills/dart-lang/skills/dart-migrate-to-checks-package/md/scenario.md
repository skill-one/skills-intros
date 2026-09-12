# dart-migrate-to-checks-package (`dart-lang/skills/dart-migrate-to-checks-package`)

## scenario

旧测试要迁到 package:checks,几百个 expect 逐行改?极易踩坑:集合比较漏改会"假通过",异步断言写错直接编译失败。我按流程批量迁移,避开已知陷阱,并用编译器和测试双重验证。🧪
