---
title: Evolucao de schema
description: Evolua modelos de documentos na TerraScale com operacoes de schema em vez de codigo manual de atualizacao de storage.
---

A TerraScale usa operacoes de schema para a evolucao normal de modelos. Os SDKs enviam a intencao do modelo tipado, Server planeja o diff de schema e TerraBase continua sendo o document store tipado atras do limite do produto.

O fluxo comum e:

- inferir ou definir um modelo tipado no SDK TypeScript ou C#
- executar um plano de schema para revisar seguranca, campos afetados, acoes geradas e escopo de reescrita
- aplicar mudancas aditivas seguras automaticamente em ambientes locais e de desenvolvimento
- exigir aprovacao explicita para mudancas guarded em producao
- manter formatos antigos e novos legiveis enquanto reescritas em background rodam
- inspecionar estado, progresso, falhas e versoes de schema pela API, SDK e dashboard

Isso substitui o padrao antigo em que o codigo da aplicacao era responsavel por upgrades rotineiros de storage. Usuarios nao deveriam escrever jobs de mapeamento, jobs de indices ou scripts de colecoes para campos aditivos normais, defaults, indices ou transforms de compatibilidade seguros.

## Modelo atual

Mudancas de schema sao representadas como operacoes duraveis de propriedade do Server. Cada operacao registra o diff planejado, safety class, versao de schema alvo, fase, progresso e qualquer mensagem de falha. A TerraScale armazena esses registros no TerraBase e retoma trabalho recuperavel apos restart, exceto quando a operacao esta pausada explicitamente.

Mudancas seguras podem terminar imediatamente. Mudancas guarded passam por fases como expanding, backfilling, cutover, cleanup e done. Operacoes com falha podem ser repetidas a partir da versao de schema alvo persistida.

## Mudancas seguras

Mudancas que a TerraScale pode aplicar sem codigo manual de atualizacao de storage:

- adicionar um campo opcional
- adicionar um campo obrigatorio com default
- adicionar um indice ou access path gerado
- ampliar um tipo compativel
- adicionar paths JSON/map selecionados por auto-indexing
- adicionar um campo unique depois de validar duplicados e fazer backfill de reservas

Use schema plan primeiro quando precisar revisar a operacao exata antes de aplicar.

## Mudancas guarded

Algumas mudancas exigem confirmacao porque a TerraScale so consegue preservar corretude com uma operacao explicita:

- rename com alias
- backfill de campo obrigatorio
- mudancas de indice ou access path em colecoes grandes
- backfill de reservas de unique constraint
- transforms de compatibilidade para formatos armazenados antigos

Mudancas guarded em producao exigem `productionApprovalId` antes de aplicar.

## Mudancas bloqueadas

A TerraScale rejeita mudancas quando nao consegue inferir uma intencao segura:

- remocao destrutiva de campo sem um plano deliberado de substituicao
- rename ambiguo sem alias
- estreitamento de tipo com possivel perda de dados
- mudancas de identidade de documento ou placement que exigem decisao de produto
- reescritas semanticas que exigem logica de negocio

Nesses casos, use uma reescrita de dados em etapas como trabalho de aplicacao ou operacoes. Mantenha-a idempotente, observavel, limitada por tenant e testada com dados representativos antes de aplica-la a registros live.

## Observabilidade de operacoes

Acompanhe evolucao de schema por historico de operacoes e versoes:

- versao de schema atual e alvo
- safety class e acoes de storage geradas
- collection e campos afetados
- percentual de progresso e fase
- mensagem de falha e guia de retry/resume
- IDs de audit e correlacao de request

## Boas praticas

1. Trate as definicoes de modelos do SDK como a fonte de intencao de schema.
2. Use a saida do schema plan em revisoes e deploys.
3. Prefira mudancas aditivas e defaults antes de limpeza destrutiva.
4. Mantenha leituras de compatibilidade ate as reescritas em background terminarem.
5. Use campos unique tipados apenas quando validacao de duplicados e backfill de reservas puderem completar.
6. Reserve reescritas manuais para mudancas destrutivas ou semanticas que a TerraScale nao consiga inferir.

## Relacionado

- [Validation](/reference/validation/)
- [Data Models](/reference/data-models/)
- [Best Practices](/reference/best-practices/)
- [TQL API](/reference/api/tql/)
