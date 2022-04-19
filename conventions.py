import re
import string


def to_snake_case(name: str) -> str:
    """Converts string to snake case"""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()


def to_pascal_case(name: str) -> str:
    """Converts string to pascal case from snake case"""
    name = string.capwords(name.replace("_", " ")).replace(" ", "")
    return name


def to_camel_case(snake_str: str) -> str:
    """Converts string to camel case from snake case"""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
