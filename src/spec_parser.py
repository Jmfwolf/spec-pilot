import re

def parse_filters(object_schema):
    filterable_fields = ['name', 'id', 'status', 'category', 'tags', 'location', 'price', 'quantity', 'author', 'created_at', 'updated_at', 'start_date', 'end_date', 'duration', 'rating', 'language', 'size', 'format', 'type', 'genre', 'artist', 'album', 'year', 'publisher', 'author_name', 'author_email', 'author_role', 'username', 'email', 'is_active', 'is_admin', 'is_verified', 'is_public', 'is_featured', 'is_draft', 'is_published', 'has_image', 'has_video', 'has_audio', 'has_attachment', 'keyword']
    
    filters = []
    for field_name, field in object_schema['properties'].items():
        if 'properties' in field:
            # Recursive call for sub-resources
            filters += parse_filters(field)
        elif field_name in filterable_fields:
            # Find matches for filterable fields using regex
            pattern = re.compile(f'({field_name})(_[a-zA-Z0-9_]+)?(_(gte|gt|lte|lt))?')
            matches = pattern.findall(field_name)
            for match in matches:
                param_name = match[0] + (match[1] if match[1] else '') + (match[2] if match[2] else '')
                param_type = 'integer' if field['type'] == 'integer' else 'string'
                filters.append({
                    'parameterName': param_name,
                    'name': field_name,
                    'in': 'query',
                    'description': field.get('description', ''),
                    'required': False,
                    'schema': {
                        'type': param_type,
                        'example': field.get('example', None)
                    }
                })
    
    return filters
