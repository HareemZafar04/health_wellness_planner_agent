from agents import Agent

class NutritionExpertAgent(Agent):
    def __init__(self):
        super().__init__(
            name="NutritionExpertAgent",
            instructions=(
                "You are a certified nutritionist. "
                "Provide evidence-based dietary guidance, especially for "
                "allergies, diabetes, or vegetarian/vegan needs."
            ),
            tools=[],          
        )
