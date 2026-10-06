---
title: Alfa Público
description: O que o Alfa Público da TerraScale inclui hoje, onde estão os limites atuais e o que ainda está sendo desenvolvido.
sidebar:
  order: 2
---

O Alfa Público é o estágio atual de lançamento da TerraScale. A plataforma está pronta para avaliação real e cargas de trabalho iniciais, mas alguns recursos ainda estão evoluindo enquanto a equipe reúne dados de uso e feedback.

## O que Alfa Público Significa

Alfa Publico significa que a plataforma principal esta funcional e disponivel para os usuarios hoje. Voce pode criar com ela, testar padroes de trafego reais e avaliar a API publica, SDKs, dashboard, SQL, Queue, Auth e Payments suportados. Ao mesmo tempo, este estagio ainda e moldado pelo feedback, entao limites podem mudar e algumas provas ao vivo de Stripe, provedores de email, provedores OAuth e producao ainda estao a caminho.

Para o contexto mais amplo do roteiro, veja o [Roteiro Público](/roadmap/).

## Recursos Disponíveis

- Suporte a API HTTP JSON versionada `/api/v1`
- Acesso a interface TQL
- Suporte ao SDK C#
- Suporte ao SDK TypeScript
- Fluxos do dashboard apoiados pela API publica e pelos SDKs
- Colecoes tipadas e operacoes de schema apoiadas pelo TerraBase
- Fluxos locais/default-CI de Queue, Auth e Payments
- Modelo de regioes de lancamento para `gru`, `sfo` e `fra`

Se você quiser começar a usar a plataforma agora, veja o [guia de Primeiros passos](/guides/getting-started/).

## Limites Atuais

- A validacao atual de regioes de lancamento se limita a `gru`, `sfo` e `fra`
- Limites de taxa se aplicam durante o Alfa Público
- Fluxos ao vivo de Stripe, provedores de email e provedores OAuth exigem credenciais e configuracao de webhooks/contas fornecidas pelo operador
- Evidencia de interrupcao multi-regiao similar a producao continua sendo bloqueador de release

Esses limites ajudam a equipe a manter a plataforma atual confiável enquanto o Alfa Público se expande.

## O que Ainda Não Está Disponível

Os itens abaixo estão planejados, mas ainda não fazem parte da versão atual do Alfa Público:

- Prova completa de interrupcao multi-regiao TerraBase/NATS/Fabric similar a producao
- Prova de Sentry ao vivo e Alertmanager de producao
- Prova de provedor OAuth/IdP ao vivo
- Prova em sandbox ao vivo de pagamentos com Stripe e provedores de email
- Cache automatico

Veja o [Roteiro do Alfa Público](/roadmap/public-alpha-roadmap/) para conhecer o próximo conjunto de prioridades.

## Como Enviar Feedback

As prioridades do Alfa Público são fortemente influenciadas pelo feedback real dos usuários. Entre na [comunidade do Discord](https://discord.gg/8Zr2Nw9g) para compartilhar ideias, relatar dificuldades e discutir seu caso de uso com a equipe.

Para suporte direto ou feedback sobre o roteiro, envie um e-mail para [support@terrascale.tech](mailto:support@terrascale.tech).
