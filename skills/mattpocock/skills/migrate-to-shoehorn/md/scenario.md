# migrate-to-shoehorn (`mattpocock/skills/migrate-to-shoehorn`)

## scenario

深夜写测试:只用到 body.id,却被迫硬造 20 个字段,否则 TS 报错;用 as 强转又被 review 打回。我帮你换成 shoehorn:fromPartial 只传需要的,fromAny 故意传错的也放行,类型全绿 ✅
