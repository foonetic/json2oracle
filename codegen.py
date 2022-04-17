import os
import subprocess
from jinja2 import Template

def load_contract_template(path: str) -> Template:
    if not os.path.exists(path):
        raise SystemExit(f'Invalid contract template path: {path}')
        
    with open(path, 'r') as file:
        contents = file.read()
        template = Template(contents)

    return template
    
def create_anchor_project(name: str, contract_render: str):
    subprocess.run(['anchor', 'init', name])
    
    lib_path = f'{name}/programs/{name}/src/lib.rs'
    if not os.path.exists(lib_path):
        raise SystemExit(f'Invalid lib.rs path: {path}')

    with open(lib_path, 'w') as file:
        file.write(contract_render)
    
    subprocess.call('anchor build', shell=True, cwd=f'./{name}')