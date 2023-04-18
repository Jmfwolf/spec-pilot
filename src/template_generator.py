import pystache
import os

def init_project():
    project_name = input("Enter a name for your project: ")
    
    # Create the main project directory
    os.mkdir(project_name)
    print(f"Created project directory: {project_name}")
    
    # Create subdirectories for each generatable item type
    subdirectories = ["schemas", "path_objects", "parameters", "info", "headers", "media_types", "responses", "parameter_objects", "tags", "servers", "contact", "license"]
    for subdir in subdirectories:
        os.mkdir(os.path.join(project_name, subdir))
        print(f"Created {subdir} directory")

def render_template(template_file, context, output_file):
    with open(template_file, 'r') as f:
        template = f.read()
    rendered = pystache.render(template, context)

    with open(output_file, 'w') as f:
        f.write(rendered)

def check_version(version):
    if version != 'v2.0' and version != 'v3.0':
        raise ValueError("Version must be either 'v2.0' or 'v3.0'")

def generate_schema(context, output_file='schema.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/schema.mustache", context, output_file)

def generate_path_object(context, output_file='path_object.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/path_object.mustache", context, output_file)

def generate_parameter(context, output_file='parameter.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/parameter.mustache", context, output_file)

def generate_info(context, output_file='info.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/info.mustache", context, output_file)

def generate_header(context, output_file='header.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/header.mustache", context, output_file)

def generate_media_type(context, output_file='media_type.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/media_type.mustache", context, output_file)

def generate_response(context, output_file='response.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/response.mustache", context, output_file)

def generate_parameter_object(context, output_file='parameter_object.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/parameter_object.mustache", context, output_file)

def generate_tag(context, output_file='tag.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/tag.mustache", context, output_file)

def generate_server(context, output_file='server.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/server.mustache", context, output_file)

def generate_contact(context, output_file='contact.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/contact.mustache", context, output_file)

def generate_license(context, output_file='license.yaml', version='v2.0'):
    check_version(version)
    render_template(f"templates/{version}/license.mustache", context, output_file)



# Example usage
schema_context = {
    'schemaName': 'Book',
    'type': 'object',
    'properties': [
        {'name': 'title', 'type': 'string', 'description': 'The title of the book', 'example': 'The Catcher in the Rye'},
        {'name': 'author', 'type': 'string', 'description': 'The author of the book', 'example': 'J.D. Salinger'},
        {'name': 'publication_date', 'type': 'string', 'description': 'The publication date of the book', 'example': '1951-07-16', 'additionalProperties': {'format': 'date'}}
    ],
    'required': [
        {'name': 'title'},
        {'name': 'author'}
    ],
    'description': 'A book in the library.'
}

generate_schema(schema_context, 'generated_schema.yaml')

path_object_context = {
    'path': '/books',
    'httpMethod': 'post',
    'summary': 'Create a new book',
    'description': 'Creates a new book in the library',
    'operationId': 'createBook',
    'tags': [{'tag': 'Books'}],
    'parameters': [],
    'requestBodyDescription': 'Book object to be created',
    'requestBodyRequired': True,
    'mediaType': 'application/json',
    'schemaName': 'Book',
    'statusCode': '201',
    'responseDescription': 'Book successfully created',
}

generate_path_object(path_object_context, 'generated_path_object.yaml')

parameter_context = {
    'parameterName': 'bookId',
    'name': 'id',
    'in': 'path',
    'description': 'The unique identifier of the book',
    'required': True,
    'type': 'string',
    'example': 'b1c4d2e5',
}

generate_parameter(parameter_context, 'generated_parameter.yaml')

info_context = {
    'title': 'Library API',
    'description': 'An API to manage books and shelves in a digital library',
    'version': '1.0.0',
    'contactName': 'Library API Support',
    'contactUrl': 'https://example.com/support',
    'contactEmail': 'support@example.com',
    'licenseName': 'Apache 2.0',
    'licenseUrl': 'https://www.apache.org/licenses/LICENSE-2.0',
}

generate_info(info_context, 'generated_info.yaml')

