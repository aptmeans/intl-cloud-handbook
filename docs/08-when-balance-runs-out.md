---
title: 余额见底以后会发生什么
description: 海外云账号欠费后通常会经历提醒、停机、释放几个阶段，按量和包月资源受的影响不同，以及停机后怎么尽快恢复。
---

# 余额见底以后会发生什么

欠费不会立刻删数据，但每个阶段都有时间限制，拖得越久越麻烦。了解这个过程，才知道还剩多少时间补救。

## 一般会经历的几个阶段

1. **预警**：余额快不够时，平台发邮件、短信或站内信。
2. **欠费**：余额变成负数，按量资源开始受限。
3. **停机**：按量付费的实例被停止，公网访问中断，数据一般还在。
4. **释放**：停机一段时间后仍未补缴，资源和数据可能被释放，释放后无法恢复。

每个阶段之间隔多久，各家、各产品不一样，也会调整，以官方文档为准：

- 阿里云国际 ECS：[Overdue payments](https://www.alibabacloud.com/help/en/ecs/overdue-payments)
- 腾讯云国际 CVM：[Overdue Payments](https://www.tencentcloud.com/document/product/213/2181)
- Azure 订阅被停用后恢复：[Reactivate a disabled Azure subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-disabled)

## 按量和包月受的影响不同

包年包月的资源在到期前不受余额影响，到期没续费才会进入停机流程。按量资源是实时扣费的，余额一欠，最先受影响的就是它们。所以混用两种计费方式的账号，看到欠费提醒时先关注按量资源。

## 停机了怎么尽快恢复

1. 先补足欠费金额，再多充一些，避免刚恢复又欠费；
2. 补缴后，有的实例会自动启动，有的需要手动启动，进控制台确认一下；
3. 检查公网 IP 是否还是原来那个，域名解析要不要改；
4. 恢复后把余额预警调高一点。

如果账号是被风控或违规处理停用的，不是欠费，处理方式完全不同，可以先看 [云账号被停用了怎么办](https://www.clouddage.com/resources/cloud-account-suspended-what-to-do) 分清是哪种情况。

## 平时就避免走到这一步

- 余额预警设成够撑一到两周的数；
- 包月资源打开自动续费，或者在日历上记下到期日；
- 充值走熟悉的流程，通过云大哥开的账号可以直接在 [充值页](https://www.clouddage.com/top-up) 填账号标识办理。

---

上一篇：[按量付费和包年包月怎么搭配](07-mixing-billing-methods.md) · [目录](./)
