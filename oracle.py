import json
import os
from typing import List, TypeVar
from dataclasses import dataclass

O = TypeVar("O", bound="Oracle")


@dataclass
class Field:
    name: str
    data_type: str


class Oracle:
    def __init__(self, name: str, fields: List[Field], space: int) -> None:
        self.name = name
        self.fields = fields
        self.space = space

    @classmethod
    def from_file(cls, path: str) -> O:
        """Loads an oracle from a schema file"""
        if not os.path.exists(path):
            raise SystemExit(f'Invalid oracle schema path: {path}')

        with open(path, 'r') as file:
            contents = file.read()
            raw = json.loads(contents)
        
        return cls(raw['name'], raw['fields'], raw['space'])
