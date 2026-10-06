---
title: Plano de Conclusão de Longo Prazo
description: O roteiro guiado por aceitação para concluir a TerraScale em banco de dados, auth, queue, pagamentos, SDKs, dashboard, GitOps e operações.
sidebar:
  order: 5
headingBadge:
  text: Planejado
  variant: secondary
---


## Objetivo Final do Produto


## Marcos

| Marco | Resultado |
| --- | --- |
| Decisões e baseline | ADRs de transporte público, regiões e provedores, matrizes MVP e um comando local de E2E. |
| MVP de banco de dados | Coleções tipadas, evolução automática segura de schema, consultas, chaves de API, APIs de repositório nos SDKs e fluxos de banco de dados no dashboard. |
| MVP de Auth | Signup, login somente por e-mail com links de verificação, verificação, sessões, convites, RBAC e fundações de conta cientes de pagamento. |
| MVP de Queue | Runtime NATS JetStream, topologia NATS no Fabric, send/receive/ack/lease/DLQ/redrive, SDKs, páginas de fila no dashboard e validação de workers de email/export. |
| Fabric e multi-região | Adoção do Fabric standalone, registro de nós, placement, roteamento, topologia `gru`, `sfo`, `fra` e simulação de outage. |
| Hardening beta | Observabilidade, provedores de email, pagamentos diretos com Stripe, recursos SaaS builder de Auth e Payments, segurança, docs, exemplos e automação de release. |

## Escopo MVP

O MVP congela a menor plataforma completa que pode ser finalizada de ponta a ponta:

- APIs públicas REST HTTP com WebSockets ou SSE para fluxos em tempo real no navegador.
- Criação de banco de dados, criação de coleção, CRUD de repositório tipado, consulta, paginação, evolução segura de schema e histórico de operações.
- Signup de Auth, verificação, links de login somente por e-mail, rotação de refresh, sessões, membros de organização, convites, chaves de API e resumos de conta cientes de pagamento.
- Criação de fila, envio, recebimento, confirmação, abandono, extensão de lease, DLQ, redrive, política de retry, estatísticas e verificação NATS JetStream.
- Entrega de email independente de provedor com Mailpit local e adapters de provedor testados.
- Pagamentos diretos com Stripe, testes determinísticos de fila e webhooks, sessões de checkout, sessões de portal de billing, webhooks assinados, projeção persistida de billing e prova em sandbox vivo de Stripe bloqueada até que credenciais sejam fornecidas.
- SDKs TypeScript e C# usando a API pública HTTP.
- Endpoints e orquestração específicos do Dashboard vivem somente no projeto full-stack do Dashboard. Suas rotas de servidor usam métodos tipados do SDK TypeScript como um usuário externo comum da TerraScale.Platform, com os mesmos contratos públicos, autenticação, autorização e limites de tenant das aplicações de clientes.

## Cenários de Aceitação Final


1. Criação de conta e organização com verificação de email, login, refresh e verificações de metadados TerraBase.
2. Banco de dados e evolução de schema em `gru`, `sfo` e `fra`.
3. Validação de query e subconjunto SQL com planos de explain e erros padronizados.
4. Processamento de filas por NATS JetStream, incluindo DLQ e redrive.
5. Checkout de Stripe, webhooks assinados, assinaturas, entitlements, atualização de roles de Auth, uso, invoices e segurança de replay de eventos por meio de TerraScale Payments e TerraScale.Queue, com cobertura determinística de fila/webhooks e evidência opt-in de sandbox vivo de Stripe.
6. Fluxos avançados de autenticação por projeto com MFA, passkeys, provedores OAuth, convites, escopos de chave de API e auditoria para o produto Authentication com escopo de projeto.
7. Cobertura de rotas do dashboard com dados backend reais.
8. Topologia Fabric multi-região, roteamento, outage e recuperação.
10. Verificações de observabilidade para logs, traces, métricas, alertas e status operacional correlacionados.

## Regra Atual de Aceitação

Recursos descritos nesta página não são promessas de disponibilidade pública. Um recurso só é aceito quando implementação, SDKs, dashboard, docs e testes provam o comportamento pela superfície pública pretendida e por estado backend durável.

## Conceitos Relacionados

Leia [Conceitos da Plataforma](/guides/platform-concepts/) para entender os conceitos de produto por trás deste roteiro.
