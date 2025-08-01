from fastapi import APIRouter, HTTPException
from services import formatter

from schemas.text import FormattedText, JustifiedText, TextInput

router = APIRouter(prefix="/formatters", tags=["formatters"])

@router.post("/wrap/", response_model=FormattedText)
def text_wrap(request: TextInput):
    if not request.text:
        raise HTTPException(status_code=404, detail="Text é um campo obrigatório")
    
    wrapped = formatter.wrap_text(request.text, request.width)
    return FormattedText(
        original_text=request.text,
        formatted_text=wrapped,
        width=request.width
    )


@router.post("/justify/", response_model=JustifiedText)
def text_justify(request: TextInput):
    if not request.text:
        raise HTTPException(status_code=404, detail="Text é um campo obrigatório")
    
    justified = formatter.justify_text(request.text, request.width)
    return JustifiedText(
        original_text=request.text,
        justified_text=justified,
        width=request.width
    )