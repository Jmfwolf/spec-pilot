import yaml
from language_processor import LanguageProcessor

class Generator:
    def __init__(self, description):
        self.description = description
        self.language_processor = LanguageProcessor()

    def _generate_openapi_component(self, component_type, component_info):
        component_spec = {}
        if component_type == "path":
            component_spec["summary"] = component_info["summary"]
            component_spec["operationId"] = component_info.get("operationId", "") # Add default value
            if "parameters" in component_info:
                component_spec["parameters"] = component_info["parameters"]
            if "responses" in component_info:
                component_spec["responses"] = component_info["responses"]
        elif component_type == "schema":
            component_spec["type"] = component_info["type"]
            if "properties" in component_info:
                component_spec["properties"] = component_info["properties"]
            if "required" in component_info:
                component_spec["required"] = component_info["required"]
        # Add support for other component types as needed
        return component_spec

    def generate_spec(self):
        parsed_components = self.language_processor.process(self.description)
        openapi_spec = {"openapi": "3.0.0", "info": {}, "paths": {}, "components": {"schemas": {}}}
        for component_type, component_info in parsed_components:
            if component_type == "info":
                openapi_spec["info"] = component_info
            elif component_type == "path":
                path = component_info["path"]
                method = component_info["method"]
                if path not in openapi_spec["paths"]:
                    openapi_spec["paths"][path] = {}
                openapi_spec["paths"][path][method] = self._generate_openapi_component(component_type, component_info)
            elif component_type == "schema":
                schema_name = component_info["name"]
                openapi_spec["components"]["schemas"][schema_name] = self._generate_openapi_component(component_type, component_info)
            # Add support for other component types as needed
        return yaml.dump(openapi_spec, sort_keys=False)
