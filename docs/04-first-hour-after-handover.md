---
title: 账号交到手的第一个小时
description: 拿到海外云账号后按顺序做六件事：登录确认、改密码、开 MFA、建子用户、设预算提醒、整理凭据，附三家官方文档链接。
---

# 账号交到手的第一个小时

账号交付以后，办理方手里可能还留着初始密码。第一个小时把下面六件事做完，账号才算真正归你。

## 第 1 步：先登录一次，确认能用

用交付的登录信息进控制台，看一下账号 ID、地域列表、费用中心的余额是否和订单一致。有任何对不上的地方，先别往里放业务，保留截图问清楚。

## 第 2 步：改掉登录密码

新密码用密码管理器生成，长度 16 位以上，不要和其他网站共用。改完退出再登一次，确认新密码有效。

## 第 3 步：给主账号开 MFA

这是最重要的一步。手机装一个身份验证器应用（Google Authenticator、Microsoft Authenticator 都行），在控制台绑定。绑定时显示的密钥或恢复码要另外存一份，换手机时要用。

- 阿里云国际：[Bind an MFA device](https://www.alibabacloud.com/help/en/ram/user-guide/bind-an-mfa-device-to-a-ram-user)
- 腾讯云国际：[绑定虚拟 MFA 设备](https://www.tencentcloud.com/document/product/378/32528)
- AWS：[MFA for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html)

三家的入口位置不一样，图文步骤可以看 [阿里云、腾讯云、AWS 的 MFA 设置](https://www.clouddage.com/resources/mfa-setup-alibaba-tencent-aws)。

## 第 4 步：日常操作用子用户

主账号只用来管账单和权限，平时部署、运维用子用户：阿里云叫 RAM 用户，腾讯云叫 CAM 子用户，AWS 叫 IAM 用户。每个人一个子用户，按需要给权限，离职时停掉这个子用户就行，不用改主账号密码。参考 [Create a RAM user](https://www.alibabacloud.com/help/en/ram/user-guide/create-a-ram-user)、[腾讯云 CAM](https://www.tencentcloud.com/document/product/598/10583)、[AWS root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)。

访问密钥（AccessKey）也从子用户创建，主账号不要建。

## 第 5 步：设一个预算提醒

在费用中心设一个月度预算，花到 50%、80% 各发一次邮件。被盗用或程序跑飞时，这是最早能发现的信号。AWS 的做法见 [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)。

## 第 6 步：把凭据放在一个地方

登录地址、账号 ID、密码、MFA 恢复码、订单号，统一放进密码管理器的一条记录里。以后充值要填账号标识，直接从这里复制，不会填错。

---

上一篇：[AWS、Azure、Google Cloud 开户时容易忽略的事](03-aws-azure-gcp-opening-notes.md) · [目录](./) · 下一篇：[第一次用 USDT 付云服务的完整过程](05-first-usdt-payment.md)
