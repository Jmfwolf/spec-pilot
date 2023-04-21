import spacy
import json

def identify_action(doc):
    for token in doc:
        if token.dep_ == "ROOT":
            return token
    return None


def identify_target(doc, action_token):
    target = None
    target_schema_name = None
    for token in doc:
        if token.dep_ == "dobj" and token.head == action_token:
            if token.lemma_ == "field":
                # Look for the word "schema" after the action word
                for next_token in doc[token.i + 1:]:
                    if next_token.lemma_ == "schema":
                        target = next_token.lemma_
            else:
                target = token.lemma_
        if token.dep_ == "pobj" and token.head.head == action_token and token.head.lemma_ == "to":
            target_schema_name = token.text
    return target, target_schema_name



def identify_property(doc):
    for token in doc:
        if token.dep_ in ["compound", "nmod"]:
            return token.text.strip("'")
    return None


def modify_openapi_asset(openapi_spec, action, target, property_name, value=None, target_schema_name=None):
    if action == "add":
        if target == "schema":
            schema = openapi_spec["components"]["schemas"][target_schema_name]
            if "properties" not in schema:
                schema["properties"] = {}
            if property_name not in schema["properties"]:
                schema["properties"][property_name] = {"type": "string"}
            schema["properties"][property_name]["description"] = value
            if target_schema_name in openapi_spec["components"]["schemas"]:
                openapi_spec["components"]["schemas"][target_schema_name]["properties"][property_name] = value
            else:
                openapi_spec["components"]["schemas"][target_schema_name] = {
                    "type": "object",
                    "properties": {property_name: value},
                }
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

    action_token = identify_action(doc)
    target, target_schema_name = identify_target(doc, action_token)
    property_name = identify_property(doc)
    
    if 'description' in input_text:
        value = input_text.split('description')[1].strip("'\"")  # Extract the description value from the input text
    else:
        value = None

    if action_token and target and property_name:
        modified_openapi_spec = modify_openapi_asset(openapi_spec, action_token.lemma_, target, property_name, value, target_schema_name)
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
