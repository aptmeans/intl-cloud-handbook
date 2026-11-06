---
title: 云厂商的通知邮件该发给谁：账单、安全、运维分开收
description: 欠费、密钥泄露、资源到期这些通知默认都发给注册邮箱。按岗位把收件人拆开，并说明三家云各自的设置位置和生效前提。
---

# 云厂商的通知邮件该发给谁：账单、安全、运维分开收

账号开好以后，所有通知默认都发给注册时那个邮箱和手机。多数小团队的情况是：注册邮箱是创始人的，或者是当时帮忙办事那个人的。欠费预警、密钥泄露提醒、实例到期通知都落在同一个收件箱里，没人专门看，直到服务停了才有人发现。

这一篇只讲一件事：把几类通知分给对应的人，并确认他们真的能收到。

## 先分清三类通知

| 类型 | 典型内容 | 适合谁收 |
| :--- | :--- | :--- |
| 账单类 | 余额不足、账单生成、退款、发票 | 管钱的人 |
| 安全类 | 异常登录、访问密钥泄露、攻击告警 | 懂技术、能马上处理的人 |
| 运维类 | 实例或证书快到期、产品故障、变更通知 | 动资源的人 |

营销和活动邮件最不重要，可以只留一个人收，也可以直接关掉。

## 阿里云国际：消息中心

阿里云把通知集中在消息中心（Message Center），分成账号消息、产品消息、安全消息、异常消息、活动消息和服务消息几类。官方文档对每一类都给了建议的收件对象，比如账号消息建议财务收，安全消息建议安全工程师或运维收。

几个要注意的地方：

- 先在账号中心添加联系人，但添加后并不会自动订阅任何通知，还要到消息中心里按消息类型挑联系人。
- 联系人要先完成验证才能收邮件。
- 在没有添加联系人之前，消息中心的通知默认都发到账号的安全邮箱。
- 默认只有主账号能看和管理全部消息；子用户要进消息中心，得由主账号授予对应权限。

官方页面：[Message Center](https://www.alibabacloud.com/help/en/account/message-center/)、[Manage mailing addresses and notification contacts](https://www.alibabacloud.com/help/en/account/add-personal-addresses-and-personal-contacts)

## 腾讯云国际：消息订阅

入口在消息中心的「消息订阅」页面。每一类消息可以单独选接收渠道（站内信、邮件、短信、语音），再用「添加接收人」指定谁收。

- 接收人来自 CAM 里的用户，所以要先给对方建一个用户并绑定邮箱，对方点确认邮件之后才会收到。
- 官方说明里，欠费通知、产品到期回收通知和账号安全通知这几类重要消息，必须保持订阅站内信和邮件，不能全部关掉。
- 账单订阅是单独的：在费用中心订阅后，每月账单生成后会发概览通知；修改账单通知的接收人属于敏感操作，需要身份验证。

官方页面：[Message Subscription Management](https://intl.cloud.tencent.com/document/product/1276/73354)、[Bill subscription](https://intl.cloud.tencent.com/document/product/555/46321)

## AWS：备用联系人

AWS 的做法更直接：在账号页面的 Alternate contacts 里，可以分别设一个账单联系人、一个运维联系人和一个安全联系人。这些是在根用户邮箱之外多加的，根用户的邮箱仍然会收到全部邮件。

官方文档提到两点：

- 联系人不一定是某个具体的人，可以填一个团队的邮件组；
- 企业账号建议填公司电话和公司邮箱，而不是个人的。

这样某个人离职，改一下邮件组的成员就行，不用回到云控制台改联系人。

官方页面：[Update the alternate contacts for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html)

## 做完以后试一遍

设置完不要默认它能用。每个收件人都做一次核对：

1. 对方的邮箱和手机是否已完成平台要求的验证；
2. 邮件有没有被公司邮箱当成垃圾邮件拦截，必要时加白名单；
3. 在余额预警、预算提醒这类可以自己设阈值的地方，临时调一个很容易触发的值，看收件人能不能收到，再改回来。各家入口见 [预算提醒和余额预警](https://www.clouddage.com/resources/budget-and-balance-alerts)。

## 人员变动时

有人离职或换岗，除了回收他的登录权限，还要把他名下的通知收件人换掉。几个人共用同一个账号时，分权限的思路见 [不要把主账号发给整个团队](https://www.clouddage.com/resources/team-access-without-sharing-root-account)。

收到的如果不是普通通知，而是账号被限制或暂停的邮件，不要只回复邮件了事，处理顺序见 [云账号被暂停或受限](https://www.clouddage.com/resources/cloud-account-suspended-what-to-do)。

---

上一篇：[几个人一起用一个云账号，权限怎么分](09-team-access-split.md) · [目录](./)
