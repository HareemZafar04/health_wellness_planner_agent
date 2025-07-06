from pydantic import BaseModel, Field

class GoalInput(BaseModel):
    """Validates a goal like 'lose 5 kg in 2 months'."""
    quantity: float = Field(..., gt=0, description="Numeric amount")
    metric: str     = Field(...,  description="e.g. kg, lbs")
    duration: str   = Field(...,  description="Timeframe, e.g. '6 months'")

class ToolOutput(BaseModel):
    data: dict