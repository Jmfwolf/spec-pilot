function build_from_template {
   FILE="$1"
   TEMPLATE="$2"
   DIR_NAME="$3"
   ASSET="$4"
   yq -j . $FILE | mustache $TEMPLATE - > $DIR_NAME/$ASSET
}

function param_builder {
  PARAM_TYPE="$1"
  PARAM_NAME="$2"
  FILENAME="src/parameters/${PARAM_TYPE}/${PARAM_NAME}.yml"
  mkdir -p "$(dirname "${FILENAME}")"
  cat > "${FILENAME}" <<EOF
name: ${PARAM_NAME}
in: ${PARAM_TYPE}
required: true
description: Add your description here
schema:
  type: string
EOF
}

function path_builder {
   RESOURCE="$1"
   FILENAME="$RESOURCE.yml"
   build_from_template "$RESOURCE" "templates/path.mustache" "resources" "$FILENAME"
}