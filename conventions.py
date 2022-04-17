import re
import string

def to_snake_case(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()

def to_pascal_case(name: str) -> str:
    name = string.capwords(name.replace("_", " ")).replace(" ", "")
    return name