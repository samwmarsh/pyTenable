'''
schema utilities
'''

def convert_blank_string_to_none(obj, match='', replace=None):
    '''
    it converts black string value to None in JSON

    Args:
        obj (dict): dictionary of items
        match (Any, optional): existing value which you want to replace
        replace (Any, optional): new value you want to place in match string

    Returns:
        `dict` - updated dictionary
    '''
    if isinstance(obj, list):
        for l in obj:
            convert_blank_string_to_none(l, match, replace)
            if isinstance(l, dict):
                convert_blank_string_to_none(l, match, replace)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            convert_blank_string_to_none(v, match, replace)
            if obj[k] == '':
                obj[k] = None
        return obj