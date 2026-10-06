---
title: "Boas práticas de segurança para TerraScale"
date: 2024-09-25
authors:
  - name: Mario Gabriell Karaziaki Belchior
    title: Founder
    url: mailto:mariogk@terrascale.tech
tags:
  - security
  - best-practices
excerpt: Segurança não é opcional. Veja como manter seus bancos TerraScale seguros com um gerenciamento sensato de API keys, MFA e controles de acesso.
cover:
  wide: /images/blog/security-best-practices/cover-wide.svg
  square: /images/blog/security-best-practices/cover-square.svg
  alt: Geometria em camadas de escudo e nós de perímetro protegidos, transmitindo segurança de banco de dados em nível empresarial.
---

Segurança não é opcional. Aqui está um checklist prático para ajudar você a manter seus bancos TerraScale seguros.

## O que você vai aprender

- Como gerenciar API keys sem criar risco desnecessário
- Quais controles de conta e equipe mais importam
- O que revisar regularmente para que segurança continue sendo algo sem drama, da melhor forma possível

Se você estiver configurando acesso enquanto lê, deixe por perto a [referência de autenticação](/reference/authentication/), a [referência de API keys](/reference/management/api-keys/) e o [guia de MFA](/reference/mfa/).

## Segurança de API keys

### Use escopos específicos

Nunca use `*` para workloads de produção. Conceda apenas as permissões de que cada serviço realmente precisa:
```csharp
// Bad: Full access
{ "scopes": ["*"] }

// Good: Specific permissions
{ "scopes": ["database:read"] }  // Read-only service
{ "scopes": ["database:read", "database:write"] }  // Backend API
{ "scopes": ["repository:read", "repository:write"] }  // Specific to repositories
```

### Separe chaves por ambiente

Use API keys diferentes para ambientes diferentes. Assim, um problema em um ambiente não vira automaticamente um problema em todos os outros.

| Environment | Key Name | Scopes |
|-------------|----------|--------|
| Production | prod-backend | database:read, database:write |
| Staging | staging-backend | database:read, database:write |
| Development | dev-local | database:* |
| CI/CD | ci-tests | database:read |

### Faça rotação de chaves regularmente

API keys devem ser rotacionadas a cada 90 dias:

1. Crie uma nova chave com os mesmos escopos
2. Atualize a configuração da sua aplicação
3. Faça deploy e verifique
4. Revogue a chave antiga

### Nunca faça commit de chaves

API keys nunca devem estar no controle de versão:
```csharp
// Bad: Hardcoded
var apiKey = "tsauth_abc123...";

// Good: Environment variable
var apiKey = Environment.GetEnvironmentVariable("TERRASCALE_API_KEY");

// Good: Secret manager
var apiKey = await secretManager.GetSecretAsync("terrascale-api-key");
```

Adicione estes padrões ao seu `.gitignore` se ainda não estiverem lá:
```
.env
.env.local
*.env
appsettings.Development.json
```

## Segurança da conta

### Habilite autenticação de dois fatores

Toda conta deve ter 2FA habilitado. O TerraScale suporta:

- **Apps autenticadores** (Google Authenticator, Authy, 1Password) - Recomendado
- **Códigos por email** - Bons como backup

Para habilitar:
1. Vá em Settings > Security
2. Clique em "Add Method"
3. Escaneie o QR code com seu app autenticador
4. Digite o código de verificação

### Use senhas fortes

Requisitos:
- Mínimo de 12 caracteres (recomendamos 16+)
- Mistura de maiúsculas, minúsculas, números e símbolos
- Exclusiva para TerraScale (não reutilizada de outros serviços)

Considere usar um gerenciador de senhas. Se uma pessoa na sua equipe ainda reutiliza senhas, este é o momento de corrigir isso.

### Revise sessões ativas

Confira periodicamente Settings > Security > Sessions:

- Procure localizações ou dispositivos desconhecidos
- Revogue qualquer sessão que você não reconheça
- Considere revogar todas as sessões após mudanças de senha

## Segurança da equipe

### Princípio do menor privilégio

Atribua o menor papel necessário:

| Role | Use Case |
|------|----------|
| Owner | Only the account creator (one person) |
| Admin | Team leads who need to manage members |
| Member | Developers who create and manage resources |
| Read-only | Auditors, analysts, support staff |

### Audite os membros da equipe

Revise sua equipe trimestralmente:

- Remova pessoas que saíram da organização
- Rebaixe permissões que não são mais necessárias
- Verifique se todos os membros têm 2FA habilitado

### Trate saídas rapidamente

Quando alguém sair:

1. Remova essa pessoa da organização imediatamente
2. Revogue quaisquer API keys criadas por ela
3. Revise quaisquer recursos aos quais ela tinha acesso
4. Considere rotacionar credenciais compartilhadas

## Segurança de rede

### Use apenas HTTPS

Todas as APIs do TerraScale Platform exigem HTTPS. Nunca tente usar HTTP.

### Valide certificados TLS

Não desabilite a validação de certificado em produção:
```csharp
// Never do this in production
ServicePointManager.ServerCertificateValidationCallback = (s, c, ch, e) => true;
```

### Controles de acesso de rede

O contrato público atual não documenta restrições de rede baseadas em IP. Não presuma que um plano inclui essas restrições. Use escopos de projeto, separação por ambiente e os controles de autenticação documentados nas referências públicas.

## Segurança de dados

### Tratamento de dados sensíveis

Não armazene dados altamente sensíveis diretamente, a menos que você tenha um motivo claro e um plano de tratamento documentado:
```csharp
// Bad: Storing raw SSN
["ssn"] = "123-45-6789"

// Better: Store a hash or encrypted value
["ssnHash"] = Hash("123-45-6789")

// Best: Don't store it at all if you don't need it
```

### Criptografia em repouso

O TerraScale usa controles qualificados de armazenamento e gerenciamento de chaves para dados em repouso. A política pública de segurança não nomeia um algoritmo até que a evidência de produção cubra todos os caminhos relevantes. Criptografia não substitui autorização, isolamento de tenant, recuperação ou exclusão.

### Criptografia em trânsito

O tráfego de clientes exige TLS 1.2 ou mais recente. Mantenha a validação de certificados ativa e não deduza um mínimo de protocolo mais forte a partir de um cliente ou da rede.

Por que isso importa: padrões de infraestrutura podem proteger você contra grandes classes de erros, mas eles não substituem decisões no nível da aplicação, como definir corretamente escopos de segredos ou escolher quais dados realmente precisam viver no banco de dados.

## Monitoramento e alertas

### Habilite audit logs

Acompanhe quem está acessando seus dados:

- Uso de API keys por tipo de operação
- Tentativas de autenticação com falha
- Ações administrativas (mudanças de membros, criação de chaves)

### Configure alertas

Configure alertas para:

- Padrões incomuns de uso da API
- Picos de falha de autenticação
- Criação de novas API keys
- Mudanças de membros da equipe

### Revisões regulares

Checklist mensal de segurança:

- [ ] Revisar uso de API keys, alguma surpresa?
- [ ] Verificar API keys inativas, revogue-as
- [ ] Confirmar que a lista de membros da equipe está correta
- [ ] Confirmar que todos os membros da equipe têm 2FA
- [ ] Revisar quaisquer alertas de segurança

## Resposta a incidentes

### Se uma API key for comprometida

1. **Revogue imediatamente** - Não espere, revogue a chave agora
2. **Crie uma nova chave** - Gere uma substituta
3. **Atualize as aplicações** - Faça deploy da nova chave
4. **Audite o uso** - Verifique logs em busca de acesso não autorizado
5. **Revise os dados** - Procure quaisquer modificações de dados
6. **Documente** - Registre o que aconteceu e como você respondeu

### Se uma conta for comprometida

1. **Troque a senha imediatamente**
2. **Revogue todas as sessões**
3. **Revise e revogue API keys**
4. **Habilite 2FA se ainda não estiver habilitado**
5. **Verifique membros de equipe não autorizados**
6. **Fale com o suporte** em support@terrascale.tech

## Resumo

Segurança é responsabilidade de todos. O objetivo não é perfeição. O objetivo é fazer do caminho seguro o caminho normal.

1. Use escopos específicos para API keys
2. Faça rotação de chaves a cada 90 dias
3. Habilite 2FA para todas as contas
4. Use o princípio do menor privilégio
5. Nunca faça commit de segredos no controle de versão
6. Monitore atividade incomum
7. Tenha um plano de resposta a incidentes

Dúvidas sobre segurança? Entre em contato em security@terrascale.tech. Para orientação operacional geral, a [referência de boas práticas](/reference/best-practices/) também vale o bookmark.
