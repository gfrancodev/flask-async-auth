from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

class Code(BaseModel): 
    id: str = uuid4()
    code: str 
    type: str 
    status: str 
    created_at: datetime
    updated_at: datetime

