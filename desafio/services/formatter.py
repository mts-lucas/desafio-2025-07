import textwrap

def wrap_text(text: str, width: int) -> list[str]:
    wrapper = textwrap.TextWrapper(width=width, break_long_words=False, break_on_hyphens=False)
    return wrapper.wrap(text)
