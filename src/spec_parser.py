import spacy
import json

def identify_action(doc):
    for token in doc:
        if token.dep_ == "ROOT":
            return token.lemma_
    return None

def identify_target(doc):
    for token in doc:
        if token.dep_ == "dobj":
            return token.lemma_
    return None

def identify_property(doc):
    for token in doc:
        if token.dep_ in ["compound", "nmod"]:
            return token.text.strip("'")
    return None


def modify_openapi_asset(openapi_spec, action, target, property_name, value=None):
    if action == "add":
        if target == "schema":
            if "components" not in openapi_spec:
                openapi_spec["components"] = {}
            if "schemas" not in openapi_spec["components"]:
                openapi_spec["components"]["schemas"] = {}  # Added colon
            if property_name not in openapi_spec["components"]["schemas"]:
                openapi_spec["components"]["schemas"][property_name] = {"type": "object", "properties": {}}  # Added colon
            openapi_spec["components"]["schemas"][property_name]["properties"][value["name"]] = value
        elif target == "parameter":
            openapi_spec["components"]["parameters"][property_name] = value
    elif action == "update":
        if target == "schema":
            openapi_spec["components"]["schemas"][property_name]["default"] = value
        elif target == "parameter":
            openapi_spec["components"]["parameters"][property_name]["default"] = value
    elif action == "remove":
        if target == "schema":
            openapi_spec["components"]["schemas"][property_name].pop("required", None)
        elif target == "parameter":
            openapi_spec["components"]["parameters"][property_name].pop("required", None)
    return openapi_spec


def process_natural_language_input(input_text, openapi_spec):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)

    action = identify_action(doc)
    target = identify_target(doc)
    property_name = identify_property(doc)
    value = {"name": property_name, "type": "string", "description": ""}  # Update this line to pass the property_name correctly

    print(f"action: {action}")  # Debugging
    print(f"target: {target}")  # Debugging
    print(f"property_name: {property_name}")  # Debugging

    if action and target and property_name:
        modified_openapi_spec = modify_openapi_asset(openapi_spec, action, target, property_name, value)
        return modified_openapi_spec
    else:
        return None

# Example OpenAPI specification
openapi_spec = {
    "components": {
        "schemas": {
            "User": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    }
                }
            }
        },
        "parameters": {
            "userId": {
                "in": "query",
                "name": "userId",
                "schema": {
                    "type": "integer"
                }
            }
        },
        "responses": {},
        "tags": []
    }
}

# Example input
input_text = "add a 'description' field to the schema User"
modified_openapi_spec = process_natural_language_input(input_text, openapi_spec)

print(json.dumps(modified_openapi_spec, indent=2))
import spacy

nlp = spacy.load("en_core_web_sm")


def process_natural_language_input(sentence):
    doc = nlp(sentence)

    # Extract relevant information from the sentence
    command, target, details = extract_command_target_details(doc)

    # Perform the appropriate action based on the extracted information
    perform_action(command, target, details)


def extract_command_target_details(doc):
    command = None
    target = None
    details = {}

    for token in doc:
        # Extract command
        if token.dep_ == "ROOT":
            command = token.lemma_

        # Extract target
        if token.dep_ in ["dobj", "attr"]:
            target = token.lemma_

        # Extract additional details (e.g., adjectives, compound nouns)
        if token.dep_ in ["amod", "compound"]:
            if token.head.lemma_ not in details:
                details[token.head.lemma_] = []
            details[token.head.lemma_].append(token.lemma_)

    return command, target, details


def perform_action(command, target, details):
    if command == "initialize":
        if target == "project":
            project_name = details.get("name", [None])[0]
            if project_name:
                generator.init_project(project_name)
            else:
                print("Please specify a project name.")
        else:
            print(f"Unsupported target for command '{command}': {target}")

    elif command == "add" or command == "update" or command == "remove":
        if target == "schema" or target == "parameter":
            component_name = details.get("name", [None])[0]
            property_name = details.get("property", [None])[0]
            value = details.get("value", [None])[0]

            if component_name and property_name:
                if command == "add":
                    generator.add_component_property(target, component_name, property_name, value)
                elif command == "update":
                    generator.update_component_property(target, component_name, property_name, value)
                elif command == "remove":
                    generator.remove_component_property(target, component_name, property_name)
            else:
                print("Please specify both the component name and property name.")
        else:
            print(f"Unsupported target for command '{command}': {target}")

    else:
        print(f"Unsupported command: {command}")
