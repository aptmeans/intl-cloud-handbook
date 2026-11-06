---
title: 几个人一起用一个云账号，权限怎么分
description: 团队共用海外云账号时，按「谁管钱、谁动资源、谁只看」拆分子用户和权限，以及有人离开时要收回哪些东西。
---

# 几个人一起用一个云账号，权限怎么分

第 4 篇说过日常操作要用子用户。这一篇接着讲人多了以后的事：三五个人同时用一个账号，谁该有什么权限，人走了怎么收。

## 先按职责分三类人

不必一开始就细到每个产品，先粗分三类，够大多数小团队用：

| 角色 | 需要做的事 | 不该有的权限 |
| :--- | :--- | :--- |
| 管钱的人 | 看账单、下载发票、看余额、处理充值 | 创建或删除服务器 |
| 动资源的人 | 开关实例、改安全组、部署 | 改别人的权限、动付款方式 |
| 只看的人 | 查监控、看日志、排查问题 | 任何写操作 |

主账号本身不属于这三类。它只留给一个负责人，用来管理子用户和处理只有主账号能做的事，平时不登录。

## 用户组，而不是一个个授权

每个平台都有「用户组」或类似概念。做法是先建好三个组，把策略挂在组上，人进哪个组就有哪个组的权限。这样新人入职只做一步「加进组」，调岗就是换组，不会出现某个人身上挂了一堆没人记得为什么加的策略。

各家对应的东西：

- 阿里云国际：RAM 用户和用户组。新建的 RAM 用户默认没有任何权限，要自己授权。官方页面：[Create a RAM user](https://www.alibabacloud.com/help/en/ram/user-guide/create-a-ram-user)
- 腾讯云国际：CAM 子用户，创建时可以直接放进用户组，或者复制已有用户的权限。注意「快速创建」出来的用户默认绑定 AdministratorAccess，给普通成员要用自定义创建。官方页面：[Creating Sub-User](https://www.tencentcloud.com/document/product/598/13674)
- AWS：IAM 用户组加托管策略；人多以后可以考虑 IAM Identity Center。官方建议见 [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- Azure：用 Azure RBAC 在订阅或资源组上分配内置角色，Reader、Contributor、Owner 是最常见的三档。见 [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
- Google Cloud：项目层面的 IAM 角色和结算账号层面的角色是分开的。项目权限见 [IAM overview](https://cloud.google.com/iam/docs/overview)，账单权限见 [Cloud Billing access control](https://cloud.google.com/billing/docs/how-to/billing-access)

策略名称各家经常调整，挑的时候在控制台搜「ReadOnly」「Billing」之类的关键词，看说明再选，不要凭印象。

## 管钱的人要单独处理

账单权限是最容易漏的一块：

- **AWS**：默认情况下 IAM 用户就算有策略也进不了账单页面，要先用 root 在账户设置里打开 IAM 用户访问账单信息的开关。说明在 [Overview of managing access permissions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html)。
- **Google Cloud**：账单挂在结算账号上，不在项目上。只给项目权限，看不到费用。
- **腾讯云国际**：余额预警的默认接收人里包括财务管理员，把管钱的人设成接收人，提醒才能到他手上。

预算和余额提醒发给谁，在 [预算提醒和余额预警：五家国际云各在哪里设置](https://www.clouddage.com/resources/budget-and-balance-alerts) 里按平台列了入口。

## 访问密钥跟着程序走，不跟着人走

部署脚本、CI 要调 API 时，单独为它建一个只开编程访问的子用户，权限只给它要用的那几个服务。不要用某个员工的子用户生成密钥给程序用，否则这个人离开时，停掉他的账号就等于停掉线上程序。

阿里云的文档也提醒，能用 STS 临时凭证的地方尽量不用长期 AccessKey。

## 有人离开时的清单

1. 停用或删除他的子用户，不要只改密码；
2. 查一下他名下有没有创建过访问密钥，一并删掉；
3. 账单、预算、余额提醒的接收人里有他的话，换掉；
4. 如果他知道过主账号密码或 MFA，主账号的密码和 MFA 都重新设置；
5. 在操作审计里看一眼他最近几天的操作，有没有不认识的资源。

第 4 条常被忽略。早期团队小，主账号密码经常是几个人都知道的。MFA 的设置方法可以看 [阿里云、腾讯云、AWS 的 MFA 设置](https://www.clouddage.com/resources/mfa-setup-alibaba-tencent-aws)。

## 账号最初是别人帮你开的

通过办理方开的账号，交付后同样适用上面所有步骤：主账号归你，子用户由你来建。如果需要别人协助处理充值，给他的是账号标识，比如 AWS 的账号 ID、阿里云和腾讯云的主账号编号，而不是任何一个能登录的用户。怎么找这些编号，见 [充值前怎么找到账号 ID](https://www.clouddage.com/resources/find-account-id-before-top-up)。

---

上一篇：[余额见底以后会发生什么](08-when-balance-runs-out.md) · [目录](./) · 下一篇：[云厂商的通知邮件该发给谁](10-who-gets-the-emails.md)
