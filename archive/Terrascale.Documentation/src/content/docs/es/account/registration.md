---
title: Account Registration
description: Registro solo con correo y flujo de verificación.
sidebar:
  order: 1
---

El registro en TerraScale es solo con correo electrónico: se proporciona una dirección, se verifica con el código enviado al buzón y la cuenta queda creada — no hay contraseña que elegir ni otra credencial que gestionar. Iniciar sesión después funciona siempre igual: un enlace de inicio de sesión enviado al correo verificado.

En el flujo objetivo de autorregistro del Dashboard, la verificación de identidad y correo electrónico aparecerá como el primer paso ya completado. Luego guiará al User por la primera Organization, Project y Database lógica, seguida de la verificación de una tarjeta de pago para controlar abusos en el registro. Verificar la tarjeta no generará cargos, suscripción, prueba pagada ni renovación automática. Después, el User elegirá entre continuar sin plan de pago y sin renovación automática, conservando la asignación Developer, o seleccionar Starter o Pro con renovación automática mensual y los primeros 30 días sin cargo cuando la Organization sea elegible. El onboarding de Users invitados seguirá separado.

El flujo objetivo se sigue en el [issue 30 de TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30), y el trabajo del SDK tipado en el [issue 6 de TerraScale.TypeScript](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6). Todavía no es el comportamiento publicado.

## Verify Email

```http
POST /api/v1/auth/password/verify-email
```

```json
{
  "pendingAuthenticationToken": "pending-token",
  "code": "123456"
}
```

## Resend Verification

```http
POST /api/v1/auth/password/resend-verification
```

```json
{
  "pendingAuthenticationToken": "pending-token",
  "verifyUrl": "https://app.example.test/verify"
}
```

Project-scoped signup and verification routes are under `/api/v1/projects/{projectId}/auth/signup`, `/verify-email`, and `/resend-verification`.

## TypeScript SDK

```ts
await client.auth.verifyEmail({
  pendingAuthenticationToken: 'pending-token',
  code: '123456'
});
```

## C# Status

The current `TerraScale.DotNet` SDK does not expose signup or verification helpers.

## Next Steps

- [Login](/account/login/)
- [Authentication](/reference/authentication/)
- [Profile](/account/profile/)
