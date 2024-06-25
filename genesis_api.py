import requests # Documentation: http://requests.readthedocs.io

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
    
    with open("find.txt","w") as fobj:
        for key, value in response.items():
            fobj.write("{:*^50}\n".format(key))
            if type(value) == dict:
                for param, specifics in value.items():
                    fobj.write("{}: {}\n".format(param, specifics))
                fobj.write("\n")
            elif type(value) == list:
                for hit in value:
                    if type(hit) == dict:
                        for param, specifics in hit.items():
                            fobj.write("{}: {}\n".format(param, specifics))
                        fobj.write("\n")
            else:
                fobj.write("{}\n".format(value))

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
    print(request.status_code)
    response = request.json()
    print(response)

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
    print(request.status_code)
    response = request.json()
    print(response)

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
    print(request.status_code)
    response = request.json()
    print(response)

# ... work in progress ... :-)