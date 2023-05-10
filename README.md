# Spec Pilot

Spec Pilot is a command-line tool for generating and managing OpenAPI specifications. The tool simplifies the process of creating OpenAPI specs by providing a user-friendly interface for inputting required information, and generates the final spec in YAML format.

## Features

- Project initialization with predefined directory structure
- OpenAPI Spec Wizard for user-friendly input of spec components
- Validation of OpenAPI specification YAML files

## Installation

To install Spec Pilot, clone this repository and run the `setup.py` script:

```sh
git clone https://github.com/jmfwolf/spec-pilot.git
cd spec-pilot
python setup.py install
```

from pypi:

```sh
pip install spec-pilot
```

## Usage

### Initializing a new project

To create a new project with a predefined directory structure, run the following command:

```sh
spec-pilot --init project_name
```

This will create a new directory with the given project name and subdirectories for schemas, resources, responses, and parameters.

### Running the OpenAPI Spec Wizard

To generate an OpenAPI spec using the Spec Wizard, run the following command:

```
spec-pilot --wizard
```

The Spec Wizard will prompt you for information about the API, such as endpoints, parameters, and responses. It will then generate an OpenAPI specification YAML file with the provided information.

### Validating an OpenAPI specification

To validate an OpenAPI specification YAML file, run the following command:

```
spec-pilot --validate path/to/openapi.yaml
```

The tool will check the validity of the YAML file and output any errors found during the validation process.

## Contributing

We welcome contributions to Spec Pilot! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make changes and commit them to your branch
4. Submit a pull request with a detailed description of your changes

Please follow the coding standards and guidelines established in the project, and make sure to include tests and documentation for any new features or changes.

We encourage users to provide feedback and contribute to the development of Spec-Pilot to make it more robust and feature-rich.

## License

Spec-Pilot is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
