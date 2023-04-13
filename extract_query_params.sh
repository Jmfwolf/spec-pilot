#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <schema_file>"
    exit 1
fi

SCHEMA_FILE="$1"
QUERY_PARAMETERS_FILE="query_parameters.yml"

echo "[]" > "$QUERY_PARAMETERS_FILE"

yq -r '.properties | keys[]' "$SCHEMA_FILE" | while read -r PROP; do
    PROP_TYPE=$(yq -r ".properties.${PROP}.type" "$SCHEMA_FILE")
    PROP_FORMAT=$(yq -r ".properties.${PROP}.format" "$SCHEMA_FILE")

    if [[ "$PROP_TYPE" != "array" && "$PROP_TYPE" != "object" ]]; then
        QUERY_PARAM="
            name: $PROP
            in: query
            description: Filter by $PROP
            required: false
            schema:
                type: $PROP_TYPE
        "

        if [[ "$PROP_FORMAT" != "null" ]]; then
            QUERY_PARAM=$(echo "$QUERY_PARAM" | jq --arg format "$PROP_FORMAT" '.schema.format = $format')
        fi

        QUERY_PARAMETERS=$(yq -s '.[0] + [.[-1]]' "$QUERY_PARAMETERS_FILE" <(echo "$QUERY_PARAM"))
        echo "$QUERY_PARAMETERS" > "$QUERY_PARAMETERS_FILE"
    fi
done
