
import json
from bs4 import BeautifulSoup


def GetNestedPropsList2(soup: BeautifulSoup):

    parent_element = soup.find_all(["h2", "h3", "p"])

    for child in parent_element:
        print(child.get_text().strip())


# def ExtractedHtmlAsJson(soup):
#     extractedSoup = {
#         "page": soup.title.get_text(),
#         "jobs": GetNestedPropsList(soup, "card-content", ["title", "company", "location"]),
#         "images": ExtractAllImages(soup),
#         "links": ExtractAllLinks(soup, "Apply")
#     }

#     return json.dumps(extractedSoup)



def ElementBuilder(elementLists, all_attributes):
    """Creates initial objects for each attribute"""
    targetElements = []
    targets = {}
    n = 0
    for elements in elementLists:
        for target in elements:
            targets = {
                "Id": elements.index(target),
                all_attributes[n]: target.get_text().strip()
            }
            targetElements.append(targets)
        n += 1
    return targetElements


def ResultHandler(extractedResult: list):
    """Creates completed JSON object from target attributes"""
    jsonObj = {}
    for result in extractedResult:
        for key, val in result.items():
            # See this works if its hardcoded to a number...
            if(key == "Id" and val == 99):
                jsonObj.update(result)
    print(jsonObj)


def AttributeHandler(Attrs: list):
    """Extracts target attribute names"""
    all_attributes = []
    for dict in Attrs:
        all_attributes.append("".join(dict.values()))
    return all_attributes