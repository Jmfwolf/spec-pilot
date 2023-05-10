class PromptBuilder:
    def __init__(self):
        self.spec_description = ""

    def add_info(self):
        name = input("Enter the name of your API: ")
        version = input("Enter the version of your API (e.g. 1.0.0): ")
        title = input("Enter a brief title for your API: ")

        self.spec_description += f"{name} {version} {title}\n"

    def add_path(self):
        method = input("Enter the HTTP method (GET, POST, PUT, DELETE, PATCH): ")
        path = input("Enter the path (e.g. /items/{itemId}): ")
        summary = input("Enter a brief summary of this endpoint: ")

        params = []
        while True:
            add_param = input("Add a parameter? (y/n): ")
            if add_param.lower() == "y":
                name = input("Enter the parameter name: ")
                param_type = input("Enter the parameter type (query, path, header, cookie, body): ")
                schema = input("Enter the schema for the parameter (e.g. string, number, customSchema): ")
                required = input("Is the parameter required? (y/n): ")

                param_str = f"{name}:{param_type} {schema}"
                if required.lower() == "y":
                    param_str += " required"
                params.append(param_str)
            else:
                break

        params_str = f"[{', '.join(params)}]" if params else ""
        self.spec_description += f"{method} {path} {summary}{params_str}\n"

    def add_schema(self):
        schema_type = input("Enter the schema type (object, array, string, number, boolean): ")
        name = input("Enter the schema name: ")

        properties = []
        if schema_type == "object":
            while True:
                add_prop = input("Add a property? (y/n): ")
                if add_prop.lower() == "y":
                    prop_name = input("Enter the property name: ")
                    prop_schema = input("Enter the schema for the property (e.g. string, number, customSchema): ")
                    prop_required = input("Is the property required? (y/n): ")

                    prop_str = f"{prop_name}:{prop_schema}"
                    if prop_required.lower() == "y":
                        prop_str += " required"
                    properties.append(prop_str)
                else:
                    break

        properties_str = f"[{', '.join(properties)}]" if properties else ""
        self.spec_description += f"{schema_type} {name}{properties_str}\n"

    def get_spec_description(self):
        return self.spec_description

    def prompt(self):
        print("Welcome to the OpenAPI Spec Prompt Builder!")
        self.add_info()

        while True:
            add_component = input("Add a component? (path, schema, done): ")
            if add_component.lower() == "path":
                self.add_path()
            elif add_component.lower() == "schema":
                self.add_schema()
            elif add_component.lower() == "done":
                break
            else:
                print("Invalid input. Please enter 'path', 'schema', or 'done'.")

        return self.get_spec_description()