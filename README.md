# Spec-Pilot

Spec-Pilot is a command-line tool and Python package that helps generate, modify, and validate OpenAPI specifications using natural language processing (NLP). It simplifies the creation and management of OpenAPI projects, making it more accessible to developers and non-developers alike.

## Features

- Initialize new OpenAPI projects
- Generate OpenAPI specifications
- Modify OpenAPI specifications using natural language
- Validate OpenAPI specifications
- Create OpenAPI assets from templates

## Installation

You can install Spec-Pilot using pip:

```bash
pip install spec_pilot
```

After installing Spec-Pilot, you also need to download the spaCy language model:

```bash
python -m spacy download en_core_web_sm
```

## CLI Usage

To use Spec-Pilot as a command-line tool, run the following commands:

- Initialize a new OpenAPI project:

```bash
spec_pilot --init project_name
```

- Generate the OpenAPI specification for a specific project:

```bash
spec_pilot --generate project_name
```

- Modify an existing OpenAPI specification using natural language:

```bash
spec_pilot --nlp "Add a new endpoint called 'get_users' with a GET method"
```

- Validate an OpenAPI specification file:

```bash
spec_pilot --validate spec_file
```

- Create a new OpenAPI asset from a template:

```bash
spec_pilot --create template asset_name output_path
```
## Generate and save your OpenAPI components using the corresponding functions

## Python Package Usage

You can also use Spec-Pilot as a Python package in your projects. Here's an example of how to use it:

```python
from spec_pilot import init_project, generate_openapi_spec, process_natural_language_input, vacuum, render_template

# Initialize a new OpenAPI project
init_project("project_name")

# Generate the OpenAPI specification for a specific project
generate_openapi_spec("project_name")

# Modify an existing OpenAPI specification using natural language
modified_openapi_spec = process_natural_language_input("Add a new endpoint called 'get_users' with a GET method", openapi_spec)

# Validate an OpenAPI specification file
vacuum(["validate", "spec_file"])

# Create a new OpenAPI asset from a template
render_template("template", "asset_name", "output_path")
```

## Limitations of NLP Functionality

Spec-Pilot's NLP functionality is currently limited and may not understand all possible natural language inputs. It can handle basic operations such as adding, updating, and removing endpoints, methods, and parameters. However, it might not handle complex operations or understand all possible variations of natural language expressions.

## Roadmap

To improve the NLP functionality and make Spec-Pilot more complete, we plan to:

1. Expand the range of natural language expressions that can be understood by the tool.
2. Add support for more complex operations, such as modifying response schemas and security settings.
3. Enhance error handling and provide better feedback to users when their input cannot be understood or processed.
4. Integrate with more advanced NLP libraries or services to improve the overall performance and accuracy of the tool.

We encourage users to provide feedback and contribute to the development of Spec-Pilot to make it more robust and feature-rich.

## License

Spec-Pilot is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
