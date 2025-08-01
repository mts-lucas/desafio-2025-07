from pydantic import BaseModel


class TextInput(BaseModel):
    text: str

class FormattedText(BaseModel):
    original_text: str
    formatted_text: str

class JustifiedText(BaseModel):
    original_text: str
    justified_text: str