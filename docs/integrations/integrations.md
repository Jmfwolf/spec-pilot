# Integrations

The goal of this project is to allow the average developer to create OpenAPI specifications that can be easily used by other tools and services. Thus integrations are some of the most important features.

## Overview

The pre-release design of spec-pilot aims to have the following integrations working out of the box upon release:

- [AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api.html)
- [Terraform Provider Creation](https://github.com/dikhan/terraform-provider-openapi/)
- [Openapi Generator](https://openapi-generator.tech/docs/generators/)
  - Client SDKs: Python, Java, Javascript
  - Proposed: MySQL, Documentation
- [Postman Collections](https://github.com/apideck-libraries/portman)
- [Redoc](https://github.com/Redocly/redoc)

## Integration Documentation

- [AWS](./aws.md)
- [Terraform](./terraform.md)
- [OpenAPI Generator](./oas_gen.md)