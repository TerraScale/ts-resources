---
title: Como escolher um plano
description: Escolha entre Developer, Starter, Pro e Enterprise indisponível usando o catálogo da Alfa Pública.
sidebar:
  order: 12
---

Use este guia com a lista pública de planos em `GET /api/v1/pricing/plans`. O catálogo abaixo é o contrato da Alfa Pública. A resposta da API é a fonte autoritativa se o catálogo publicado mudar. Cada User recebe uma Organização Personal não transferível. Seus métodos de pagamento, identidade de cliente Polar, assinaturas, testes, histórico de cobrança, Projects e associações pertencem à Organização, não diretamente ao User.

## Escolha alvo durante o onboarding

O fluxo alvo de autorregistro começa com a verificação de identidade e e-mail já contada como uma etapa concluída. Depois, cria a primeira Organization, o primeiro Project e a primeira Database lógica e verifica um cartão de pagamento para controle de abuso no cadastro. A verificação não cria cobrança, assinatura, teste pago nem renovação automática. Em seguida, o User escolhe entre continuar sem plano pago e sem renovação automática, mantendo a franquia Developer, ou selecionar Starter ou Pro com renovação automática mensal e os primeiros 30 dias sem cobrança quando a Organization for elegível. No texto do onboarding, "sem plano pago" é a opção apresentada ao cliente e Developer é a franquia gratuita interna. O onboarding de Users convidados continua separado. Esse objetivo ainda não foi publicado e é acompanhado pelo [issue 30 do TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30).

## Escolha rápida

| Plano | Preço e disponibilidade | Quando usar |
| --- | --- | --- |
| `Developer` | US$ 0, não vence | Você está explorando a TerraScale ou criando um protótipo dentro dos limites de Developer. |
| `Starter` | US$ 5 mensal | Você precisa de uma franquia paga menor e de um objetivo de suporte. |
| `Pro` | US$ 25 mensal | Você precisa de franquias maiores de projetos, armazenamento e unidades de operação. |
| `Enterprise` | Base de suporte mensal de US$ 500 mais uso medido, indisponível durante a Alfa Pública | Você precisa de um plano contratual quando os termos forem aprovados. |

## Limites que costumam decidir

- **Projetos e bancos de dados**: Developer permite 1 Project e 3 Databases. Starter permite 5 Projects e 10 Databases. Pro permite 25 Projects e 50 Databases.
- **Armazenamento**: Developer permite 1 GB entre as regiões selecionadas. Starter permite 5 GB. Pro permite 50 GB.
- **Unidades de operação**: Developer permite 10.000 por mês. Starter permite 1.000.000. Pro permite 10.000.000.
- **Membros**: Developer permite 3 membros. Starter permite 5. Pro permite 25.
- **Regiões**: todos os planos disponíveis podem selecionar São Paulo, San Francisco e Falkenstein.

## Conselhos práticos

1. Comece no **Developer** enquanto valida autenticação, repositórios, TQL e fluxos de filas.
2. Escolha **Starter** quando as franquias do Developer não forem mais suficientes.
3. Escolha **Pro** quando precisar de franquias maiores ou do objetivo de suporte em um dia útil.
4. Considere **Enterprise** indisponível até que seu contrato e suas tarifas de uso sejam aprovados.

Quando uma franquia rígida é atingida, novos trabalhos faturáveis são rejeitados. Leituras, exportação de projetos, exclusão e trabalhos que reduzem o uso continuam disponíveis. A franquia mensal de unidades de operação é renovada no início do próximo mês-calendário.

Uma Organização paga elegível recebe os primeiros 30 dias sem cobrança depois que um Organization Owner seleciona explicitamente Starter ou Pro e aceita a renovação automática mensal. A verificação do cartão para o cadastro não inicia esse período. A elegibilidade do teste é durável; alterações no cartão, proprietário ou associação não a restauram. O cancelamento interrompe a renovação ao fim do período pago. Uma renovação com falha recebe sete dias de tentativas de pagamento com acesso normal e depois um período de somente leitura de 30 dias. O pagamento durante qualquer um dos períodos restaura o plano anterior e o acesso aos dados. O período de somente leitura permite ler, reduzir o uso, excluir e exportar, e bloqueia novos trabalhos faturáveis. Ao fim, a TerraScale elimina o Customer content e as cópias que o cliente pode restaurar. Mantém apenas os registros mínimos de Organização, cobrança, segurança, Audit e recibo de exclusão exigidos pela política. A Organização vazia pode ser reativada mais tarde, mas os dados excluídos não podem voltar e uma Organização inadimplente não é rebaixada para Developer.

A exclusão voluntária do User é separada do tratamento de falha de pagamento. Ela inicia uma janela cancelável de sete dias, revoga sessões imediatamente, interrompe cobranças e preserva a exportação durante a janela. Ao concluir, exclui a Organização Personal, associações e Customer content, mantendo somente os registros legalmente exigidos e um recibo de exclusão. Uma exportação completa de Project é um pacote ZIP versionado com um manifesto versionado, hashes de integridade e um arquivo JSON delimitado por novas linhas para cada Repository. Inclui Database, Environment, Repository, Document, índices e metadados de versão, nunca inclui segredos de credenciais e não é um backup nem um snapshot de Database. A entrega é um download autenticado e revogável disponível por 24 horas ou um destino presigned de AWS S3 de curta duração fornecido pelo cliente. A TerraScale não armazena as chaves de acesso AWS do cliente.

## Suporte

Developer recebe documentação e suporte por e-mail de melhor esforço. Starter tem como objetivo responder em dois dias úteis. Pro tem como objetivo responder em um dia útil. Esses objetivos não garantem resolução nem são um SLA de disponibilidade. O suporte Enterprise está indisponível durante a Alfa Pública.

Os preços dos planos não variam conforme a região selecionada. A medição de unidades de operação usa o contrato de blocos iniciados de 4 KiB documentado em [Preços](/reference/pricing/).

## Próximos passos

- [Referência de planos](/reference/plans/)
- [Cobrança](/reference/billing/)
- [Primeiros passos](/guides/getting-started/)
