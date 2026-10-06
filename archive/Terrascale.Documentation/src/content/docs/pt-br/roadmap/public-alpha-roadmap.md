---
title: Roteiro do Alfa Público
description: Melhorias planejadas para a TerraScale durante o Alfa Público, incluindo automação de desempenho e limites maiores por banco de dados.
sidebar:
  order: 3
---

Esta página cobre as principais melhorias planejadas durante o Alfa Público. O foco é direto: tornar a TerraScale mais rápida de adotar, mais fácil de ajustar e mais capaz sob cargas de trabalho reais.

Para a visão completa do produto, veja o [Roteiro Público](/roadmap/). Para o estágio de lançamento atual, veja [Alfa Público](/roadmap/public-alpha/).

## Visão Geral

O Alfa Publico ja pode ser usado, mas varias melhorias importantes ainda estao por vir. O roteiro desta etapa esta centrado em automacao de desempenho, evolucao automatica de schema, melhor comportamento de cache e prova similar a producao para o modelo de regioes de lancamento suportado.

## Recursos Planejados

### Indexação Automática

A TerraScale ja tem cobertura default-CI e deterministica para candidatos de auto-indexing informados por workload, incluindo padroes repetidos de consulta sobre propriedades JSON. O trabalho restante e evidencia DevHost/runtime mais ampla, ajuste de politica com workloads reais e visibilidade operacional que explique por que um indice gerado foi selecionado.

### Cache Automático com Invalidação

O cache automático de resultados de consulta está planejado para melhorar o desempenho de leitura sem exigir que as equipes gerenciem manualmente cada decisão de cache. A invalidação de cache faz parte do design para manter os resultados em cache alinhados às mudanças nos dados subjacentes.

### Evolução Automática de Schema

A TerraScale faz com que mudancas seguras de modelo parecam automaticas pelo SDK enquanto o armazenamento no TerraBase continua tipado e sustentado por operacoes de schema internamente. O SDK e o control plane inferem mudancas seguras em colecoes e indices, acompanham versoes de schema e executam rewrites em background para que desenvolvedores nao precisem escrever codigo de upgrade de armazenamento para evolucao comum de modelos.

### Prova de regioes de lancamento similar a producao

O modelo de regioes de lancamento e `gru`, `sfo` e `fra`. O roteiro inclui prova de interrupcao TerraBase/NATS/Fabric similar a producao, reconciliacao de Vault ao vivo, entrega de Sentry ao vivo e roteamento de Alertmanager de producao antes de afirmar readiness multi-regiao estavel.

### Controles Manuais de Cache

Junto com o cache automático, a TerraScale planeja adicionar controles manuais de cache para equipes que querem um controle mais rígido sobre o comportamento. Isso inclui remoção LRU e gerenciamento explícito de cache para cargas de trabalho que precisam de ajustes previsíveis.

## Observações sobre o Cronograma

Este roteiro é priorizado pelo feedback dos usuários e por padrões reais de uso. Ainda não existem datas públicas fixas, e a ordem pode mudar à medida que a equipe aprende mais com cargas de trabalho semelhantes à produção durante o Alfa Público.

## Solicite um Recurso

Quer influenciar o roteiro? Entre na [comunidade do Discord](https://discord.gg/8Zr2Nw9g) e compartilhe o que sua carga de trabalho precisa em seguida.

Para solicitações diretas ou perguntas de acompanhamento, envie um e-mail para [support@terrascale.tech](mailto:support@terrascale.tech).
