#!/bin/bash

function check_params {
    if [ "$#" -eq 0 ]; then
        echo -e "Error: No parameters passed\n"
        exit 1
    fi
}

function insert_into_index {
    # yq insert inplace at the root level the environment variable 
    # NEW_ENTRY into the index file of the Directory type: parameter, resources, schemas, or responses
    check_params "$@"
    if [ "$?" -eq 1 ]; then
        echo -e "New asset requires a name in order to be inserted into the appropriate index.\n"
        exit 1
    else
        export NEW_ENTRY="$1"
        export NEW_FILE="$NEW_ENTRY.yml"
        yq -i '.[env(NEW_ENTRY)].$ref = env(NEW_FILE)' $DIR_NAME/_index.yml
        echo "$NEW_ENTRY inserted to $DIR_NAME/_index.yml"
    fi
}

function create_asset {
    # touch new yml file in the appropriate directory
    check_params "$@"
    if [ "$?" -eq 1 ]; then
        echo -e "New asset requires a name in order to be created.\n"
        exit 1
    else
        export NEW_ASSET="$1"
        touch $DIR_NAME/"$NEW_ASSET.yml"
        echo "$NEW_ASSET successfully created"
    fi
}

function remove_from_index {
    # yq remove inplace the entry in _index.yml that matches the value passed in
    check_params "$@"
    if [ "$?" -eq 1 ]; then
        echo -e "Please specify the entry to remove.\n"
    else
        export RM_TARGET="$1"
        yq -i 'del( .[env(RM_TARGET)] )' $DIR_NAME/_index.yml
    fi
}

function remove_asset {
    # remove the rm_target from the directory and the indexing
    check_params "$@"
    if [ "$?" -eq 1 ]; then
        echo -e "Please specify the entry to remove.\n"
    else
        export RM_TARGET="$1"
        rm $DIR_NAME/"$RM_TARGET.yml"
        remove_from_index "$RM_TARGET"
    fi
}

function init_project {
    # create the initial file structure and indexes
    check_params "$@"
    if [ "$?" -eq 1 ]; then
        echo -e "Please specify the project name.\n"
    else
        mkdir -p "$1"/schemas "$1"/resources "$1"/parameters/query "$1"/parameters/path "$1"/responses
        cd $1
        touch schemas/_index.yml resources/_index.yml parameters/_index.yml responses/_index.yml
    fi
}

