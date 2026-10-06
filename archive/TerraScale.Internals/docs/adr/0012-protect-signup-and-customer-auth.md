# Add layered abuse controls to signup and Authentication

TerraScale signup requires verified email, Polar payment-method verification, bot checks such as Turnstile, IP and account controls, one Developer organization per user and payment method, velocity rules, and manual suspension without revealing which individual fraud check failed. The customer Authentication product offers verified email, bot-challenge integration, configurable IP and account controls, velocity rules, and user suspension. Polar checks and Developer-organization limits remain TerraScale platform rules rather than customer Authentication features.

ADR-0037 supersedes only the constraint based on sharing one payment method across Users because Polar does not expose a card fingerprint. The remaining signup and abuse controls stay in force.
