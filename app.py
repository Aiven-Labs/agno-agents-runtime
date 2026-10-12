"""Two Agno agents (agent-a, agent-b) served by one AgentOS app, for the Kafka Connect BYOC test.

Set ANTHROPIC_API_KEY. Set OS_SECURITY_KEY to require `Authorization: Bearer <key>` on every call
(the Kafka connector's `agno.bearer.token`).
"""
import os

from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.os import AgentOS

MODEL_ID = os.getenv("MODEL_ID", "claude-sonnet-4-6")


def model() -> Claude:
    return Claude(id=MODEL_ID)


agent_a = Agent(
    id="agent-a",
    name="agent-a",
    model=model(),
    instructions=[
        "You are Agent A. You exchange messages with Agent B over Kafka.",
        "When a message starts a conversation, write one short friendly message for Agent B (one or two sentences).",
        "When you receive a reply from Agent B, answer with just the single word: Received.",
    ],
)

agent_b = Agent(
    id="agent-b",
    name="agent-b",
    model=model(),
    instructions=[
        "You are Agent B, a pirate translator.",
        "Translate the message you receive into pirate speak. Reply with only the translation, nothing else.",
    ],
)

agent_os = AgentOS(agents=[agent_a, agent_b])
app = agent_os.get_app()
