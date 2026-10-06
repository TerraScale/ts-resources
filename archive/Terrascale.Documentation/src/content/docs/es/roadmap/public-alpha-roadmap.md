---
title: Hoja de Ruta de la Alfa Pública
description: Mejoras planificadas para TerraScale durante la Alfa Pública, incluida la automatización del rendimiento y límites más altos por base de datos.
sidebar:
  order: 3
---

Esta página cubre las principales mejoras planificadas durante la Alfa Pública. El enfoque es directo: hacer que TerraScale sea más rápida de adoptar, más fácil de ajustar y más capaz bajo cargas de trabajo reales.

Para ver la visión completa del producto, consulta la [Hoja de Ruta Pública](/roadmap/). Para la etapa de lanzamiento actual, consulta [Alfa Pública](/roadmap/public-alpha/).

## Resumen

La Alfa Publica ya se puede usar, pero aun quedan varias mejoras importantes por delante. La hoja de ruta en esta etapa se centra en automatizacion de rendimiento, evolucion automatica de schema, mejor comportamiento de cache y prueba similar a produccion para el modelo de regiones de lanzamiento soportado.

## Funciones Planificadas

### Indexación Automática

TerraScale ya tiene cobertura default-CI y deterministica para candidatos de auto-indexing informados por workload, incluidos patrones repetidos de consulta sobre propiedades JSON. El trabajo restante es evidencia DevHost/runtime mas amplia, ajuste de politica con workloads reales y visibilidad operativa que explique por que se selecciono un indice generado.

### Caché Automática con Invalidación

La caché automática de resultados de consultas está planificada para mejorar el rendimiento de lectura sin exigir que los equipos gestionen manualmente cada decisión de caché. La invalidación de la caché forma parte del diseño para mantener los resultados almacenados alineados con los cambios en los datos subyacentes.

### Evolución Automática de Esquema

TerraScale hace que los cambios de modelo seguros se sientan automaticos desde el SDK mientras el almacenamiento en TerraBase sigue tipado y respaldado por operaciones de schema internamente. El SDK y el control plane infieren cambios seguros en colecciones e indices, siguen versiones de schema y ejecutan rewrites en background para que los desarrolladores no tengan que escribir codigo de upgrade de almacenamiento para la evolucion comun de modelos.

### Prueba de regiones de lanzamiento similar a produccion

El modelo de regiones de lanzamiento es `gru`, `sfo` y `fra`. La hoja de ruta incluye prueba de interrupcion TerraBase/NATS/Fabric similar a produccion, reconciliacion de Vault en vivo, entrega de Sentry en vivo y ruteo de Alertmanager de produccion antes de reclamar readiness multi-region estable.

### Controles Manuales de Caché

Junto con la caché automática, TerraScale planea añadir controles manuales de caché para los equipos que quieran un control más estricto sobre el comportamiento. Eso incluye expulsión LRU y gestión explícita de la caché para cargas de trabajo que necesitan ajustes predecibles.

## Notas sobre el Cronograma

Esta hoja de ruta se prioriza según el feedback de los usuarios y los patrones reales de uso. Todavía no hay fechas públicas fijas, y el orden puede cambiar a medida que el equipo aprende más de cargas de trabajo similares a producción durante la Alfa Pública.

## Solicita una Función

¿Quieres influir en la hoja de ruta? Únete a la [comunidad de Discord](https://discord.gg/8Zr2Nw9g) y comparte qué necesita tu carga de trabajo a continuación.

Para solicitudes directas o preguntas de seguimiento, escribe a [support@terrascale.tech](mailto:support@terrascale.tech).
