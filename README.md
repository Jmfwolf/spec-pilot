# OAS-maker

This software simplifies the creation and management of customized OpenAPI specifications for specific tools and platforms. It provides a set of utilities for creating, updating, and removing assets such as schemas, resources, parameters, and responses. The software also helps you maintain a clean and organized file structure and build assets from templates.

## Project Goal

The primary objective of this project is to simplify the creation and management of customized OpenAPI specifications for specific tools and platforms. In various scenarios, a single OpenAPI specification may not be suitable for multiple tools due to differences in requirements, constraints, or features.

For instance, when using [Terrraform-Provider-OpenAPI](https://github.com/dikhan/terraform-provider-openapi) to manage infrastructure alongside [API Gateway on AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html) for API deployment, the same OpenAPI specification might not be compatible with both tools. This could be due to differences in supported fields, required extensions, or other tool-specific expectations.

This software aims to address such issues by providing a foundation for creating a "proto-build" of your service. The proto-build serves as a starting point for generating tool-specific OpenAPI specifications tailored to the requirements of each target platform. This approach enables seamless integration with various tools, ensuring compatibility and promoting best practices for API development.

By using this software, engineers can maintain a single source of truth for their API specifications while generating and managing customized versions for different tools and environments, streamlining development, and reducing the risk of inconsistencies across platforms.

## Prerequisites

- [yq](https://github.com/mikefarah/yq) command-line processor for YAML (version 4.x)
- [mustache](http://mustache.github.io/) command-line tool for rendering mustache templates

## Usage

To use this script, first clone the repository, and navigate to the directory containing the script. Make sure the script is executable by running:

```sh

chmod +x utilities.sh
```

### Initializing a Project

To initialize a new project, run the following command:

```sh

./utilities.sh init_project <project_name>
```

This will create the initial file structure and indexes for your project.

### Creating an Asset

To create a new asset, run the following command:

```sh

./utilities.sh create_asset <asset_name>
```

This will create a new YAML file in the appropriate directory.

### Inserting an Asset into the Index

To insert an asset into the index, run the following command:

```sh

./utilities.sh insert_into_index <asset_name>
```

This will insert the specified asset into the appropriate index file.

### Removing an Asset from the Index

To remove an asset from the index, run the following command:

```sh

./utilities.sh remove_from_index <asset_name>
```

This will remove the specified asset from the index file.

### Removing an Asset

To remove an asset, run the following command:

```sh

./utilities.sh remove_asset <asset_name>
```

This will delete the specified asset and remove it from the index.

### Building Assets from Templates

To build assets from templates, run the following command:

```sh

./utilities.sh build_from_template <input_file> <template_file> <output_directory> <output_asset_name>
```

This will use the specified input file and template file to create a new asset in the specified output directory.

### Building Paths from Resources

To build paths from resources, run the following command:

```sh
./utilities.sh path_builder <resource_name>
```

This will generate a path file from the specified resource YAML file, using the provided templates/path.mustache template, and save it in the resources directory with a .yml extension.

## License

This project is licensed under the [GNU General Public License v3.0.](https://www.gnu.org/licenses/gpl-3.0.html) See the LICENSE file for details.

## Acknowledgments

Special thanks to the creators of the yq and mustache command-line tools, which are essential components of this software.
