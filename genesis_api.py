import requests # Documentation: http://requests.readthedocs.io

def show_response(response: dict, path: str):
    
    with open(path,"w") as fobj:
        for section, content in response.items():
            
            # Formatting and writing of section titles
            fobj.write("{:*^50}\n".format(section))
            
            # Formatting and writing of dictionaries
            if type(content) == dict:
                for param, specifics in content.items():
                    fobj.write("{}: {}\n".format(param, specifics))
                fobj.write("\n")
            
            # Formatting and writing of lists
            elif type(content) == list:
                for elem in content:
                    if type(elem) == dict:
                        for param, specifics in elem.items():
                            fobj.write("{}: {}\n".format(param, specifics))
                        fobj.write("\n")
                    else:
                        fobj.write("{}\n".format(elem))
                        fobj.write("\n")
            
            # Formatting and writing of other information
            else:
                fobj.write("{}\n".format(content))
                fobj.write("\n")

def whoami():
    '''
    Method for testing the address.
    Returns the caller's IP address and hostname.

    Parameters required:
    None
    '''
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/helloworld/whoami")
    print(request.status_code)
    print(request.text)

def logincheck(username: str, password: str, language: str = "de"):
    '''
    Method for testing system login with access data.
    Confirms or denies successful system login.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    params = {
        "username": username,
        "password": password,
        "language": language
        }
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/helloworld/logincheck?", 
                           params = params)
    print(request.status_code)
    print(request.text)

def find(username: str, password: str, term: str, category: str = "all", pagelength: int = 100, language: str = "de"):
    '''
    Method for finding information based on one or more search terms.
    Returns lists of fitting objects (e.g. tables, time series).

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - term: "Comma-separated search terms"
    - category:
    --- "all" = default
    --- "tables"
    --- "statistics"
    --- "cubes"
    --- "variables"
    --- "time-series"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    params = {
        "username": username,
        "password": password,
        "term": term,
        "category": category,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/find/find?", 
                           params = params)
    # print(request.status_code)
    response = request.json()
    if type(response) == dict:
        show_response(response, "find.txt")
    else:
        pass

def catalogue():
    pass

def cubes(username: str, password: str, selection: str, area: str = "Alle", pagelength: int = 100, language: str = "de"):
    '''
    Method that for listing data cubes. 
    Returns a list of data cubes.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of data cube" (use of * possible)
    - area:
    --- internal users
    ----- "Meine/Benutzer"
    ----- "Gruppe"
    ----- "Amt"
    ----- "Katalog/Öffentlich"
    ----- "Alle" = default
    --- external users
    ----- "Meine/Benutzer"
    ----- "Katalog/Öffentlich"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    
    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes?",
                           params = params)
    #print(request.status_code)
    response = request.json()
    if type(response) == dict:
        show_response(response, "cubes.txt")
    else:
        pass

def cubes2statistic(username: str, password: str, name: str, selection: str, area: str = "Alle", pagelength: int = 100, language: str = "de"):
    '''
    Method for listing data cubes fitting a selected statistic.
    Returns a list of data cubes.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Code of statistic"    
    - selection: "Code of data cube" (use of * possible)
    - area:
    --- internal users
    ----- "Meine/Benutzer"
    ----- "Gruppe"
    ----- "Amt"
    ----- "Katalog/Öffentlich"
    ----- "Alle" = default
    --- external users
    ----- "Meine/Benutzer"
    ----- "Katalog/Öffentlich"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    
    params = {
        "username": username,
        "password": password,
        "name": name,        
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes2statistic?",
                           params = params)
    # print(request.status_code)
    response = request.json()
    if type(response) == dict:
        show_response(response, "cubes2statistic.txt")
    else:
        pass

def cubes2variable(username: str, password: str, name: str, selection: str, area: str = "Alle", pagelength: int = 100, language: str = "de"):
    '''
    Method for listing data cubes fitting a selected variable.
    Returns a list of data cubes.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Code of variable"    
    - selection: "Code of data cube" (use of * possible)
    - area:
    --- internal users
    ----- "Meine/Benutzer"
    ----- "Gruppe"
    ----- "Amt"
    ----- "Katalog/Öffentlich"
    ----- "Alle" = default
    --- external users
    ----- "Meine/Benutzer"
    ----- "Katalog/Öffentlich"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''    
    params = {
        "username": username,
        "password": password,
        "name": name,        
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes2variable?",
                           params = params)
    # print(request.status_code)
    response = request.json()
    if type(response) == dict:
        show_response(response, "cubes2variable.txt")
    else:
        pass

# ... work in progress ... :-)