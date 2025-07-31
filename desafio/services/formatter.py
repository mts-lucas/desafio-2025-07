def wrap_text(text: str, width: int) -> list[str]:

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + " " + word) <= width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines
