import os
import subprocess
from jinja2 import Template


def load_template_from_file(path: str) -> Template:
    """Loads a template from a file"""
    if not os.path.exists(path):
        raise SystemExit(f'Invalid contract template path: {path}')

    with open(path, 'r') as file:
        contents = file.read()
        template = Template(contents)

    return template


def create_anchor_project(name: str) -> None:
    """Runs anchor init"""
    subprocess.run(['anchor', 'init', name])


def build_anchor_project(name: str) -> None:
    """Runs anchor build"""
    subprocess.call('anchor build', shell=True, cwd=f'./{name}')


def overwrite_contract(name: str, contract_render: str) -> None:
    """Overwrites anchor's generated lib.rs"""
    lib_path = f'{name}/programs/{name}/src/lib.rs'
    if not os.path.exists(lib_path):
        raise SystemExit(f'Invalid lib.rs path: {lib_path}')

    with open(lib_path, 'w') as file:
        file.write(contract_render)


def overwrite_tests(name: str, tests_render: str) -> None:
    """Overwrites anchor's generated testing script"""
    tests_path = f'{name}/tests/{name}.ts'
    if not os.path.exists(tests_path):
        raise SystemExit(f'Invalid testing path: {tests_path}')

    with open(tests_path, 'w') as file:
        file.write(tests_render)
