# Spec-Pilot

Spec-Pilot is a Python package that allows you to generate OpenAPI specifications using natural language. It simplifies the process of creating API documentation by allowing users to describe the API using everyday language.

## Features

- Initialize new OpenAPI projects with ease.
- Generate OpenAPI specifications from natural language input.
- Modify existing OpenAPI specifications using natural language.
- Validate generated OpenAPI specifications.
- Demo functionality available to test the package.

## Installation

To install Spec-Pilot, run:

```bash
pip install spec-pilot
```

After installing Spec-Pilot, you also need to download the spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Once installed, you can use Spec-Pilot from the command line or as a Python package.

### Command Line Usage

Initialize a new OpenAPI project:

```bash
spec-pilot --init project_name
```

Generate the OpenAPI specification for an existing project:

```bash
spec-pilot --generate project_name
```

Modify an OpenAPI specification with natural language input:

```bash
spec-pilot --nlp "Add a GET endpoint /users that returns a list of users"
```

### Python Package Usage

You can also use Spec-Pilot as a Python package in your own projects:

```python
from spec_pilot.generator import init_project, generate_openapi_spec
from spec_pilot.spec_parser import process_natural_language_input

# Initialize a new OpenAPI project
init_project("project_name")

# Generate the OpenAPI specification for an existing project
generate_openapi_spec("project_name")

# Modify an OpenAPI specification with natural language input
with open("openapi_spec.json", "r") as f:
    openapi_spec = json.load(f)

modified_openapi_spec = process_natural_language_input("Add a GET endpoint /users that returns a list of users", openapi_spec)
```

## License

Spec-Pilot is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
