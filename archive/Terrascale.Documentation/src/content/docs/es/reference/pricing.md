---
title: Precios y medición
description: Reglas de almacenamiento y unidades de operación de la Alfa Pública.
sidebar:
  order: 7
---

TerraScale mide el almacenamiento entre regiones y el trabajo de la base de datos en unidades de operación. La Alfa Pública usa límites estrictos por plan y no cobra la transferencia de salida. La facturación, los métodos de pago y el historial pertenecen a la Organización, no directamente al User.

## Almacenamiento entre regiones

El uso de almacenamiento es la suma de los bytes sin comprimir de los documentos guardados en cada región seleccionada. Un conjunto de 100 MB almacenado en tres regiones consume 300 MB. El límite de 1 GB de Developer usa el mismo cálculo.

Las vistas de almacenamiento por base de datos son estimaciones. TerraScale aplica el límite al uso exacto de los proyectos de la organización.

## Unidades de operación

Una unidad de operación cubre cada bloque iniciado de 4 KiB, o 4.096 bytes, de datos de documentos procesados por una operación facturable.

- Las lecturas cobran los bytes de cada documento devuelto desde la región que atendió la solicitud.
- Una consulta exitosa sin resultados cuesta una unidad.
- Las creaciones, sustituciones y actualizaciones cobran las unidades del documento una vez por cada región seleccionada.
- Un lote redondea cada documento por separado y luego suma las unidades.
- Una eliminación cuesta una unidad por región seleccionada.

### Redondeo

Un documento de 1 byte y uno de 4.096 bytes cuestan una unidad. Un documento de 4.097 bytes cuesta dos.

### Escritura multirregional

Escribir un documento de 5 KiB usa dos unidades por región. Con tres regiones seleccionadas cuesta seis unidades. La replicación no agrega otro cargo.

### Lotes

Un lote escribe documentos de 1 KiB, 4 KiB y 5 KiB en dos regiones. Se redondean a una, una y dos unidades por región. El lote cuesta ocho unidades: `(1 + 1 + 2) × 2`.

### Consultas y eliminaciones

Una consulta sin documentos cuesta una unidad. Tres documentos de 2 KiB cuestan tres unidades porque cada uno se redondea por separado. Eliminar un documento de una base de datos con tres regiones cuesta tres unidades.

## Trabajo no facturado

Las solicitudes rechazadas, los errores del servidor, reintentos internos, indexación, copias de seguridad, monitorización, reparación interna y la replicación posterior a la multiplicación regional no agregan unidades. La transferencia de salida aparece en los informes, pero no se factura durante la Alfa Pública.

## Al alcanzar un límite

TerraScale rechaza el nuevo trabajo facturable que superaría un límite. Las lecturas, la exportación de proyectos, la eliminación y la reducción de uso siguen disponibles. Alcanzar un límite no elimina los datos almacenados.

Consulta [Planes de la Alfa Pública](/reference/plans/) para ver los límites mensuales.
