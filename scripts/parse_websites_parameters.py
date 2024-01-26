import json


def parse_websites_parameters(website_parameters_file="config/websites_parameters.json"):
    with open(website_parameters_file) as websites_parameters_file:
        websites_parameters = json.load(websites_parameters_file)

    websites_parameters_dict = {}
    for key, website_parameters in websites_parameters.items():
        name = key
        # make sure it has the title_tag key or raise error
        for elem_tag in ["title_tag", "content_tag"]:
            if elem_tag not in website_parameters:
                raise ValueError(
                    f"'{elem_tag}' key is missing in {website_parameters}")
            elem_tag = website_parameters[elem_tag]
            tag = elem_tag["tag"]
            name = elem_tag["name"]


parse_websites_parameters()
