

def strip_html_string(string):
    pass


def check_json_key(json, key, return_elem=True):
    if key not in json:
        raise ValueError(
            f"'{elem_tag}' key is missing in {website_parameters}")
    if return_elem:
        return json[key]
    else:
        return False
