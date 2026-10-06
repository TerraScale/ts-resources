---
title: Alfa Pública
description: Lo que incluye hoy la Alfa Pública de TerraScale, dónde están los límites actuales y qué se sigue desarrollando.
sidebar:
  order: 2
---

La Alfa Pública es la etapa de lanzamiento actual de TerraScale. La plataforma está lista para una evaluación real y cargas de trabajo iniciales, pero algunas capacidades siguen evolucionando mientras el equipo recopila datos de uso y feedback.

## Qué Significa la Alfa Pública

Alfa Publica significa que la plataforma principal funciona y esta disponible para los usuarios hoy. Puedes construir sobre ella, probar patrones de trafico reales y evaluar la API publica, SDKs, dashboard, SQL, Queue, Auth y Payments soportados. Al mismo tiempo, esta etapa todavia esta definida por el feedback, asi que los limites pueden cambiar y algunas pruebas en vivo de Stripe, proveedores de email, proveedores OAuth y produccion todavia estan en camino.

Para ver el contexto más amplio de la hoja de ruta, consulta la [Hoja de Ruta Pública](/roadmap/).

## Funciones Disponibles

- Soporte para API HTTP JSON versionada `/api/v1`
- Acceso a la interfaz TQL
- Soporte para SDK de C#
- Soporte para SDK de TypeScript
- Flujos del dashboard respaldados por la API publica y los SDKs
- Colecciones tipadas y operaciones de schema respaldadas por TerraBase
- Flujos locales/default-CI de Queue, Auth y Payments
- Modelo de regiones de lanzamiento para `gru`, `sfo` y `fra`

Si quieres empezar a usar la plataforma ahora, consulta la [guía de primeros pasos](/guides/getting-started/).

## Límites Actuales

- La validacion actual de regiones de lanzamiento se limita a `gru`, `sfo` y `fra`
- Se aplican límites de tasa durante la Alfa Pública
- Los flujos en vivo de Stripe, proveedores de email y proveedores OAuth requieren credenciales y configuracion de webhooks/cuentas provistas por el operador
- La evidencia de interrupcion multi-region similar a produccion sigue siendo un bloqueador de release

Estas barreras ayudan al equipo a mantener la plataforma actual confiable mientras la Alfa Pública se amplía.

## Lo que Aún No Está Disponible

Los siguientes elementos están planificados, pero todavía no forman parte de la versión actual de la Alfa Pública:

- Prueba completa de interrupcion multi-region TerraBase/NATS/Fabric similar a produccion
- Prueba de Sentry en vivo y Alertmanager de produccion
- Prueba de proveedor OAuth/IdP en vivo
- Prueba en sandbox en vivo de pagos con Stripe y proveedores de email
- Cache automatica

Consulta la [Hoja de Ruta de la Alfa Pública](/roadmap/public-alpha-roadmap/) para ver el siguiente conjunto de prioridades.

## Cómo Enviar Feedback

Las prioridades de la Alfa Pública están muy influenciadas por el feedback real de los usuarios. Únete a la [comunidad de Discord](https://discord.gg/8Zr2Nw9g) para compartir ideas, informar fricciones y comentar tu caso de uso con el equipo.

Para soporte directo o feedback sobre la hoja de ruta, escribe a [support@terrascale.tech](mailto:support@terrascale.tech).
