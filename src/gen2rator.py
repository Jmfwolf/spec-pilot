import os
import yaml
import pystache

def init_project(project_name):
    # create a project directory
    os.makedirs(project_name, exist_ok=True)

    # create a directory in the project for: schemas, resources, responses, and parameters
    os.makedirs(os.path.join(project_name, "schemas"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "resources"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "responses"), exist_ok=True)
    os.makedirs(os.path.join(project_name, "parameters"), exist_ok=True)

def render_template(asset_type, context, output_file, version="v3.0"):
    check_version(version)

    # use the mustache template
    template_file = os.path.join("templates", version, f"{asset_type}.mustache")
    with open(template_file, "r") as f:
        template = f.read()
    rendered = pystache.render(template, context)
    
    with open(output_file, "w") as f:
        f.write(rendered)

def check_requirements(asset_type, schema):
    if asset_type == "parameter":
        required_keys = ["in", "name", "schema", "required"]
        for key in required_keys:
            if key not in schema:
                raise ValueError(f"{key} is missing in the parameter schema")
    # Add checks for other asset types: schemas, resources, responses
    # as well as the info prompt that a user will need to complete

def check_version(version):
    if version != 'v2.0' and version != 'v3.0':
        raise ValueError("Version must be either 'v2.0' or 'v3.0'")

def generate_openapi_spec(project_name, version='v3.0', output_file='openapi_spec.yaml'):
    check_version(version)

    openapi_spec = {
        "openapi": version,
        "info": {},
        "paths": {},
        "components": {
            "schemas": {},
            "parameters": {},
            "responses": {}
        }
    }

    # Add info from info.yaml if it exists
    info_file = os.path.join(project_name, "info", "info.yaml")
    if os.path.exists(info_file):
        with open(info_file, 'r') as f:
            openapi_spec['info'] = yaml.safe_load(f)

    # Load content from yaml files in subdirectories
    for subdir, _, files in os.walk(project_name):
        for file in files:
            if file.endswith(".yaml"):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = yaml.safe_load(f)

                if subdir.endswith("schemas"):
                    openapi_spec['components']['schemas'][file[:-5]] = content
                elif subdir.endswith("resources"):
                    openapi_spec['paths'].update(content)
                elif subdir.endswith("parameters"):
                    openapi_spec['components']['parameters'][file[:-5]] = content
                elif subdir.endswith("responses"):
                    openapi_spec['components']['responses'][file[:-5]] = content

    # Write the merged OpenAPI spec to the output file
    with open(os.path.join(project_name, output_file), 'w') as f:
        yaml.dump(openapi_spec, f, sort_keys=False, default_flow_style=False)

def demo():
    print("Initializing demo project...")
    project_name = "demo_project"
    init_project(project_name)

    # create a demonstration to show it works
    asset_type = "parameter"
    context = {
        "in": "query",
        "name": "example_parameter",
        "schema": {
            "type": "string"
        },
        "required": True
    }
    output_file = os.path.join(project_name, "parameters", "example_parameter.yaml")
    render_template(asset_type, context, output_file)

    print("Demo project initialized with an example parameter.")

if __name__ == "__main__":
    demo()