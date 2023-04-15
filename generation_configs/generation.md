# Generation Config Files

The generation_configs directory is used to store multiple YAML files that define additional properties for different client SDK generators in the OpenAPI Generator CLI. These files can be used by the main program to automate the generation process and ensure consistency across different SDKs.

Each YAML file should define additional properties for a single generator, using the same format as the config.yml file described earlier. For example, a YAML file for the Java generator might look like this:

```yaml

# Configuration for Java generator
groupId: "com.example"
artifactId: "my-java-sdk"
artifactDescription: "My Java SDK"
artifactVersion: "1.0.0"
developerName: "John Doe"
developerEmail: "johndoe@example.com"
developerOrganization: "Example Inc."
developerOrganizationUrl: "https://www.example.com"
apiPackage: "com.example.api"
invokerPackage: "com.example.sdk"
modelPackage: "com.example.model"
```

To use the YAML files in the generation_configs directory, the main program can read each file and pass its contents to the OpenAPI Generator CLI using the --additional-properties-file option. For example, a shell script that generates client SDKs for multiple generators might look like this:

```bash

#!/bin/bash

# Loop through YAML files in generation_configs directory
for file in ./generation_configs/*.yaml; do
  # Extract generator name from file name
  generator=$(basename "$file" .yaml)

  # Generate client SDK for current generator
  openapi-generator-cli generate -g "$generator" -i openapi.yaml -o "sdk_$generator" --config config.yml --additional-properties-file "$file"
done
```

This shell script loops through all the YAML files in the generation_configs directory and generates client SDKs for each generator, using the --additional-properties-file option to pass the contents of the corresponding YAML file to the OpenAPI Generator CLI.
