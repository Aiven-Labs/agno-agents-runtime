# Agno AgentOS: agent-a + agent-b (Kafka Connect BYOC test)

One AgentOS app serving two agents. `agent-a` writes a short message; `agent-b` translates what it receives into pirate speak.
Called by the `AgnoAgentSinkConnector` via `POST /agents/{id}/runs`.

## Environment variables (set in the Aiven Runtime app, never in git)
| Var | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Key for the LLM. For the Aiven agent gateway, use the gateway key. |
| `ANTHROPIC_BASE_URL` | Optional. Gateway base URL; the Anthropic SDK reads this automatically. Leave unset to call Anthropic directly. |
| `OS_SECURITY_KEY` | Bearer token required on every call. Use the same value as `agno.bearer.token` in the connector config. |
| `MODEL_ID` | Optional, default `claude-sonnet-4-6`. Use whatever model id the gateway exposes. |

Port 8080, health at `/health`.

Note: AgentOS returns HTTP 200 with `status: "ERROR"` when the LLM call fails; the connector treats that as a failure.
