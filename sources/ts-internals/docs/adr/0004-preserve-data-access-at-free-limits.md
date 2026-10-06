# Preserve data access at free-tier limits

The free tier does not expire. TerraScale does not delete or hide customer data
because a customer declines a paid plan or reaches a free allowance. At a hard
limit, the service preserves reads, exports, and deletion while rejecting new
billable writes or resource creation with a typed upgrade response.

Dashboard owns subscription and dunning behavior through Better Auth's
official Stripe plugin. TerraBase usage facts remain the billing authority.
Overage billing requires reconciled usage, customer-visible totals, spend-cap
enforcement, and tested dispute, refund, and provider-failure handling.
