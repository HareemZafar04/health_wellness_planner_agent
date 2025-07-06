from agents import Agent

class InjurySupportAgent(Agent):
    def __init__(self):
        super().__init__(
            name="InjurySupportAgent",
            instructions=(
                "You are a physiotherapy assistant. "
                "Offer safe, low-impact workout modifications and recovery tips "
                "for users with injuries or chronic pain."
            ),
            tools=[],
        )
