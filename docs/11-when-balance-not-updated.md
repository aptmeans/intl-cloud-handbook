---
title: 付款成功但余额没动：找客服之前自己先查什么
description: 订单已付、控制台余额不变时，按订单、链上哈希、账号标识和五家云费用入口自查，准备好材料再联系，避免重复付款。
---

# 付款成功但余额没动：找客服之前自己先查什么

钱已经从交易所或钱包转出去了，订单也可能显示付过了，可是打开阿里云国际、腾讯云国际或 AWS 控制台，余额或额度还是原来的数。这时候最容易做的两件错事是：再付一笔，或者立刻把密码截图发给客服。先自己过一遍下面几项，多数情况能分清是延迟、看错位置，还是真的需要人工介入。

## 先分清三层状态

| 层 | 看哪里 | 说明 |
| :--- | :--- | :--- |
| 办理方订单 | 订单状态、应付金额、收款网络与地址 | 订单未完成，云侧不会有入账 |
| 链上（USDT） | 交易哈希是否 Confirmed、收款地址与金额 | 发出去 ≠ 已被订单确认 |
| 云厂商控制台 | 费用中心里对应字段 | 字段名各家不同，看错等于没查 |

云大哥订单页各字段的含义见 [看懂云大哥订单页](https://www.clouddage.com/resources/how-to-read-order-page)；专门讲「付完款余额没变」的逐步清单见 [付完款控制台余额还没变](https://www.clouddage.com/resources/top-up-paid-but-balance-unchanged)。

## 自己先查的五件事

1. **订单是不是已经完成。** 仍是待付款、待确认时，不要去纠结控制台数字。
2. **哈希、地址、金额是否与订单一致。** 网络选错（例如本应 TRC20）时，钱不会进这份订单。USDT 操作步骤可参考 [第一次用 USDT 付款](https://www.clouddage.com/resources/buy-usdt-and-withdraw-trc20)。
3. **登录的是不是充值目标账号。** 对照交付信息里的 UID / 账号 ID / AWS Account ID，方法见 [充值前先找准账号标识](https://www.clouddage.com/resources/find-account-id-before-top-up)。
4. **费用入口和字段是否找对。**
   - 阿里云国际：Expenses and Costs → Billing Account；区分现金余额与可用额度。官方说明：[Billing account overview](https://www.alibabacloud.com/help/en/user-center/fund-account-overview)
   - 腾讯云国际：Billing Center → Account Info / Transactions；不同充值方式到账时间不同，见 [Top-up Process Instructions](https://www.tencentcloud.com/document/product/555/11319)
   - AWS：Billing → Credits，新 credit 显示可能有延迟，见 [Applying AWS credits](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-credits.html)
   - Azure：Cost Management + Billing，选对 billing scope 后看 Azure credits，见 [Track Azure credit balance](https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/credits/mca-check-azure-credits-balance)
   - Google Cloud：选对 Cloud Billing account 再查入账
5. **当前登录身份有没有财务权限。** 普通子用户经常进不了计费中心，换有权限的账号再看。

## 联系办理方时带什么

不要只说「余额没变」。准备这三样：

- 订单号（以及查询码，若有）；
- 链上交易哈希；
- 费用中心截图（可对账号标识打码），并注明查看时间。

重复付款只会让对账更乱。渠道受理范围以办理方说明为准，例如云大哥 [充值说明](https://www.clouddage.com/top-up) 一般只处理在本渠道开通的账号。

充值前后的常规核对习惯，还可以对照本系列第 6 篇：[充值前后各核对一遍](06-top-up-check-before-and-after.md)。

---

上一篇：[云厂商的通知邮件该发给谁](10-who-gets-the-emails.md) · [目录](./)
