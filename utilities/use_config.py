from .actions import GetNestedPropsList, ExtractAllLinks, GetMeTheSoup, GetListByAttribute


def UseConfig(config):
    soup = GetMeTheSoup(config["url"])
    response = {}

    # Loop through config array from req and use util functions with args and soup to generate fields
    for target in config["configs"]:
        if target["method"] == "ex-nested-props":
            response[target["name"]] = GetNestedPropsList(soup, *target["arguments"])
        elif target["method"] == "ex-links":
            response[target["name"]] = ExtractAllLinks(soup, *target["arguments"])
        elif target["method"] == "ex-elements-by-attr":
            response[target["name"]] = GetListByAttribute(soup, target["arguments"])

    return response