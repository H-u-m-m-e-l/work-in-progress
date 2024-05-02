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

def logincheck(username: str, password: str, language:str = "de"):
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
    Returns lists of fitting objects (e.g. tables).

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
    print(request.status_code)
    response = request.json()

    with open("search_results.txt", "w") as fobj:
        for key in response:
            fobj.write(f"+++++ {key} +++++ \n")
            if type(response[key]) == list:
                for elem in response[key]:
                    fobj.write(f"{elem} \n")
            else:
                fobj.write(f"{response[key]} \n\n")

# ... TO BE CONTINUED ... :-)