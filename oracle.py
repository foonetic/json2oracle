import json
import os
from typing import List
from dataclasses import dataclass

@dataclass
class Field:
    name: str
    data_type: str

class Oracle:
    def __init__(self, name: str, fields: List[Field], space: int):
        self.name = name
        self.fields = fields
        self.space = space
    
    @classmethod
    def from_file(cls, path: str):
        if not os.path.exists(path):
            raise SystemExit(f'Invalid oracle schema path: {path}')
            
        with open(path, 'r') as file:
            contents = file.read()
            raw = json.loads(contents)
        oracle = Oracle(raw['name'], raw['fields'], raw['space'])

        return oracle