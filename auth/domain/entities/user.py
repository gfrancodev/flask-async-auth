from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from uuid import uuid4
from json import dumps
from datetime import datetime

"""
if 
  elif
      else 
      
if
  if
    if
      
def 
    if return 
    if not
    if 

Early Return
"""

class User(BaseModel):
    id: str = Field(str(uuid4())) 
    name: Optional[str] = Field(..., title="Name", description="Nome não é obrigatorio")
    email: EmailStr = Field(...)
    username: Optional[str] = Field(..., min_length=3, max_length=20)
    password: str = Field(..., title="Password") 
    created_at: Optional[str] = Field(datetime.now().isoformat())
    updated_at: Optional[str] = Field(datetime.now().isoformat())
       
    @field_validator('username')
    @classmethod
    def transform_username(cls, value):
        return f"@{value}"  
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        # deve ser maior que 8 digitos
        # dever no minimo uma letra maiucula
        # dever no minimo letra minsucula
        # dever no minimo um numero
        # dever no minimo um caracter especial
        # deve ter até 20 digitos
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characteres long')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit')
        
        if not any(char.isalpha() for char in value):
            raise ValueError('Password must contain at least one upper letter')
        
        if not any(char.islower() for char in value):
            raise ValueError('Password must contain at least lower letter')
        
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one upper letter')
    
        if not any(not char.isalnum() for char in value):
            raise ValueError('Password must contain at least one alphanumeric charactere')    
        
        if len(value) > 20:
            raise ValueError('Password must be at least 20 characteres short')
        
        return f"{value}"
    
payload = {
    "name": "Gustavo",
    "username": "gfrancodev",
    "email": "gustavo.franco@gmail.com",
    "password": "hdjasdasdH8@",
}

user = User(**payload)
print(dumps(user.model_dump(), indent=2))