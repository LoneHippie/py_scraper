import requests
from bs4 import BeautifulSoup


##### Intial parse #####

def GetMeTheSoup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


##### Image, link extractor actions #####

def ExtractAllImages(soup: BeautifulSoup):
    images = soup.find_all('img')

    if(len(images)) == 0:
        return None

    image_collection = []

    for image in images:
        image_collection.append({
            "alt": image.get('alt'),
            "src": image.get('src')
        })
    return image_collection

def ExtractAllLinks(soup: BeautifulSoup, linkText):
    links = soup.find_all('a', text=f"{linkText}")

    if(len(links) == 0):
        return None

    link_collection = []

    for link in links:
        link_collection.append({
            "href": link.get('href'),
            "alt": link.get('alt')
        })
    return link_collection


##### Argument parsers #####

def GetArgumentValue(Attribute) -> str: # Get dict value from attribute argument as string
    return list(Attribute.values())[0]

def GetArgumentKey(Attribute) -> str: # Get key name from attribute argument as string
    return list(Attribute.keys())[0]


##### Element extractors #####
### Attribute = {"<class/id/tag>": "<target value>"} ~ dictionary argument

def GetElementBySelector(soup: BeautifulSoup, Attribute) -> str:
    argument_type = GetArgumentKey(Attribute)
    if (argument_type == "tag"):
        return soup.find(GetArgumentValue(Attribute)).text.strip()
    else:
        return soup.find(attrs=Attribute).text.strip()

def GetElementListBySelector(soup: BeautifulSoup, Attribute) -> list:
    argument_type = GetArgumentKey(Attribute)
    if (argument_type == "tag"):
        return soup.find_all(GetArgumentValue(Attribute))
    else:
        return soup.find_all(attrs=Attribute)


##### ACTIONS #####

# Loop through all isntances of a target and build object from list of child targets
# ParentTarget = Attribute, childrenTargets = Array<Attribute>
def GetNestedPropsList(soup: BeautifulSoup, parentTarget, childrenTargets) -> list:

    el_collection = GetElementListBySelector(soup, parentTarget)
    data_collection = []

    for element in el_collection:
        el = {}

        for childAttr in childrenTargets:
            el[GetArgumentValue(childAttr)] = GetElementBySelector(element, childAttr)

        data_collection.append(el)

    return data_collection

# Get list of strings from all instances of target
def GetListByAttribute(soup: BeautifulSoup, target) -> list:

    el_collection = GetElementListBySelector(soup, target)
    data_collection = []

    for element in el_collection:
        data_collection.append(element.text.strip())
    
    return data_collection