# Terraform

Current planned support for Terraform uses [terraform provider openapi](https://github.com/dikhan/terraform-provider-openapi/)

## Limitations

Limitations and requirements of this tool are explained in the [how to](https://github.com/dikhan/terraform-provider-openapi/blob/master/docs/how_to.md)

- Limited Swagger 2.0: The terraform provider openapi currently only supports Swagger 2.0 specifications. While this can be a limitation for those using newer versions of the OpenAPI specification, it's still a powerful tool for generating Terraform code from Swagger 2.0 specs.

- Manual configuration required: In order to use the terraform provider openapi, some manual configuration is required. This includes setting up a Terraform provider and defining the necessary resources in the provider configuration.

- Limited support for Terraform resources: While the terraform provider openapi supports many common Terraform resources, there may be some resources that are not fully supported or require additional configuration.

## Roadmap

Limitations of this tool provide an interesting challenge as it only currently supports Swagger 2.0. Converting a 3.x spec to 2.0 is not enough to have the tool work out of the box. But there is no point in having an enterprise grade API gateway if Enterprise grade tooling can't be used.