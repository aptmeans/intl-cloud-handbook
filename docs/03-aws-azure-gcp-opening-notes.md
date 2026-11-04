---
title: AWS、Azure、Google Cloud 开户时容易忽略的事
description: 欧美三家云开户后最常卡住的地方是配额和审批：AWS 新账号配额低，Azure OpenAI 要单独申请，Vertex AI 也有地区和配额限制。
---

# AWS、Azure、Google Cloud 开户时容易忽略的事

账号开出来只是第一步。真正让项目延期的，往往是开完才发现想用的机型起不来、模型调用不了。三家各有一个要提前准备的地方。

## AWS：新账号的配额普遍偏低

新开的 AWS 账号，EC2 的 vCPU 配额、GPU 实例配额默认都很低，有些 GPU 机型干脆是 0。要用大规格或 GPU 实例，需要在 Service Quotas 里提交提额申请，批不批、批多少由 AWS 决定，新账号往往要有一段时间的正常使用记录。官方说明见 [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)。

建议的顺序：

1. 账号到手先跑一些小规格实例，正常用一段时间；
2. 提额申请写清楚用途、区域、需要的数量；
3. 不要一上来就申请很大的数量，被拒后再申请会更慢。

AWS 在云大哥可以网页自助办理，充值时凭交付的 AWS 登录账号核验，详细说明在 [AWS 开户与充值](https://www.clouddage.com/platforms/aws) 页。

## Azure：订阅类型和 OpenAI 配额要先想清楚

Azure 的「开户」其实是开订阅，订阅类型不同，能开的服务和计费方式就不同。打算用 Azure OpenAI 的，模型部署和每分钟令牌数都有配额限制，不同地区能用的模型也不一样，见 [Azure OpenAI quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)。

所以 Azure 一般不适合直接下单，先把计划用的服务、地区和月用量列出来，再由顾问评估。[Azure 开户与充值](https://www.clouddage.com/platforms/azure) 页列了需要提供哪些信息。

## Google Cloud：结算账户和项目是两层

Google Cloud 的钱挂在结算账户上，资源建在项目里，一个结算账户可以挂多个项目。充值、看账单时认的是结算账户 ID，见 [Find a Cloud Billing account ID](https://cloud.google.com/billing/docs/how-to/find-billing-account-id)。用 Vertex AI 调用 Gemini 时，同样有按地区、按模型的配额，见 [Generative AI quotas](https://cloud.google.com/vertex-ai/generative-ai/docs/quotas)。

Google Cloud 和 Azure 一样走顾问办理，办理前要准备的信息写在 [Google Cloud 开户与充值](https://www.clouddage.com/platforms/google-cloud) 页。

## 想用大模型服务的，先过一遍清单

Azure OpenAI 和 Vertex AI 的开通条件、配额和地区限制变化很快，云大哥资料库里有一份 [Azure OpenAI 与 Vertex AI 开通前核对清单](https://www.clouddage.com/resources/azure-openai-vertex-ai-checklist)，开户前对照着准备材料，能省掉来回补资料的时间。

---

上一篇：[做东南亚和香港业务：阿里云国际还是腾讯云国际](02-alibaba-or-tencent-for-asia.md) · [目录](./) · 下一篇：[账号交到手的第一个小时](04-first-hour-after-handover.md)
