# Dashboard command reference

Every action uses the dashboard's published authenticated feature API.
Run a command with `--help` for its input flags and required fields.
Use `--project-id` and `--organization-id` to select a scope, `--json` for
structured output, or `--dry-run` to inspect a request without sending it.
Destructive actions require `--yes`; server roles remain authoritative.

| Command | Dashboard action | Purpose |
| --- | --- | --- |
| `ts access get-invitation` | `get_invitation` | Get invitation |
| `ts access invite` | `invite_member` | Invite member |
| `ts access list-invitations` | `list_invitations` | List invitations |
| `ts access members` | `list_members` | List members |
| `ts access remove` | `remove_member` | Remove member |
| `ts access resend-invitation` | `resend_invitation` | Resend invitation |
| `ts access respond-to-invitation` | `respond_to_invitation` | Respond to invitation |
| `ts access revoke-invitation` | `revoke_invitation` | Revoke invitation |
| `ts access set-role` | `update_member_role` | Update member role |
| `ts admin delete-plan` | `admin_delete_plan` | Delete plan (platform admin) |
| `ts admin get-estate` | `admin_get_estate` | Get estate (platform admin) |
| `ts admin get-usage` | `admin_get_usage` | Get platform usage (platform admin) |
| `ts admin list-databases` | `admin_list_databases` | List databases (platform admin) |
| `ts admin list-organizations` | `admin_list_organizations` | List organizations (platform admin) |
| `ts admin list-plans` | `admin_list_plans` | List plans (platform admin) |
| `ts admin list-projects` | `admin_list_projects` | List projects (platform admin) |
| `ts admin list-users` | `admin_list_users` | List users (platform admin) |
| `ts admin record-estate-action` | `admin_record_estate_action` | Record estate action (platform admin) |
| `ts admin rename-organization` | `admin_rename_organization` | Rename organization (platform admin) |
| `ts admin rename-project` | `admin_rename_project` | Rename project (platform admin) |
| `ts admin save-plan` | `admin_save_plan` | Save plan (platform admin) |
| `ts admin set-plan-visibility` | `admin_set_plan_visibility` | Set plan visibility (platform admin) |
| `ts admin update-user` | `admin_update_user` | Update user (platform admin) |
| `ts audit list` | `list_audit_events` | List audit events |
| `ts authentication action` | `auth_run_resource_action` | Run authentication record action |
| `ts authentication audit` | `auth_list_audit_events` | List authentication audit events |
| `ts authentication branding` | `auth_update_branding` | Update hosted page branding |
| `ts authentication delete` | `auth_delete_resource` | Delete authentication record |
| `ts authentication list` | `auth_list_resources` | List authentication records |
| `ts authentication overview` | `auth_get_overview` | Get authentication overview |
| `ts authentication save` | `auth_save_resource` | Save authentication record |
| `ts authentication sections` | `auth_describe_sections` | Describe authentication sections |
| `ts authentication strategy` | `auth_set_strategy` | Set sign-in strategy |
| `ts backups create` | `create_backup` | Create backup |
| `ts backups list` | `list_backups` | List backups |
| `ts backups policy` | `set_backup_policy` | Set backup policy |
| `ts backups restore` | `restore_backup` | Restore backup |
| `ts billing cancel-checkout` | `cancel_checkout` | Cancel plan checkout |
| `ts billing change-plan` | `change_plan` | Change plan |
| `ts billing create-checkout` | `create_checkout` | Start plan checkout |
| `ts billing invoices` | `list_invoices` | List invoices |
| `ts billing plans` | `list_plans` | List plans |
| `ts billing portal` | `get_billing_portal_url` | Open billing portal |
| `ts billing preview-plan-change` | `preview_plan_change` | Preview plan change |
| `ts billing show` | `get_billing` | Get billing |
| `ts billing undo-plan-change` | `undo_plan_change` | Undo scheduled plan change |
| `ts context show` | `get_context` | Get context |
| `ts data apply-index-recommendation` | `apply_index_recommendation` | Apply index recommendation |
| `ts data check-sql` | `check_sql` | Check SQL |
| `ts data create-document` | `create_document` | Create document |
| `ts data create-index` | `create_index` | Create index |
| `ts data delete-document` | `delete_document` | Delete document |
| `ts data delete-saved-query` | `delete_saved_query` | Delete saved query |
| `ts data get-collection-schema` | `get_collection_schema` | Get collection schema |
| `ts data get-document` | `get_document` | Get document |
| `ts data get-document-history` | `get_document_history` | Get document history |
| `ts data get-index-migration` | `get_index_migration` | Get index migration |
| `ts data list-collections` | `list_collections` | List collections |
| `ts data list-documents` | `list_documents` | List documents |
| `ts data list-index-recommendations` | `list_index_recommendations` | List index recommendations |
| `ts data list-indexes` | `list_indexes` | List indexes |
| `ts data list-saved-queries` | `list_saved_queries` | List saved queries |
| `ts data patch-document` | `patch_document` | Patch document |
| `ts data replace-document` | `replace_document` | Replace document |
| `ts data run-sql` | `run_sql` | Run SQL |
| `ts data save-query` | `save_query` | Save query |
| `ts data set-collection-schema` | `set_collection_schema` | Set collection schema |
| `ts databases branch` | `branch_database` | Branch database |
| `ts databases create` | `create_database` | Create database |
| `ts databases delete` | `delete_database` | Delete database |
| `ts databases get` | `get_database` | Get database |
| `ts databases list` | `list_databases` | List databases |
| `ts keys create` | `create_api_key` | Create API key |
| `ts keys create-m2m-client` | `create_m2m_client` | Create M2M client |
| `ts keys list` | `list_api_keys` | List API keys |
| `ts keys revoke` | `revoke_api_key` | Revoke API key |
| `ts keys rotate` | `rotate_api_key` | Rotate API key |
| `ts notifications list` | `list_notifications` | List notifications |
| `ts notifications read` | `mark_notification_read` | Mark notification read |
| `ts notifications read-all` | `mark_all_notifications_read` | Mark all notifications read |
| `ts onboarding complete` | `save_onboarding_step` | Save onboarding step |
| `ts onboarding show` | `get_onboarding` | Get onboarding |
| `ts organizations confirm-ownership-transfer` | `confirm_ownership_transfer` | Confirm ownership transfer |
| `ts organizations create` | `create_organization` | Create organization |
| `ts organizations get` | `get_organization` | Get organization |
| `ts organizations leave` | `leave_organization` | Leave organization |
| `ts organizations rename` | `rename_organization` | Rename organization |
| `ts organizations request-deletion` | `request_organization_deletion` | Request organization deletion |
| `ts organizations request-ownership-transfer` | `request_ownership_transfer` | Request ownership transfer |
| `ts organizations select` | `select_organization` | Select organization |
| `ts overview show` | `get_overview` | Get overview |
| `ts profile list-access-tokens` | `list_access_tokens` | List access tokens |
| `ts profile revoke-access-token` | `revoke_access_token` | Revoke access token |
| `ts profile set-language` | `set_language` | Set language |
| `ts profile show` | `get_profile` | Get profile |
| `ts profile update` | `update_profile` | Update profile |
| `ts projects create` | `create_project` | Create project |
| `ts projects select` | `select_project` | Select project |
| `ts projects update` | `update_project` | Update project |
| `ts settings delete-project` | `delete_project` | Delete project |
| `ts settings set-audit-retention` | `set_audit_retention` | Set audit retention |
| `ts settings set-project-authentication` | `set_project_authentication` | Set project authentication |
| `ts settings show` | `get_project_settings` | Get project settings |
| `ts subscriptions attach` | `attach_query_subscription` | Attach query subscription |
| `ts subscriptions detach` | `detach_query_subscription` | Detach query subscription |
| `ts subscriptions list` | `list_query_subscriptions` | List query subscriptions |
| `ts subscriptions pause` | `pause_query_subscription` | Pause query subscription |
| `ts subscriptions resume` | `resume_query_subscription` | Resume query subscription |
| `ts usage set-spending-controls` | `set_spending_controls` | Set spending controls |
| `ts usage show` | `get_usage` | Get usage |

The same groups are available under `ts dashboard`.
`ts dashboard tools list` discovers the actions available to your role
on the connected server. `tools call TOOL --input @file.json` supports newly
published actions before the named command catalog is regenerated.
