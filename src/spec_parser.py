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
