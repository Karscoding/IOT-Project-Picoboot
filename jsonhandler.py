import json
import os 

#Returns Value of Keyword Given
def Reader(kword):
    """
    Returns the value that is at given Keyword in data.json.
    kword = String
    """
    
    path = PathChecker()
    
    with open(path, "r") as JsonFile:
        data = json.load(JsonFile)
        
    return data[kword]

#Replaces Value of Keyword
def Writer(kword, value):
    """
    Opens the data.json File and replaces the Value at given kword with value.
    This keyword doesn't have to exist in the json file.
    It will create it if it doesn't.
    kword = String
    value = Anything.
    """
    
    path = PathChecker()
    
    with open(path, "r") as JsonFile:
        data = json.load(JsonFile)
        JsonFile.close()
    
    data[kword] = value
    
    with open(path, "w") as JsonFile:
        json.dump(data,JsonFile,indent=2)
        JsonFile.close()
        
    return data

#Checks Path (Complicated)
def PathChecker():
    """
    This Function checks the path from where this script is being ran from.
    When you import this script from the dashboard.
    The script will be inside the /dashboard/ folder.
    So it cannot find data.json.
    Because of this I have to give it a ../data.json if that's the case.
    Not doing this would require me to copy past this same code and make it in the dashboard folder.
    So this is fine.
    """
    
    curpath = os.getcwd()
    if "dashboard" in curpath:
        return "../data.json"
    else:
        return "data.json"