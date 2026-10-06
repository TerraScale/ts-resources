---
title: Preços e medição
description: Regras de armazenamento e unidades de operação da Alfa Pública.
sidebar:
  order: 7
---

A TerraScale mede o armazenamento entre regiões e o trabalho de banco de dados em unidades de operação. A Alfa Pública usa limites rígidos por plano e não cobra transferência de saída. A cobrança, os métodos de pagamento e o histórico pertencem à Organização, não diretamente ao User.

## Armazenamento entre regiões

O uso de armazenamento é a soma dos bytes não comprimidos dos documentos guardados em cada região selecionada. Um conjunto de 100 MB armazenado em três regiões consome 300 MB. O limite de 1 GB do Developer usa o mesmo cálculo.

As exibições de armazenamento por banco de dados são estimativas. A TerraScale aplica o limite ao uso exato dos projetos da organização.

## Unidades de operação

Uma unidade de operação cobre cada bloco iniciado de 4 KiB, ou 4.096 bytes, de dados de documentos processados por uma operação faturável.

- Leituras cobram os bytes de cada documento retornado pela região que atendeu a solicitação.
- Uma consulta bem-sucedida sem resultados custa uma unidade.
- Criações, substituições e atualizações cobram as unidades do documento uma vez em cada região selecionada.
- Um lote arredonda cada documento separadamente e depois soma as unidades.
- Uma exclusão custa uma unidade por região selecionada.

### Arredondamento

Um documento de 1 byte e um de 4.096 bytes custam uma unidade. Um documento de 4.097 bytes custa duas.

### Escrita multirregional

Gravar um documento de 5 KiB usa duas unidades por região. Com três regiões selecionadas, a gravação custa seis unidades. A replicação não adiciona outra cobrança.

### Lotes

Um lote grava documentos de 1 KiB, 4 KiB e 5 KiB em duas regiões. Eles são arredondados para uma, uma e duas unidades por região. O lote custa oito unidades: `(1 + 1 + 2) × 2`.

### Consultas e exclusões

Uma consulta sem documentos custa uma unidade. Três documentos de 2 KiB custam três unidades porque cada um é arredondado separadamente. Excluir um documento de um banco com três regiões custa três unidades.

## Trabalho não faturado

Solicitações rejeitadas, falhas do servidor, novas tentativas internas, indexação, backups, monitoramento, reparos internos e a replicação posterior à multiplicação regional não adicionam unidades. A transferência de saída aparece nos relatórios, mas não é cobrada durante a Alfa Pública.

## Ao atingir um limite

A TerraScale rejeita novos trabalhos faturáveis que ultrapassariam um limite. Leituras, exportação de projetos, exclusão e redução de uso continuam disponíveis. Atingir um limite não apaga os dados armazenados.

Consulte [Planos da Alfa Pública](/reference/plans/) para ver os limites mensais.
