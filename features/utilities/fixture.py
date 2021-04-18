import re


def to_snake_case(value):
    value = value.replace(' ', '_').replace('&', 'and').lower()
    return re.sub(r'\W+', '', value)


def get_element_key(element_name, element_type=None):
    if element_type is None:
        return f'{to_snake_case(element_name)}'
    else:
        return f'{to_snake_case(element_name)}_{to_snake_case(element_type)}'


def search_and_get_multiple_value_from_content(pattern, content):
    param = re.finditer(pattern, content)
    items = []
    if param:
        for p in param:
            items.append({
                'full_value': p.group(0),
                'inner_value': p.group(1)
            })

    return items
