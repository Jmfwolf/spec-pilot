# OpenAPI Spec Generator

OpenAPI Spec Generator is a Python script that helps you generate a valid and working OpenAPI specification from various OpenAPI components, including schemas, paths, parameters, responses, tags, servers, contacts, and licenses. The script leverages the pystache library for template rendering and supports both OpenAPI v2.0 and v3.0.

## Features

- Initialize an OpenAPI project with the required directory structure
- Generate OpenAPI components using customizable templates
- Combine and generate a complete OpenAPI specification from the generated components

## Requirements

    Python 3.x
    PyYAML
    pystache

You can install these libraries using the following pip command:

```sh
pip install PyYAML pystache
```

## Usage

Import the script into your project and call the init_project() function to create a new OpenAPI project directory with the required structure:

```python

from openapi_spec_generator import init_project

project_name = "my_project"
init_project(project_name)
```
Use the provided functions to generate individual OpenAPI components using customized context data and store them in the corresponding directories in the project folder:


```python

from openapi_spec_generator import generate_schema, generate_path_object, generate_parameter, generate_info, generate_contact, generate_license, generate_response, generate_server, generate_tag

```
## Generate and save your OpenAPI components using the corresponding functions

Finally, call the generate_openapi_spec() function to generate the complete OpenAPI specification from the generated components:

```python

from openapi_spec_generator import generate_openapi_spec

generate_openapi_spec(project_name, version='v3.0', output_file='openapi_spec.yaml')
```

## Demo

A demo() function is provided in the script to demonstrate how to use the OpenAPI Spec Generator. You can run the demo by simply calling the function:

```python

from openapi_spec_generator import demo

demo()
```
This will create a sample OpenAPI project, generate some components, and output an OpenAPI specification file named openapi_spec.yaml.

## Contributing

We welcome contributions to improve and extend OAS Maker. To contribute, please fork the repository, make your changes, and submit a pull request.

## License

OAS Maker is released under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for more information.
