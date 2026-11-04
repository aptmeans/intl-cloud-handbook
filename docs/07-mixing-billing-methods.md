---
title: 按量付费和包年包月怎么搭配
description: 按量付费和包年包月各适合什么资源，怎么组合能让海外云账单稳定，以及余额该留多少、怎么设预算提醒。
---

# 按量付费和包年包月怎么搭配

同样一台机器，按量付费和包年包月的月成本可能差不少。但全选包月也不对，用不上的资源照样要付钱。比较实际的做法是按资源的「稳定程度」分开处理。

## 两种方式的区别

| | 按量付费 | 包年包月 |
| :--- | :--- | :--- |
| 什么时候扣钱 | 用完按小时或按秒结算 | 购买时一次付清 |
| 单价 | 较高 | 时间越长折扣越多 |
| 能不能随时释放 | 能，释放后停止计费 | 到期前释放通常要按规则退款或不退 |
| 对余额的要求 | 要一直有余额，不然会停机 | 买完以后不依赖余额 |

官方定义见阿里云 [Pay-as-you-go](https://www.alibabacloud.com/help/en/ecs/pay-as-you-go-1) 和 [Subscription](https://www.alibabacloud.com/help/en/ecs/subscription)，其他几家逻辑类似。

## 一个常见的组合

- 数据库、主站服务器这类 7×24 小时跑的：包年包月。
- 测试环境、临时压测、活动期间加的机器：按量付费，用完就释放。
- 流量、对象存储请求这类没法预估的：只能按量，靠预算提醒兜底。

更多场景的对比可以看 [按量付费和包年包月怎么选](https://www.clouddage.com/resources/pay-as-you-go-vs-subscription)。

## 余额留多少

有按量资源的账号，余额最好够撑 1 到 2 周，给自己留出充值的时间。USDT 付款虽然快，周末或者人在外面的时候也可能来不及。

## 一定要设的提醒

- 余额低于某个数时提醒：各家费用中心都有余额预警；
- 月度预算提醒：[AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)、[Azure budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)、[Google Cloud budgets](https://cloud.google.com/billing/docs/how-to/budgets)。

账单规划方面的其他文章，集中放在云大哥资料库的 [账单规划专题](https://www.clouddage.com/resources/topic/billing-planning)。

---

上一篇：[充值前后各核对一遍](06-top-up-check-before-and-after.md) · [目录](./) · 下一篇：[余额见底以后会发生什么](08-when-balance-runs-out.md)
