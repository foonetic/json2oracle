import os
import json
import argparse
from jinja2 import Template

import codegen
import conventions
from oracle import Oracle, Field

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate anchor program for oracle schema")
    parser.add_argument("oracle_schema_path", type=str,
                        help="Path to oracle schema")
    parser.add_argument("contract_template_path", type=str,
                        help="Path to contract template")
    parser.add_argument("tests_template_path", type=str,
                        help="Path to tests template")
    args = parser.parse_args()

    oracle = Oracle.from_file(args.oracle_schema_path)
    contract_template = codegen.load_template_from_file(
        args.contract_template_path)
    contract_render = contract_template.render(
        oracle=oracle,
        to_snake_case=conventions.to_snake_case,
        to_pascal_case=conventions.to_pascal_case)

    tests_template = codegen.load_template_from_file(args.tests_template_path)
    tests_render = tests_template.render(
        oracle=oracle,
        to_snake_case=conventions.to_snake_case,
        to_pascal_case=conventions.to_pascal_case,
        to_camel_case=conventions.to_camel_case)

    codegen.create_anchor_project(oracle.name)
    codegen.overwrite_contract(oracle.name, contract_render)
    codegen.overwrite_tests(oracle.name, tests_render)
    codegen.build_anchor_project(oracle.name)
