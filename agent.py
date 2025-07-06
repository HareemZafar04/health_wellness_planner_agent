<<<<<<< HEAD
from agents import Agent, handoff, Runner, ModelSettings, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.workout_recomender import workout_recommender
from tools.scheduler import scheduler
from tools.tracker import tracker
from custom_agents.nutrition_expert_agent import NutritionExpertAgent
from custom_agents.injury_support_agent import InjurySupportAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Use the appropriate Gemini model
    openai_client=external_client
)

class PlannerAgent(Agent):
    """Chat-first AI for personalised health & wellness planning."""

    def __init__(self) -> None:
        super().__init__(
            # Identity
            name="Health & Wellness Planner",
            instructions=(
                "You are an AI health-and-wellness planner. "
                "Collect user goals, generate personalised meal and workout plans, "
                "schedule check-ins, log progress, and hand off to specialists when needed."
            ),
            # Model
            model=model,  # Use Gemini model
            model_settings=ModelSettings(
                temperature=0.7,
                top_p=1.0,
                parallel_tool_calls=True,
            ),
            # Core tools
            tools=[
                goal_analyzer,
                meal_planner,
                workout_recommender,
                scheduler,
                tracker,
            ],
            # Specialist hand-offs
            handoffs=[
                NutritionExpertAgent(),  # tool: transfer_to_nutrition_expert_agent
                handoff(
                    InjurySupportAgent(),
                    tool_name_override="transfer_to_injury_support",
                    tool_description_override=(
                        "Send the user to InjurySupportAgent when they mention pain, "
                        "injury, or require low-impact exercise modifications."
                    ),
                ),
            ],
        )

    # Convenience helper for blocking unit tests / scripts
    def run_sync(self, prompt: str, context):
=======
from agents import Agent, handoff, Runner, ModelSettings, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.workout_recomender import workout_recommender
from tools.scheduler import scheduler
from tools.tracker import tracker
from custom_agents.nutrition_expert_agent import NutritionExpertAgent
from custom_agents.injury_support_agent import InjurySupportAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Use the appropriate Gemini model
    openai_client=external_client
)

class PlannerAgent(Agent):
    """Chat-first AI for personalised health & wellness planning."""

    def __init__(self) -> None:
        super().__init__(
            # Identity
            name="Health & Wellness Planner",
            instructions=(
                "You are an AI health-and-wellness planner. "
                "Collect user goals, generate personalised meal and workout plans, "
                "schedule check-ins, log progress, and hand off to specialists when needed."
            ),
            # Model
            model=model,  # Use Gemini model
            model_settings=ModelSettings(
                temperature=0.7,
                top_p=1.0,
                parallel_tool_calls=True,
            ),
            # Core tools
            tools=[
                goal_analyzer,
                meal_planner,
                workout_recommender,
                scheduler,
                tracker,
            ],
            # Specialist hand-offs
            handoffs=[
                NutritionExpertAgent(),  # tool: transfer_to_nutrition_expert_agent
                handoff(
                    InjurySupportAgent(),
                    tool_name_override="transfer_to_injury_support",
                    tool_description_override=(
                        "Send the user to InjurySupportAgent when they mention pain, "
                        "injury, or require low-impact exercise modifications."
                    ),
                ),
            ],
        )

    # Convenience helper for blocking unit tests / scripts
    def run_sync(self, prompt: str, context):
>>>>>>> faa8bc7afdfe6f43f8569794d231ee58b8d13116
        return Runner.run(self, prompt, context=context)