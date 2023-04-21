# spec-pilot

## Description

Spec-pilot is a project that uses Natural Language Processing (NLP) to help create OpenAPI specifications. It consists of two main parts: a spec generator and a spec parser. The spec generator provides templates for creating different parts of an OpenAPI specification, while the spec parser uses NLP to parse natural language input and modify the OpenAPI specification accordingly.

## Documentation

Information on spec-pilot's integrations, roadmap, and other features can be found in the [documentation](./docs/index.md)

## Installation

To use spec-pilot, you must have Python 3 installed on your machine. Clone the repository from GitHub and install the required packages by running the following command in the project directory:

```sh
pip install -r requirements.txt
```

## Usage

### Spec Generator

The spec generator consists of several modules in the src/ directory, each of which provides functions for generating different parts of an OpenAPI specification. The templates/ directory contains Mustache templates used by the generator. Here are the main modules:

**openapi_spec_generator.py**: 
This module contains functions for generating various parts of an OpenAPI spec, including schemas, paths, parameters, responses, tags, servers, contacts, and licenses. To use this module, import the relevant function and provide the necessary arguments. For example, to generate a schema for a v3.0 OpenAPI specification, you would use the following code:

```python

from spec_pilot import generate_schema

context = {
    "schema_name": "MySchema",
    "schema_properties": {
        "property1": {"type": "string"},
        "property2": {"type": "integer"}
    }
}

generate_schema(context, output_file="myschema.yaml", version="v3.0")
```

### Spec Parser

The spec parser uses NLP to parse natural language input and modify an existing OpenAPI specification accordingly. The spec_parser.py module provides functions for this purpose. To use the spec parser, import the relevant function and provide a natural language input and the current state of the OpenAPI specification. For example, to add a property to a schema in the OpenAPI specification, you would use the following code:

```python
from spec_pilot import process_natural_language_input

input_text = "Add a 'description' property to the 'MySchema' schema"
openapi_spec = {"components": {"schemas": {"MySchema": {"type": "object", "properties": {}}}}}

modified_spec = process_natural_language_input(input_text, openapi_spec)
```

## Validator

This project will be using [vacuum linter](https://quobix.com/vacuum/)
If it is not present, there are two options
Either via a docker container

```sh
docker dshanley/vacuum lint <my-openapi-spec.yaml>
```

or curl

```sh
curl -fsSL https://quobix.com/scripts/install_vacuum.sh | sh 
```

[Customized rulesets](./lint-rulesets/) can be fed to the linter, this implementation is significantly faster than any linter in js or python

## Contributing

If you would like to contribute to spec-pilot, please fork the repository and submit a pull request with your changes. Please make sure to include tests and update the documentation as necessary.

## License

Spec-pilot is licensed under the GNU General Public License v3.0. See LICENSE.txt for more information.
