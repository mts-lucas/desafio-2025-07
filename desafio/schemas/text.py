from pydantic import BaseModel


class TextInput(BaseModel):
    text: str
    width: int = 50

class FormattedText(BaseModel):
    original_text: str
    formatted_text: str
    width: int

class JustifiedText(BaseModel):
    original_text: str
    justified_text: str
    width: int