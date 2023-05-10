import re

class LanguageProcessor:
    def __init__(self):
        # Define regular expressions for each component type
        self.component_patterns = {
            "info": re.compile(r"(?P<name>[A-Za-z0-9_]+) (?P<version>\d+\.\d+\.\d+) (?P<title>.+?)"),
            "path": re.compile(r"(?P<method>GET|POST|PUT|DELETE|PATCH) (?P<path>\/[^\s]+) (?P<summary>[^\[\]]+)(\[(?P<params>[^\]]+)\])?"),
            "schema": re.compile(r"(?P<type>object|array|string|number|boolean) (?P<name>[A-Za-z0-9_]+)(\[(?P<props>[^\]]+)\])?"),
            "parameter": re.compile(r"(?P<name>[A-Za-z0-9_]+):(?P<type>query|path|header|cookie|body) (?P<schema>[A-Za-z0-9_]+)( (?P<required>required))?"),
            "response": re.compile(r"(?P<code>\d{3}) (?P<description>[^:\n]+)(: (?P<schema>[A-Za-z0-9_]+))?"),
        }

    def _parse_parameters(self, params_str):
        # Parse parameter strings and return a list of dictionaries
        parameters = []
        for match in self.component_patterns["parameter"].finditer(params_str):
            param_info = match.groupdict()
            param_info["in"] = param_info.pop("type")
            param_info["required"] = param_info.get("required") == "required"
            parameters.append(param_info)
        return parameters

    def _parse_responses(self, responses_str):
        # Parse response strings and return a dictionary of response codes and their corresponding information
        responses = {}
        for match in self.component_patterns["response"].finditer(responses_str):
            response_info = match.groupdict()
            code = response_info.pop("code")
            responses[code] = response_info
        return responses

    def process(self, description):
        # Parse the input description string and return a list of tuples containing the component type and its information
        parsed_components = []
        for component_type, pattern in self.component_patterns.items():
            for match in pattern.finditer(description):
                component_info = match.groupdict()
                if component_type == "path":
                    # If the component type is a path, parse the parameters and responses
                    if "params" in component_info and component_info["params"]:
                        component_info["parameters"] = self._parse_parameters(component_info.pop("params"))
                    if "responses" in component_info and component_info["responses"]:
                        component_info["responses"] = self._parse_responses(component_info.pop("responses"))
                elif component_type == "schema":
                    # If the component type is a schema, parse the properties and their required status
                    if "props" in component_info and component_info["props"]:
                        component_info["properties"] = self._parse_parameters(component_info.pop("props"))
                        component_info["required"] = [p["name"] for p in component_info["properties"] if p["required"]]
                parsed_components.append((component_type, component_info))
        return parsed_components