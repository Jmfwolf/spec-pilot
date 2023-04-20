import pystache
import os
import yaml

def init_project(project_name):
    if project_name == "":
        project_name = input("Enter project name: ")
    os.mkdir(project_name)
    os.mkdir(os.path.join(project_name, "schemas"))
    os.mkdir(os.path.join(project_name, "paths"))
    os.mkdir(os.path.join(project_name, "parameters"))
    os.mkdir(os.path.join(project_name, "responses"))
    os.mkdir(os.path.join(project_name, "tags"))
    os.mkdir(os.path.join(project_name, "servers"))
    os.mkdir(os.path.join(project_name, "contacts"))
    os.mkdir(os.path.join(project_name, "licenses"))

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
    
def generate_openapi_spec(project_name, version='v3.0', output_file='openapi_spec.yaml'):
    check_version(version)

    openapi_spec = {
        'openapi': '3.0.0' if version == 'v3.0' else '2.0',
        'info': {},
        'paths': {},
        'components': {
            'schemas': {},
            'parameters': {},
            'responses': {},
            'headers': {},
            'requestBodies': {},
            'securitySchemes': {}
        },
        'tags': [],
        'servers': []
    }

    if os.path.exists(os.path.join(project_name, "info", "info.yaml")):
        with open(os.path.join(project_name, "info", "info.yaml"), 'r') as f:
            openapi_spec['info'] = yaml.safe_load(f)

    for subdir, dirs, files in os.walk(project_name):
        for file in files:
            if file.endswith(".yaml"):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = yaml.safe_load(f)

                if subdir.endswith("schemas"):
                    openapi_spec['components']['schemas'][file[:-5]] = content
                elif subdir.endswith("paths"):
                    openapi_spec['paths'].update(content)
                elif subdir.endswith("parameters"):
                    openapi_spec['components']['parameters'][file[:-5]] = content
                elif subdir.endswith("responses"):
                    openapi_spec['components']['responses'][file[:-5]] = content
                elif subdir.endswith("tags"):
                    openapi_spec['tags'].append(content)
                elif subdir.endswith("servers"):
                    openapi_spec['servers'].append(content)
                elif subdir.endswith("contacts"):
                    openapi_spec['info']['contact'] = content
                elif subdir.endswith("licenses"):
                    openapi_spec['info']['license'] = content

    with open(output_file, 'w') as f:
        yaml.dump(openapi_spec, f, sort_keys=False, default_flow_style=False)

def demo():
    # Example usage
    project_name = "demo"
    init_project(project_name)
    schema_context = {
        'schemaName': 'Book',
        'type': 'object',
        'properties': [
            {'name': 'title', 'type': 'string', 'description': 'The title of the book', 'example': 'The Catcher in the Rye'},
            {'name': 'author', 'type': 'string', 'description': 'The author of the book', 'example': 'J.D. Salinger'},
            {'name': 'publication_date', 'type': 'string', 'description': 'The publication date of the book', 'example': '1951-07-16', 'format': 'date'}
        ],
        'required': ['title', 'author'],
        'description': 'A book in the library.'
    }

    generate_schema(schema_context, os.path.join(f"{project_name}/schemas", 'book.yaml'), version='v3.0')

    path_object_context = {
        'path': '/books',
        'httpMethod': 'post',
        'summary': 'Create a new book',
        'description': 'Creates a new book in the library',
        'operationId': 'createBook',
        'tags': ['Books'],
        'parameters': [
            {
                'parameterName': 'bookId',
                'name': 'id',
                'in': 'path',
                'description': 'The unique identifier of the book',
                'required': True,
                'type': 'string',
                'example': 'b1c4d2e5',
                'parameterFile': os.path.join('parameters', 'bookId.yaml')
            }
        ],
        'requestBodyDescription': 'Book object to be created',
        'requestBodyRequired': True,
        'mediaType': 'application/json',
        'schemaName': 'Book',
        'schemaFile': '#/components/schemas/Book',
        'responses': [
            {
                'statusCode': '201',
                'description': 'Book successfully created',
                'mediaType': 'application/json',
                'schemaName': 'Book',
                'schemaFile': '#/components/schemas/Book',
                'example': {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'publication_date': '1951-07-16'}
            }
        ]
    }
    generate_path_object(path_object_context, os.path.join(f"{project_name}/paths", 'books.yaml'), version='v3.0')

    parameter_context = {
        'parameterName': 'bookId',
        'name': 'id',
        'in': 'path',
        'description': 'The unique identifier of the book',
        'required': True,
        'type': 'string',
        'example': 'b1c4d2e5',
    }

    generate_parameter(parameter_context, os.path.join(f"{project_name}/parameters", 'bookId.yaml'), version='v3.0')

    info_context = {
        'title': 'Library API',
        'description': 'An API to manage books and shelves in a digital library',
        'version': '1.0.0',
        'contact': {
            'name': 'Library API Support',
            'url': 'https://example.com/support',
            'email': 'support@example.com'
        },
        'license': {
            'name': 'Apache 2.0',
            'url': 'https://www.apache.org/licenses/LICENSE-2.0'
        }
    }
    contact_context = {
    'name': 'Library API Support',
    'url': 'https://example.com/support',
    'email': 'support@example.com'
    }

    generate_contact(contact_context, os.path.join(f"{project_name}/contacts", 'library_api_support.yaml'), version='v3.0')

    license_context = {
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0'
    }

    generate_license(license_context, os.path.join(f"{project_name}/licenses", 'apache_2.0.yaml'), version='v3.0')

    responses_context = {
        'statusCode': '200',
        'description': 'Success',
        'mediaType': 'application/json',
        'schemaName': 'Book',
        'schemaFile': os.path.join('schemas', 'book.yaml'),
        'example': {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'publication_date': '1951-07-16'}
    }

    generate_response(responses_context, os.path.join(f"{project_name}/responses", 'success.yaml'), version='v3.0')

    servers_context = {
        'url': 'https://example.com/api',
        'description': 'Production server'
    }

    generate_server(servers_context, os.path.join(f"{project_name}/servers", 'production.yaml'), version='v3.0')

    tags_context = {
        'name': 'Books',
        'description': 'Operations related to books'
    }

    generate_tag(tags_context, os.path.join(f"{project_name}/tags", 'books.yaml'), version='v3.0')

    generate_info(info_context, os.path.join('info.yaml'), version='v3.0')

demo()
generate_openapi_spec("demo")