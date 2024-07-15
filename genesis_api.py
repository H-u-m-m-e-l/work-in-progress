import requests # Documentation: http://requests.readthedocs.io

def show(response: dict, path: str = "search_hits.txt"):
    
    if type(response) == dict:
    
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

                    fobj.write("Search hits:{}\n\n".format(len(content)))

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
    else:
        pass

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
    #print(request.text)

def find(*, username: str, password: str, term: str, category: str = "all",
         pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns lists of objects (e.g. tables, time series) fitting one or more search terms.

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
    return request.json()
    
def cubes(*, username: str, password: str, selection: str, area: str = "Alle",
          pagelength: int = 100, language: str = "de") -> dict:
    '''
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
    return request.json()

def cubes2statistic(*, username: str, password: str, name: str, selection: str,
                    area: str = "Alle", pagelength: int = 100,
                    language: str = "de") -> dict:
    '''
    Returns a list of data cubes fitting a selected statistic.

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
    return request.json()

def cubes2variable(*, username: str, password: str, name: str, selection: str,
                   area: str = "Alle", pagelength: int = 100,
                   language: str = "de") -> dict:
    '''
    Returns a list of data cubes fitting a selected variable.

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
    return request.json()

def jobs(*, username: str, password: str, selection: str, searchcriterion: str,
         sortcriterion: str, type: str = "Alle", area: str = "Alle",
         pagelength: int = 100, language: str = "de")-> dict:
    '''
    Returns a list of jobs.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Code of variable"    
    - selection: "Code of job" (use of * possible)
    - searchcriterion:
    --- "Auftragstyp"
    --- "Status"
    --- "Zeitpunkt"
    - sortcriterion:
    --- "Auftragstyp"
    --- "Status"
    --- "Zeitpunkt"
    - kind:
    --- "Alle" = default
    --- "Import"
    --- "Export"
    --- "Werteabruf"
    --- "Summenquader berechnen"
    --- "Datenquader bereinigen"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "type": type,
        "area": area,        
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/jobs?",
                           params = params)
    
    # print(request.status_code)
    return request.json()

def modifieddata(*, username: str, password: str, selection: str, date: str,
                 type: str = "Alle", pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of updated objects as of a specified date. 

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of object" (use of * possible)
    - date: "dd.mm.yyyy"
    - kind:
    --- "Alle" = default
    --- "Tabellen"
    --- "Statistiken"
    --- "StatistikUpdates"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    
    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "type": type,
        "date": date,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/modifieddata?",
                           params = params)

    #print(request.status_code)
    return request.json()

def qualitysigns(*, language: str = "de") -> dict:
    '''
    Returns a list of quality indicators.

    Parameters required:
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    
    params = {
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/qualitysigns?",
                           params = params)
        
    #print(request.status_code)
    return request.json()

def results(*, username: str, password: str, selection: str, area: str = "Alle",
            pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of tables.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of table" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/results?",
                           params = params)

    #print(request.status_code)
    return request.json()

def statistics(*, username: str, password: str, selection: str,
               searchcriterion: str = "code", sortcriterion: str = "code",
               pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of statistics.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of statistics" (use of * possible)
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    
    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/statistics?",
                           params = params)

    #print(request.status_code)
    return request.json()

def statistics2variable(*, username: str, password: str, name: str, selection: str,
                        area: str = "Alle", searchcriterion: str = "code",
                        sortcriterion: str = "code", pagelength: int = 100,
                        language: str = "de") -> dict:
    '''
    Returns a list of statistics fitting a selected variable.

    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Name of variable"    
    - selection: "Code of statistic" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/statistics2variable?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def tables(*, username: str, password: str, selection: str, area: str = "Alle",
           searchcriterion: str = "code", sortcriterion: str = "code",
           pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of tables.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of table" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def tables2statistic(*, username: str, password: str, name: str, selection: str,
                    area: str = "Alle", pagelength: int = 100, 
                    language: str = "de") -> dict:
    '''
    Returns a list of tables fitting a selected statistic.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Name of statistic"
    - selection: "Code of table" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables2statistic?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def tables2variable(*, username: str, password: str, name: str, selection: str,
                    area: str = "Alle", pagelength: int = 100, 
                    language: str = "de") -> dict:
    '''
    Returns a list of tables fitting a selected variable.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Name of variable"
    - selection: "Code of table" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables2variable?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def terms(*, username: str, password: str, selection: str, pagelength: int = 100,
           language: str = "de") -> dict:
    '''
    Returns a list of terms.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of term" (use of * possible)
    - pagelength: 1 up to 2500, 100 = default
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''

    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/terms?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def timeseries(*, username: str, password: str, selection: str, area: str = "Alle",
               pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of time series.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of time series" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def timeseries2statistic(*, username: str, password: str, name: str, selection: str,
                         area: str = "Alle", pagelength: int = 100,
                         language: str = "de") -> dict:
    '''
    Returns a list of time series fitting a selected statistic.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Code of statistic"
    - selection: "Code of time series" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries2statistic?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def timeseries2variable(*, username: str, password: str, name: str, selection: str,
                        area: str = "Alle", pagelength: int = 100,
                        language: str = "de") -> dict:
    '''
    Returns a list of time series fitting a selected variable.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Name of variable"
    - selection: "Code of time series" (use of * possible)
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
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries2variable?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def values(*, username: str, password: str, selection: str, area: str = "Alle",
           searchcriterion: str = "code", sortcriterion: str = "code",
           pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of values.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of value" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/values?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def values2variable(*, username: str, password: str, name: str, selection: str,
                    area: str = "Alle", searchcriterion: str = "code",
                    sortcriterion: str = "code", pagelength: int = 100,
                    language: str = "de") -> dict:
    '''
    Returns a list of values for a selected variable.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Name of variable"
    - selection: "Code of value" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/values2variable?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def variables(*, username: str, password: str, selection: str, area: str = "Alle",
              searchcriterion: str = "code", sortcriterion: str = "code",
              pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of variables.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - selection: "Code of variable" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/variables?",
                           params = params)
    
    #print(request.status_code)
    return request.json()

def variables2statistic(*, username: str, password: str, name: str, selection: str,
                        area: str = "Alle", searchcriterion: str = "code",
                        sortcriterion: str = "code", type: str = "alle",
                        pagelength: int = 100, language: str = "de") -> dict:
    '''
    Returns a list of variables fitting a selected statistic.
    
    Parameters required:
    - username: "User name of GENESIS account"
    - password: "Password of GENESIS account"
    - name: "Code of statistic"
    - selection: "Code of variable" (use of * possible)
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
    - searchcriterion:
    --- "Code" = default
    --- "Inhalt"
    - sortcriterion:
    --- "Code" = default
    --- "Inhalt"
    - type:
    --- "klassifizierend"
    --- "insgesamt"
    --- "räumlich"
    --- "sachlich"
    --- "wert"
    --- "zeitlich"
    --- "zeitidentifizierend"
    --- "alle" = default
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
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "type": type,
        "pagelength": pagelength,
        "language": language
        }
    
    request = requests.get("https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/variables2statistic?",
                           params = params)

    #print(request.status_code)
    return request.json()

# ... work in progress ... :-)