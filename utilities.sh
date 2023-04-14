#!/bin/bash

function check_params {
    local EXPECTED_PARAMS="$1"
    shift
    if [ "$#" -ne "$EXPECTED_PARAMS" ]; then
        echo -e "Error: Incorrect number of parameters. Expected $EXPECTED_PARAMS, but received $#\n"
        exit 1
    fi
}

function insert_into_index {
    # yq insert inplace at the root level the environment variable 
    # NEW_ENTRY into the index file of the Directory type: parameter, resources, schemas, or responses
    check_params 2 "$@"
    export NEW_ENTRY="$1"
    local DIR_NAME="$2"
    export NEW_FILE="$NEW_ENTRY.yml"
    yq -i '.[env(NEW_ENTRY)].$ref = env(NEW_FILE)' $DIR_NAME/_index.yml
    echo "$NEW_ENTRY inserted to $DIR_NAME/_index.yml"
}

function create_asset {
    # touch new yml file in the appropriate directory
    check_params 2 "$@"
    export NEW_ASSET="$1"
    local DIR_NAME="$2"
    touch $DIR_NAME/"$NEW_ASSET.yml"
    echo "$NEW_ASSET successfully created"
}

function remove_from_index {
    # yq remove inplace the entry in _index.yml that matches the value passed in
    check_params 2 "$@"
    export RM_TARGET="$1"
    local DIR_NAME="$2"
    yq -i 'del( .[env(RM_TARGET)] )' $DIR_NAME/_index.yml
}

function remove_asset {
    # remove the rm_target from the directory and the indexing
    check_params  "$@"
    export RM_TARGET="$1"
    local DIR_NAME="$2"
    rm $DIR_NAME/"$RM_TARGET.yml"
    remove_from_index "$RM_TARGET"
}

function init_project {
    # create the initial file structure and indexes
    check_params 1 "$@"
    mkdir -p "$1"/schemas "$1"/resources "$1"/parameters/query "$1"/parameters/path "$1"/responses
    cd "$1" || exit
    touch schemas/_index.yml resources/_index.yml parameters/_index.yml responses/_index.yml
}

function build_from_template {
    # Use user input data as file and appropriate mustache template
    # to create a new asset 
    check_params 4 "$@"
    FILE="$1"
    TEMPLATE="$2"
    DIR_NAME="$3"
    FILENAME="$4"
    yq -j . $FILE | mustache - "$TEMPLATE" > $DIR_NAME/$FILENAME
}

function resource_builder {
    # Create Path from resource yaml
    check_params 1 "$@"
    RESOURCE="$1"
    FILENAME="$RESOURCE.yml"
    build_from_template "$RESOURCE" "templates/path.mustache" "resources" "$FILENAME"
}

function response_builder {
    # Create Response from response yaml
    check_params 1 "$@"
    RESPONSE="$1"
    FILENAME="$RESPONSE.yml"
    build_from_template "$RESPONSE" "templates/response.mustache" "responses" "$FILENAME"
}

function parameter_builder {
    # Create Parameter from parameter yaml
    check_params 1 "$@"
    PARAMETER="$1"
    FILENAME="$PARAMETER.yml"
    build_from_template "$PARAMETER" "templates/parameter.mustache" "parameters" "$FILENAME"
}

function schema_builder {
    # Create Schema from schema yaml
    check_params 1 "$@"
    SCHEMA="$1"
    FILENAME="$SCHEMA.yml"
    build_from_template "$SCHEMA" "templates/schema.mustache" "schemas" "$FILENAME"
}

function insert_resource_paths {
    # Insert path into resource index
    check_params 1 "$@"
    RESOURCE="$1"
    export FILENAME="$RESOURCE.yml"
    yq -i '.paths.$ref = env(FILENAME)' resources/_index.yml
}

function insert_parameter {
    # Insert parameter into parameter index
    check_params 2 "$@"
    export PARAM_TYPE="$1"
    PARAM="$2"
    export FILENAME="$PARAM.yml"
    yq -i '.[env(PARAM_TYPE)].$ref = env(FILENAME)' parameters/_index.yml
}

function insert_response {
    # Insert response into response index
    check_params 2 "$@"
    export STATUS_CODE="$1"
    RESPONSE="$2"
    export FILENAME="$RESPONSE.yml"
    yq -i '.[env(STATUS_CODE)].$ref = env(FILENAME)' responses/_index.yml
}

function insert_schema {
    # Insert schema into schema index
    check_params 1 "$@"
    export SCHEMA="$1"
    export FILENAME="$SCHEMA.yml"
    yq -i '.[env(SCHEMA)].$ref = env(FILENAME)' schemas/_index.yml
    
}