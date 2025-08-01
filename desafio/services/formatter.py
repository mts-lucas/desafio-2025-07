import textwrap

def wrap_text(text: str, width: int) -> str:
    wrapper = textwrap.TextWrapper(width=width, break_long_words=False, break_on_hyphens=False)
    return '\n'.join(wrapper.wrap(text))


def justify_line_by_char_count(line: str, width: int) -> str:
    words = line.split()
    if len(words) == 1:
        return words[0].ljust(width)

    total_spaces = width - sum(len(word) for word in words)
    gaps = len(words) - 1
    min_space = total_spaces // gaps
    extra = total_spaces % gaps

    justified = ""
    for i, word in enumerate(words[:-1]):
        justified += word
        spaces = min_space + (1 if i < extra else 0)
        justified += " " * spaces
    justified += words[-1]

    return justified


def justify_text(text: str, width: int) -> str:
    lines = textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    
    justified_lines = [justify_line_by_char_count(line, width) for line in lines[:-1]]
    justified_lines.append(lines[-1])
    return '\n'.join(justified_lines)