# Add layered abuse controls to signup and Authentication

TerraScale platform signup requires verified email, credit-card validation
through Stripe, Stripe Radar, bot checks such as Turnstile, IP and account
controls, velocity limits, and manual suspension without revealing which fraud
check failed. Dashboard owns these controls. A valid card does not require the
user to subscribe during onboarding.

The customer Authentication product offers verified email, bot-challenge
integration, configurable IP and account controls, velocity limits, and user
suspension. Platform signup controls remain separate from customer Project
Authentication.

The customer controls in this decision apply to end users of customer
applications. They do not grant credentials or database scope to a TerraScale
account.
