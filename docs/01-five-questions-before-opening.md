---
title: 开户之前先回答五个问题
description: 选海外云平台之前，先弄清用户在哪、用哪些服务、预算怎么走、谁来维护、付款方式，答完基本就知道该开哪家。
---

# 开户之前先回答五个问题

很多人选云平台是看哪家活动力度大，开完才发现机房离用户太远，或者要用的服务那家没有。下面五个问题按顺序答一遍，通常就能把范围缩到一两家。

## 1. 你的用户主要在哪里

延迟由物理距离决定，这一条最先定。

- 用户在东南亚、港澳台、日韩：阿里云国际和腾讯云国际在这一带节点多，新加坡、雅加达、曼谷、东京、首尔都有机房。
- 用户在北美、欧洲、拉美：AWS、Azure、Google Cloud 的区域覆盖更全。
- 用户分散在全球：主站放一家，静态资源交给 CDN，比到处开机房省事。

各家公布的区域列表：[阿里云 Regions and zones](https://www.alibabacloud.com/help/en/ecs/regions-and-zones)、[腾讯云 CVM 地域与可用区](https://www.tencentcloud.com/document/product/213/6091)、[AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)。

## 2. 你要用的服务哪家有

普通的云服务器、数据库、对象存储，五家都能做。差别在专门的服务上：

| 需求 | 先看哪家 |
| :--- | :--- |
| 调用 OpenAI 系列模型 | Azure（Azure OpenAI 需要单独申请配额） |
| 调用 Gemini 等 Google 模型 | Google Cloud（Vertex AI） |
| 调用 Claude 等多家模型，配合 Lambda、S3 | AWS（Amazon Bedrock） |
| 游戏、音视频、直播加速 | 腾讯云国际 |
| 电商、跨境支付相关的配套 | 阿里云国际 |

## 3. 每月大概花多少，波动大不大

用量稳定，适合包年包月拿折扣；用量起伏大、还在试错期，按量付费更灵活。这一点会影响后面怎么充值、留多少余额，详见第 7 篇 [按量付费和包年包月怎么搭配](07-mixing-billing-methods.md)。

## 4. 谁来维护这个账号

如果团队里没人熟悉 AWS 的 IAM 或 Azure 的订阅体系，选一家控制台有中文、文档有中文的平台会少走很多弯路。阿里云国际和腾讯云国际的控制台都能切中文。

## 5. 你打算怎么付款

阿里云国际、腾讯云国际、AWS 自己注册时都要绑定能通过验证的国际信用卡。手里没有合适的卡，可以考虑通过渠道开户、用 USDT 结算。各平台在云大哥的办理方式不一样，可以先看一眼 [支持平台一览](https://www.clouddage.com/platforms)：阿里云国际、腾讯云国际和 AWS 能在网页上自助下单，Azure 和 Google Cloud 要先和顾问确认方案。

---

[目录](./) · 下一篇：[做东南亚和香港业务：阿里云国际还是腾讯云国际](02-alibaba-or-tencent-for-asia.md)
