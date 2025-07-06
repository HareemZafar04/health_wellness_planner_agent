<<<<<<< HEAD
from pydantic import BaseModel, Field

class GoalInput(BaseModel):
    """Validates a goal like 'lose 5 kg in 2 months'."""
    quantity: float = Field(..., gt=0, description="Numeric amount")
    metric: str     = Field(...,  description="e.g. kg, lbs")
    duration: str   = Field(...,  description="Timeframe, e.g. '6 months'")

class ToolOutput(BaseModel):
=======
from pydantic import BaseModel, Field

class GoalInput(BaseModel):
    """Validates a goal like 'lose 5 kg in 2 months'."""
    quantity: float = Field(..., gt=0, description="Numeric amount")
    metric: str     = Field(...,  description="e.g. kg, lbs")
    duration: str   = Field(...,  description="Timeframe, e.g. '6 months'")

class ToolOutput(BaseModel):
>>>>>>> faa8bc7afdfe6f43f8569794d231ee58b8d13116
    data: dict