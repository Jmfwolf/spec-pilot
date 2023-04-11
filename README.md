# OAS-maker

This software helps you manage your OpenAPI specification files by providing a set of utilities for creating, updating, and removing assets such as schemas, resources, parameters, and responses. It also helps you maintain a clean and organized file structure, and build assets from templates.

## Prerequisites

Bash shell
yq command-line processor for YAML (version 4.x)
mustache command-line tool for rendering mustache templates

## Usage

To use this script, first clone the repository, and navigate to the directory containing the script. Make sure the script is executable by running:

```bash

chmod +x utilities.sh
```

### Initializing a Project

To initialize a new project, run the following command:

```bash

./utilities.sh init_project <project_name>
```

This will create the initial file structure and indexes for your project.

### Creating an Asset

To create a new asset, run the following command:

```bash

./utilities.sh create_asset <asset_name>
```

This will create a new YAML file in the appropriate directory.

### Inserting an Asset into the Index

To insert an asset into the index, run the following command:

```bash

./utilities.sh insert_into_index <asset_name>
```

This will update the index file of the appropriate directory with a reference to the new asset.

### Removing an Asset

To remove an asset, run the following command:

```bash

./utilities.sh remove_asset <asset_name>
```

This will remove the specified asset and update the index file accordingly.

### Removing an Entry from the Index

To remove an entry from the index without deleting the associated asset, run the following command:

```bash

./utilities.sh remove_from_index <entry_name>
```

### Building an Asset from a Template

To build an asset from a template, run the following command:

```bash

./utilities.sh build_from_template <input_file> <template_file> <directory_name> <asset_name>
```

This will use the provided input data and mustache template to create a new asset in the specified directory.

### Building a Path from a Resource

To build a path from a resource YAML file, run the following command:

```bash

./utilities.sh path_builder <resource_name>
```

This will create a new path YAML file based on the resource data and the templates/path.mustache template.

## Functions

The script provides the following functions:

- check_params: Checks if any parameters were passed to a function.
- insert_into_index: Inserts an asset into the index.
- create_asset: Creates a new asset file.
- remove_from_index: Removes an entry from the index.
- remove_asset: Removes an asset and its entry from the index.
- init_project: Initializes a new project with the required file structure and indexes.
- build_from_template: Builds an asset from a user input file and a mustache template.
- path_builder: Creates a path asset from a resource YAML file.

## License

This project is open-source and available under the GNU General Public License v3.0.
