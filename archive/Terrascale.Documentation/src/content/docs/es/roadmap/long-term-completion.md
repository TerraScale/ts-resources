---
title: Plan de Conclusión de Largo Plazo
description: La hoja de ruta guiada por aceptación para completar TerraScale en base de datos, auth, queue, pagos, SDKs, dashboard, GitOps y operaciones.
sidebar:
  order: 5
headingBadge:
  text: Planificado
  variant: secondary
---


## Objetivo Final del Producto


## Hitos

| Hito | Resultado |
| --- | --- |
| Decisiones y baseline | ADRs de transporte público, regiones y proveedores, matrices MVP y un comando local de E2E. |
| MVP de base de datos | Colecciones tipadas, evolución automática segura de schema, consultas, claves de API, APIs de repositorio en los SDKs y flujos de base de datos en el dashboard. |
| MVP de Auth | Signup, inicio de sesión solo con correo mediante enlaces de verificación, verificación, sesiones, invitaciones, RBAC y bases de cuenta conscientes de pagos. |
| MVP de Queue | Runtime NATS JetStream, topología NATS en Fabric, send/receive/ack/lease/DLQ/redrive, SDKs, páginas de cola en el dashboard y validación de workers de email/export. |
| Fabric y multi-región | Adopción de Fabric standalone, registro de nodos, placement, ruteo, topología `gru`, `sfo`, `fra` y simulación de outage. |
| Hardening beta | Observabilidad, proveedores de email, pagos directos con Stripe, capacidades SaaS builder de Auth y Payments, seguridad, docs, ejemplos y automatización de release. |

## Alcance MVP

El MVP congela la plataforma completa más pequeña que se puede finalizar de punta a punta:

- APIs públicas REST HTTP con WebSockets o SSE para flujos en tiempo real de navegador.
- Creación de base de datos, creación de colección, CRUD de repositorio tipado, consulta, paginación, evolución segura de schema e historial de operaciones.
- Signup de Auth, verificación, enlaces de inicio de sesión solo con correo, rotación de refresh, sesiones, miembros de organización, invitaciones, claves de API y resúmenes de cuenta conscientes de pagos.
- Creación de cola, envío, recepción, confirmación, abandono, extensión de lease, DLQ, redrive, política de retry, estadísticas y verificación NATS JetStream.
- Entrega de email independiente de proveedor con Mailpit local y adapters de proveedor probados.
- Pagos directos con Stripe, tests determinísticos de cola y webhooks, sesiones de checkout, sesiones de portal de billing, webhooks firmados, proyección persistida de billing y prueba en sandbox vivo de Stripe bloqueada hasta que se entreguen credenciales.
- SDKs TypeScript y C# usando la API pública HTTP.
- Los endpoints y la orquestación específicos del Dashboard viven solo en el proyecto full-stack del Dashboard. Sus rutas de servidor usan métodos tipados del SDK TypeScript como un usuario externo ordinario de TerraScale.Platform, con los mismos contratos públicos, autenticación, autorización y límites de tenant que las aplicaciones de clientes.

## Escenarios de Aceptación Final


1. Creación de cuenta y organización con verificación de email, login, refresh y verificaciones de metadatos TerraBase.
2. Base de datos y evolución de schema en `gru`, `sfo` y `fra`.
3. Validación de query y subconjunto SQL con planes de explain y errores estándar.
4. Procesamiento de colas por NATS JetStream, incluyendo DLQ y redrive.
5. Checkout de Stripe, webhooks firmados, suscripciones, entitlements, actualización de roles de Auth, uso, invoices y seguridad de replay de eventos mediante TerraScale Payments y TerraScale.Queue, con cobertura determinística de cola/webhooks y evidencia opt-in de sandbox vivo de Stripe.
6. Flujos avanzados de autenticación por proyecto con MFA, passkeys, proveedores OAuth, invitaciones, scopes de clave de API y auditoría para el producto Authentication con alcance de proyecto.
7. Cobertura de rutas del dashboard con datos backend reales.
8. Topología Fabric multi-región, ruteo, outage y recuperación.
10. Verificaciones de observabilidad para logs, traces, métricas, alertas y estado operativo correlacionados.

## Regla Actual de Aceptación

Las capacidades descritas en esta página no son promesas de disponibilidad pública. Una capacidad se acepta solo cuando implementación, SDKs, dashboard, docs y pruebas demuestran el comportamiento por la superficie pública prevista y por estado backend durable.

## Conceptos Relacionados

Lee [Conceptos de la Plataforma](/guides/platform-concepts/) para entender los conceptos de producto detrás de esta hoja de ruta.
