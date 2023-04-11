#!/bin/bash

function check_params {
    local expected_params="$1"
    shift
    if [ "$#" -ne "$expected_params" ]; then
        echo -e "Error: Incorrect number of parameters. Expected $expected_params, but received $#\n"
        exit 1
    fi
}

function insert_into_index {
    # yq insert inplace at the root level the environment variable 
    # NEW_ENTRY into the index file of the Directory type: parameter, resources, schemas, or responses
    check_params 1 "$@"
    export NEW_ENTRY="$1"
    export NEW_FILE="$NEW_ENTRY.yml"
    yq -i '.[env(NEW_ENTRY)].$ref = env(NEW_FILE)' $DIR_NAME/_index.yml
    echo "$NEW_ENTRY inserted to $DIR_NAME/_index.yml"
}

function create_asset {
    # touch new yml file in the appropriate directory
    check_params 1 "$@"
    export NEW_ASSET="$1"
    touch $DIR_NAME/"$NEW_ASSET.yml"
    echo "$NEW_ASSET successfully created"
}

function remove_from_index {
    # yq remove inplace the entry in _index.yml that matches the value passed in
    check_params 1 "$@"
    export RM_TARGET="$1"
    yq -i 'del( .[env(RM_TARGET)] )' $DIR_NAME/_index.yml
}

function remove_asset {
    # remove the rm_target from the directory and the indexing
    check_params 1 "$@"
    export RM_TARGET="$1"
    rm $DIR_NAME/"$RM_TARGET.yml"
    remove_from_index "$RM_TARGET"
}

function init_project {
    # create the initial file structure and indexes
    check_params 1 "$@"
    mkdir -p "$1"/schemas "$1"/resources "$1"/parameters/query "$1"/parameters/path "$1"/responses
    cd $1
    touch schemas/_index.yml resources/_index.yml parameters/_index.yml responses/_index.yml
}
# Need testing!
function build_from_template {
    # use user input data as file and appropriate mustache template
    # to create new asset 
    check_params 4 "$@"
    FILE="$1"
    TEMPLATE="$2"
    DIR_NAME="$3"
    ASSET="$4"
    yq -j . $FILE | mustache $TEMPLATE - > $DIR_NAME/$ASSET
}
# Need testing!
function path_builder {
    # Create Path from resource yaml
    check_params 1 "$@"
    RESOURCE="$1"
    FILENAME="$RESOURCE.yml"
    build_from_template "$RESOURCE" "templates/path.mustache" "resources" "$FILENAME"
}
