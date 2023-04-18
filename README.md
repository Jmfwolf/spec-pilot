# OAS Maker

OAS Maker is a Python script to generate OpenAPI Specification (OAS) files using the mustache templating engine. This script allows you to easily create OAS files for your API by providing a simple way to define the various components such as schemas, paths, parameters, responses, etc. This project supports both OpenAPI v2.0 (Swagger) and v3.0 specifications.

## Prerequisites

Before using this script, make sure you have the following installed:

    Python 3.6 or higher
    pystache (pip install pystache)

## How to use

1. Clone or download this repository.
2. Define the context for each component (e.g., schema, path object, parameter, etc.) following the examples provided in the demo() function.
3. Call the appropriate function for each component, passing the context and the desired output file location.
4. Run the script to generate the OAS files in the specified output directories.

## Functions

The main functions provided by the script are:

- `init_project(project_name)`: Initializes a new project with the required directory structure.
- `generate_oas(context, output_file, version)`: Generates an OAS file.
- `generate_schema(context, output_file, version)`: Generates a schema definition file.
- `generate_path_object(context, output_file, version)`: Generates a path object definition file.
- `generate_parameter(context, output_file, version)`: Generates a parameter definition file.
- `generate_info(context, output_file, version)`: Generates the main info block for the OAS file.
- `generate_header(context, output_file, version)`: Generates a header definition file.
- `generate_media_type(context, output_file, version)`: Generates a media type definition file.
- `generate_response(context, output_file, version)`: Generates a response definition file.
- `generate_parameter_object(context, output_file, version)`: Generates a parameter object definition file.
- `generate_tag(context, output_file, version)`: Generates a tag definition file.
- `generate_server(context, output_file, version)`: Generates a server definition file.
- `generate_contact(context, output_file, version)`: Generates a contact definition file.
- `generate_license(context, output_file, version)`: Generates a license definition file.

## Example usage

The `demo()` function in the script demonstrates how to use the functions to generate a simple OAS for a Library API. To run the demo, simply execute the script:

`python template_generator.py`

This will create a new project named "demo" with the necessary directory structure and generate the OAS files for the provided context.

## Customization

You can customize the templates for each component by editing the mustache template files located in the `templates/v2.0` and `templates/v3.0` directories. The script will automatically render the templates with the provided context when generating the OAS files.

## Merging Generated Files

Once you have generated the various components of your OAS files (e.g., schemas, paths, parameters, etc.), you will need to merge them into a single OAS file. This can be done manually or by using a tool like Swagger-CLI or OpenAPI CLI.

For example, using Swagger-CLI, you can merge the generated files with the following command:

    ```sh
    swagger-cli bundle -r -o output.yaml info.yaml
    ```

This command will recursively merge all the generated files referenced in info.yaml and output the final OAS file as output.yaml.
Validation

After merging the generated files, it's a good idea to validate the resulting OAS file to ensure that it conforms to the OpenAPI Specification. You can use an online validator like Swagger Editor or Swagger Validator or a command-line tool like OpenAPI CLI or Swagger CLI.

For example, using OpenAPI CLI, you can validate the merged OAS file with the following command:

    ```sh
    openapi-cli validate output.yaml
    ```

If there are any errors or warnings, address them in your templates or context definitions and regenerate the OAS files.

## Documentation

Once you have a valid OAS file, you can use it to generate documentation for your API. There are various tools available for this purpose, such as Swagger UI, ReDoc, or Spectacle.

For example, to generate documentation using Swagger UI, follow these steps:

    Download or clone the Swagger UI repository.
    Replace the example/swagger.json file in the Swagger UI repository with your generated and merged OAS file.
    Open the dist/index.html file in a web browser to view the interactive documentation.

## Contributing

We welcome contributions to improve and extend OAS Maker. To contribute, please fork the repository, make your changes, and submit a pull request.

## License

OAS Maker is released under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for more information.
