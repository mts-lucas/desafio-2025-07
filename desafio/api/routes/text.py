from fastapi import APIRouter, HTTPException
from services import formatter

from schemas.text import FormattedText, JustifiedText, TextInput

router = APIRouter(prefix="/formatters", tags=["formatters"])

@router.post("/wrap/", response_model=FormattedText)
def text_wrap(request: TextInput):
    """
    Formata o texto inserido de acordo com o numero de caracteres fornecido com default = 50.

    AVISO: Este endpoint aceita o texto apenas com quebra de linha usando *`\\n`** ou *`\\n\\n`**
    """
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
    """
    Formata o texto inserido de acordo com o numero de caracteres fornecido com default = 50 e justifica o texto.

    AVISO: Este endpoint aceita o texto apenas com quebra de linha usando *`\\n`** ou *`\\n\\n`**
    """
    if not request.text:
        raise HTTPException(status_code=404, detail="Text é um campo obrigatório")
    
    justified = formatter.justify_text(request.text, request.width)
    return JustifiedText(
        original_text=request.text,
        justified_text=justified,
        width=request.width
    )