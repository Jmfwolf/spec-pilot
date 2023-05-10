import argparse
import yaml
import os
from .prompt_builder import PromptBuilder
from .generator import Generator
from .validator import Validator

def create_project_structure(project_name):
    # create a project directory
    os.makedirs(project_name, exist_ok=True)

    # create a directory in the project for: schemas, resources, responses, and parameters
    os.makedirs(os.path.join(project_name, "schemas"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "resources"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "responses"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "parameters"), exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="Create and manage OpenAPI specifications.")
    parser.add_argument("--init", type=str, help="Initialize a new project")
    parser.add_argument("--wizard", action="store_true", help="Run the OpenAPI Spec wizard")
    parser.add_argument("--output", type=str, default="openapi.yaml", help="Output file for the generated OpenAPI specification")
    parser.add_argument("--validate", type=str, help="Validate an OpenAPI specification YAML file")

    args = parser.parse_args()

    if args.init:
        create_project_structure(args.init)

    elif args.wizard:
        prompt_builder = PromptBuilder()
        description = prompt_builder.prompt()

        generator = Generator(description)
        openapi_spec = generator.generate_spec()

        with open(args.output, "w") as output_file:
            yaml_spec = yaml.safe_load(openapi_spec)
            yaml.dump(yaml_spec, output_file, default_flow_style=False, sort_keys=False)
    
    elif args.validate:
        validator = Validator()
        validation_result = validator.validate(args.validate)

        if validation_result["valid"]:
            print(f"The OpenAPI specification file '{args.validate}' is valid.")
        else:
            print(f"Errors found in the OpenAPI specification file '{args.validate}':")
            for error in validation_result["errors"]:
                print(f"- {error}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()