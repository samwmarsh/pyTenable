from restfly.utils import dict_merge, url_validator

def policy_settings(item):
    '''
    Recursive function to attempt to pull out the various settings from scan
    policy settings in the editor format.
    '''
    resp = dict()
    if 'id' in item and ('default' in item
        or ('type' in item and item['type'] in [
            'file',
            'checkbox',
            'entry',
            'textarea',
            'medium-fixed-entry',
            'password'])):
        # if we find both an 'id' and a 'default' attribute, or if we find
        # a 'type' attribute matching one of the known attribute types, then
        # we will parse out the data and append it to the response dictionary
        if not 'default' in item:
            item['default'] = ""
        resp[item['id']] = item['default']

    for key in item.keys():
        # here we will attempt to recurse down both a list of sub-
        # documents and an explicitly defined sub-document within the
        # editor data-structure.
        if key == 'modes':
            continue
        if (isinstance(item[key], list)
            and len(item[key]) > 0
            and isinstance(item[key][0], dict)):
            for i in item[key]:
                resp = dict_merge(resp, policy_settings(i))
        if isinstance(item[key], dict):
            resp = dict_merge(resp, policy_settings(item[key]))

    # Return the key-value pair.
    return resp


def is_type(v, t):
    '''
    check if the value is of expected type

    Args:
        v: value
        t: type of value

    Returns:
        `bool`
    '''
    try:
        t(v)
        return True
    except:
        return False


def serialize_types(obj):
    '''
    parse JSON and convert values to expected types

    Args:
        obj (JSON obj): dictionary or list of dictionaries

    Returns:
        `dict` - updated dictionary
    '''
    true_values = [
        "t",
        "T",
        "true",
        "True",
        "TRUE",
        "on",
        "On",
        "ON",
        "y",
        "Y",
        "yes",
        "Yes",
        "YES",
    ]

    false_values = [
        "f",
        "F",
        "false",
        "False",
        "FALSE",
        "off",
        "Off",
        "OFF",
        "n",
        "N",
        "no",
        "No",
        "NO",
    ]
    if isinstance(obj, list):
        for l in obj:
            serialize_types(l)
            if isinstance(l, dict):
                serialize_types(l)
        return obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            serialize_types(v)
            if obj[k] == '':
                obj[k] = None
            elif isinstance(obj[k], str) and is_type(obj[k], int):
                obj[k] = int(obj[k])
            elif isinstance(obj[k], str) and is_type(obj[k], float):
                obj[k] = float(obj[k])
            elif isinstance(obj[k], str) and obj[k] in true_values:
                obj[k] = True
            elif isinstance(obj[k], str) and obj[k] in false_values:
                obj[k] = False
        return obj
