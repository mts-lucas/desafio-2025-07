from pydantic import BaseModel
from typing import Optional


class TextInput(BaseModel):
    text: str
    width: Optional[int] = 50

class FormattedText(BaseModel):
    original_text: str
    formatted_text: str
    width: int

class JustifiedText(BaseModel):
    original_text: str
    justified_text: str
    width: int