from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
import re
import json

def aws_apigateway_compatible(openapi_spec):
    errors = []
    spec, spec_url = read_from_filename(openapi_spec)
    validate_spec(spec)
    # Helper function to check if a string is alphanumeric
    def is_alphanumeric(s):
        return s.isalnum()

    # Check if path segments are valid
    path_pattern = re.compile(r'^[a-zA-Z0-9_,.:{}-]+$')
    for path in spec.get('paths', {}):
        path_segments = path.split('/')
        for segment in path_segments:
            if segment and not path_pattern.match(segment):
                errors.append(f"Invalid path segment: {segment}")

    # Check if model names are valid
    for model_name in spec.get('components', {}).get('schemas', {}):
        if not is_alphanumeric(model_name):
            errors.append(f"Invalid model name: {model_name}")

    # Check if securitySchemes type is apiKey
    security_schemes = spec.get('components', {}).get('securitySchemes', {})
    for scheme_name, scheme in security_schemes.items():
        if scheme.get('type') != 'apiKey':
            errors.append(f"Invalid securitySchemes type for {scheme_name}: {scheme.get('type')}")

    # Check if discriminator is used in any schema object
    for schema_name, schema in spec.get('components', {}).get('schemas', {}).items():
        if 'discriminator' in schema:
            errors.append(f"discriminator is not supported in schema: {schema_name}")

    # Check if the default keyword is used
    def check_default(obj, path):
        for key, value in obj.items():
            if key == 'default':
                errors.append(f"default keyword is not supported in {path}")
            elif isinstance(value, dict):
                check_default(value, f"{path}.{key}")

    check_default(spec, '')

    return len(errors) == 0, errors


res = aws_apigateway_compatible('../examples/appwrite.yml')
print(res)