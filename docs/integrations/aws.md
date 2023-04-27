# AWS

Currently the project is focusing on AWS API Gateway integration

## Limitations
In addition to the limitations mentioned in the [API-gateway-known-issues](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-known-issues.html#api-gateway-known-issues-rest-apis), there are some other limitations to be aware of when using AWS API Gateway with OpenAPI specifications. These include:

- Limited support for API Gateway Extensions: While AWS API Gateway does support some OpenAPI extensions, there are some that are not currently supported. Be sure to check the AWS API Gateway documentation to see which extensions are supported.

- Limited support for validation rules: AWS API Gateway has a limited set of validation rules that it can enforce when using OpenAPI specifications. This means that some OpenAPI specification features may not be enforced by AWS API Gateway.

- Limited support for customization: AWS API Gateway provides some customization options for your API, but these are limited compared to other API management tools. If you require more advanced customization options, you may need to consider using a different API management tool or building your own API management layer.

## Roadmap

In addition to the basic validator for AWS-specific violations, there are several other features that we plan to add to the AWS API Gateway integration in the future. These include:

- Support for additional OpenAPI extensions: We plan to add support for more OpenAPI extensions, allowing users to take advantage of more advanced OpenAPI features when using AWS API Gateway.

- Better error handling: We plan to improve the error handling and error messages provided by the AWS API Gateway integration, making it easier for users to troubleshoot issues with their API.

- Support for other AWS services: We plan to add support for other AWS services, such as Lambda functions, that can be used in conjunction with AWS API Gateway to build more advanced APIs.