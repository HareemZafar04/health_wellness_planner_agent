from agents import Agent as BaseAgent, RunContextWrapper

class EscalationAgent(BaseAgent):
    """
    Handoff agent connecting user to a human coach.
    """
    def __init__(self, context: RunContextWrapper):
        super().__init__(
            name="EscalationAgent",
            instructions="Connect the user to a human coach.",
            tools=[],
            context=context,
        )

    def run(self, user_input: str):
        return "You’re being connected to a human coach now."
