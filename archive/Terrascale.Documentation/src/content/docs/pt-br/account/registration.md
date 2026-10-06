---
title: Account Registration
description: Cadastro somente por e-mail e fluxo de verificação.
sidebar:
  order: 1
---

O cadastro no TerraScale é somente por e-mail: informe um endereço, verifique-o com o código enviado para a caixa de entrada e a conta passa a existir — não há senha para escolher nem outra credencial para gerenciar. O login depois funciona sempre da mesma forma: um link de login enviado para o e-mail verificado.

No fluxo alvo de autorregistro do Dashboard, a verificação de identidade e e-mail aparecerá como a primeira etapa já concluída. Depois, guiará o User pela primeira Organization, pelo primeiro Project e pela primeira Database lógica, seguida da verificação de um cartão de pagamento para controle de abuso no cadastro. A verificação do cartão não criará cobrança, assinatura, teste pago nem renovação automática. Em seguida, o User escolherá entre continuar sem plano pago e sem renovação automática, mantendo a franquia Developer, ou selecionar Starter ou Pro com renovação automática mensal e os primeiros 30 dias sem cobrança quando a Organization for elegível. O onboarding de Users convidados continuará separado.

O fluxo alvo é acompanhado pelo [issue 30 do TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30), e o trabalho tipado do SDK pelo [issue 6 do TerraScale.TypeScript](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6). Esse ainda não é o comportamento publicado.

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
