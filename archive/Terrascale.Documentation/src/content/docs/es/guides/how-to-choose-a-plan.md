---
title: Cómo elegir un plan
description: Elige entre Developer, Starter, Pro y Enterprise no disponible usando el catálogo de la Alfa Pública.
sidebar:
  order: 12
---

Usa esta guía con la lista pública de planes en `GET /api/v1/pricing/plans`. El catálogo es el contrato de la Alfa Pública. La respuesta de la API es la fuente autoritativa si cambia el catálogo publicado. Cada User recibe una Organización Personal no transferible. Sus métodos de pago, identidad de cliente de Polar, suscripciones, pruebas, historial de facturación, Projects y membresías pertenecen a la Organización, no directamente al User.

## Elección objetivo durante el onboarding

El flujo objetivo de autorregistro comienza con la verificación de identidad y correo electrónico ya contada como un paso completado. Luego crea la primera Organization, Project y Database lógica y verifica una tarjeta de pago para controlar abusos en el registro. La verificación no crea cargo, suscripción, prueba pagada ni renovación automática. Después, el User elige entre continuar sin plan de pago y sin renovación automática, conservando la asignación Developer, o seleccionar Starter o Pro con renovación automática mensual y los primeros 30 días sin cargo cuando la Organization sea elegible. En el texto de onboarding, "sin plan de pago" es la opción que ve el cliente y Developer es la asignación gratuita interna. El onboarding de Users invitados sigue separado. Este objetivo todavía no está publicado y se sigue en el [issue 30 de TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30).

## Selector rápido

| Plan | Precio y disponibilidad | Cuándo conviene |
| --- | --- | --- |
| `Developer` | $0, no vence | Estás explorando TerraScale o creando un prototipo dentro de los límites de Developer. |
| `Starter` | $5 mensual | Necesitas una asignación pagada pequeña y un objetivo de soporte. |
| `Pro` | $25 mensual | Necesitas asignaciones mayores de proyectos, almacenamiento y unidades de operación. |
| `Enterprise` | Base de soporte mensual de $500 más uso medido, no disponible durante la Alfa Pública | Necesitas un plan contractual cuando se aprueben sus términos. |

## Límites que suelen decidir

- **Proyectos y bases de datos**: Developer permite 1 Project y 3 Databases. Starter permite 5 Projects y 10 Databases. Pro permite 25 Projects y 50 Databases.
- **Almacenamiento**: Developer permite 1 GB entre las regiones seleccionadas. Starter permite 5 GB. Pro permite 50 GB.
- **Unidades de operación**: Developer permite 10.000 al mes. Starter permite 1.000.000. Pro permite 10.000.000.
- **Miembros**: Developer permite 3 miembros. Starter permite 5. Pro permite 25.
- **Regiones**: todos los planes disponibles pueden seleccionar São Paulo, San Francisco y Falkenstein.

## Consejos prácticos

1. Empieza con **Developer** mientras validas la autenticación, los repositorios, TQL y los flujos de colas.
2. Elige **Starter** cuando las asignaciones de Developer ya no alcancen.
3. Elige **Pro** cuando necesites asignaciones mayores u objetivo de soporte de un día hábil.
4. Trata **Enterprise** como no disponible hasta que se aprueben su contrato y sus tarifas de uso.

Cuando se alcanza una asignación estricta, se rechaza el nuevo trabajo facturable. Las lecturas, la exportación de proyectos, la eliminación y el trabajo que reduce el uso siguen disponibles. La asignación mensual de unidades de operación se restablece al comienzo del siguiente mes calendario.

Una Organización pagada elegible recibe sus primeros 30 días sin cargo después de que un Organization Owner selecciona explícitamente Starter o Pro y acepta la renovación automática mensual. Verificar la tarjeta para el registro no inicia este período. La elegibilidad de la prueba es duradera; los cambios en la tarjeta, el propietario o la membresía no la restauran. La cancelación detiene la renovación al final del período pagado. Una renovación fallida recibe siete días de reintentos de pago con acceso normal y luego un período de solo lectura de 30 días. El pago durante cualquiera de los dos períodos restaura el plan anterior y el acceso a los datos. El período de solo lectura permite leer, reducir el uso, eliminar y exportar, y bloquea el nuevo trabajo facturable. Al finalizar, TerraScale purga el Customer content y las copias que el cliente puede restaurar. Conserva solo los registros mínimos de la organización, facturación, seguridad, Audit y recibo de eliminación requeridos por la política. La organización vacía puede reactivarse más adelante, pero los datos purgados no pueden volver y una organización impaga no se degrada a Developer.

La eliminación voluntaria del User es independiente del tratamiento de pagos fallidos. Comienza una ventana cancelable de siete días, revoca sesiones de inmediato, detiene los cargos y conserva la exportación durante la ventana. Al completarse, elimina la Organización Personal, las membresías y el Customer content, y conserva solo los registros legalmente requeridos y un recibo de eliminación. Una exportación completa de Project es un paquete ZIP versionado con un manifiesto versionado, hashes de integridad y un archivo JSON delimitado por saltos de línea por cada Repository. Incluye Database, Environment, Repository, Document, índices y metadatos de versión, nunca incluye secretos de credenciales y no es una copia de seguridad ni una instantánea de Database. La entrega es una descarga autenticada y revocable disponible durante 24 horas o un destino presignado de AWS S3 proporcionado por el cliente y de corta duración. TerraScale nunca almacena las claves de acceso de AWS del cliente.

## Soporte

Developer recibe documentación y soporte por correo de mejor esfuerzo. Starter tiene como objetivo responder en dos días hábiles. Pro tiene como objetivo responder en un día hábil. Estos objetivos no garantizan la resolución ni son un SLA de disponibilidad. El soporte de Enterprise no está disponible durante la Alfa Pública.

Los precios no varían según la región seleccionada. La medición de unidades de operación usa el contrato de bloques iniciados de 4 KiB documentado en [Precios](/reference/pricing/).

## Próximos pasos

- [Referencia de planes](/reference/plans/)
- [Facturación](/reference/billing/)
- [Primeros pasos](/guides/getting-started/)
