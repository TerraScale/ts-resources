---
title: Evolucion de schema
description: Evoluciona modelos de documentos en TerraScale con operaciones de schema en lugar de codigo manual de actualizacion de storage.
---

TerraScale usa operaciones de schema para la evolucion normal de modelos. Los SDKs envian la intencion del modelo tipado, Server planifica el diff de schema y TerraBase sigue siendo el document store tipado detras del limite del producto.

El flujo comun es:

- inferir o definir un modelo tipado en el SDK TypeScript o C#
- ejecutar un plan de schema para revisar seguridad, campos afectados, acciones generadas y alcance de reescritura
- aplicar cambios aditivos seguros automaticamente en entornos locales y de desarrollo
- exigir aprobacion explicita para cambios guarded en produccion
- mantener legibles las formas antiguas y nuevas mientras corren reescrituras en background
- inspeccionar estado, progreso, fallos y versiones de schema desde API, SDK y dashboard

Esto reemplaza el patron anterior donde el codigo de aplicacion era responsable de upgrades rutinarios de storage. Los usuarios no deberian escribir jobs de mapeo, jobs de indices o scripts de colecciones para campos aditivos normales, defaults, indices o transforms de compatibilidad seguros.

## Modelo actual

Los cambios de schema se representan como operaciones durables propiedad de Server. Cada operacion registra el diff planificado, safety class, version de schema objetivo, fase, progreso y cualquier mensaje de fallo. TerraScale almacena esos registros en TerraBase y reanuda trabajo recuperable despues de restart salvo que la operacion este pausada explicitamente.

Los cambios seguros pueden completarse de inmediato. Los cambios guarded avanzan por fases como expanding, backfilling, cutover, cleanup y done. Las operaciones fallidas pueden reintentarse desde su version de schema objetivo persistida.

## Cambios seguros

Cambios que TerraScale puede aplicar sin codigo manual de actualizacion de storage:

- agregar un campo opcional
- agregar un campo requerido con default
- agregar un indice o access path generado
- ampliar un tipo compatible
- agregar paths JSON/map seleccionados por auto-indexing
- agregar un campo unique despues de validar duplicados y hacer backfill de reservas

Usa schema plan primero cuando necesites revisar la operacion exacta antes de aplicar.

## Cambios guarded

Algunos cambios requieren confirmacion porque TerraScale solo puede preservar correctitud con una operacion explicita:

- rename con alias
- backfill de campo requerido
- cambios de indice o access path en colecciones grandes
- backfill de reservas de unique constraint
- transforms de compatibilidad para formas almacenadas antiguas

Los cambios guarded en produccion requieren `productionApprovalId` antes de aplicar.

## Cambios bloqueados

TerraScale rechaza cambios donde no puede inferir una intencion segura:

- eliminar campos de forma destructiva sin un plan de reemplazo deliberado
- rename ambiguo sin alias
- estrechar tipos con posible perdida de datos
- cambios de identidad de documento o placement que requieren decision de producto
- reescrituras semanticas que requieren logica de negocio

Para esos casos, usa una reescritura de datos por etapas como trabajo de aplicacion u operaciones. Mantenla idempotente, observable, limitada por tenant y probada con datos representativos antes de aplicarla a registros live.

## Observabilidad de operaciones

Sigue la evolucion de schema por historial de operaciones y versiones:

- version de schema actual y objetivo
- safety class y acciones de storage generadas
- collection y campos afectados
- porcentaje de progreso y fase
- mensaje de fallo y guia de retry/resume
- IDs de audit y correlacion de request

## Buenas practicas

1. Trata las definiciones de modelos del SDK como la fuente de intencion de schema.
2. Usa la salida de schema plan en revisiones y despliegues.
3. Prefiere cambios aditivos y defaults antes de limpieza destructiva.
4. Mantiene lecturas de compatibilidad hasta que terminen las reescrituras en background.
5. Usa campos unique tipados solo cuando validacion de duplicados y backfill de reservas puedan completarse.
6. Reserva reescrituras manuales para cambios destructivos o semanticos que TerraScale no pueda inferir.

## Relacionado

- [Validation](/reference/validation/)
- [Data Models](/reference/data-models/)
- [Best Practices](/reference/best-practices/)
- [TQL API](/reference/api/tql/)
