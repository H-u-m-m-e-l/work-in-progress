import requests # Documentation: http://requests.readthedocs.io

# OOP -  ... work in progress ... :-)
class GenesisAPI:
    def __init__(self, method: str, params: dict = None):
        self.method = method
        self.params = params
        self.URL_BASIC = "https://www-genesis.destatis.de/genesisWS/rest/2020/"
        self.URL_EXTENSION = {"whoami": "helloworld/whoami",
                              "logincheck": "helloworld/logincheck?",
                              "find": "find/find?",
                              "cubes": "catalogue/cubes?",
                              "cubes2statistic": "catalogue/cubes2statistic?",
                              "cubes2variable": "catalogue/cubes2variable?",
                              "jobs": "catalogue/jobs?",
                              "modifieddata": "catalogue/modifieddata?",
                              "qualitysigns": "catalogue/qualitysigns?",
                              "results": "catalogue/results?",
                              "statistics": "catalogue/statistics?",
                              "statistics2variable": "catalogue/statistics2variable?",
                              "tables": "catalogue/tables?",
                              "tables2statistic": "catalogue/tables2statistic?",
                              "tables2variable": "catalogue/tables2variable?",
                              "terms": "catalogue/terms?",
                              "timeseries": "catalogue/timeseries?",
                              "timeseries2statistic": "catalogue/timeseries2statistic?",
                              "timeseries2variable": "catalogue/timeseries2variable?",
                              "values": "catalogue/values?",
                              "values2variable": "catalogue/values2variable?",
                              "variables": "catalogue/variables?",
                              "variables2statistic": "catalogue/variables2statistic?"
                              }
        self.response = {}

    def request(self) -> bool:
        URL = self.URL_BASIC + self.URL_EXTENSION[self.method]
        self.response = requests.get(URL, self.params).json()
        return True
    
    def show_hits(self, path: str = "search_hits.txt") -> bool:
        if self.request():
            with open(path,"w") as fobj:
                for section, content in self.response.items():

                    # Formatting and writing of section titles
                    fobj.write(f"{section:*^50}\n")

                    # Formatting and writing of dictionaries
                    if type(content) == dict:
                        for param, specifics in content.items():
                            fobj.write(f"{param}: {specifics}\n")
                        fobj.write("\n")
                    
                    # Formatting and writing of lists
                    elif type(content) == list:
                        fobj.write(f"Search hits:{len(content)}\n\n")

                        for elem in content:
                            if type(elem) == dict:
                                for param, specifics in elem.items():
                                    fobj.write(f"{param}: {specifics}\n")
                                fobj.write("\n")
                            else:
                                fobj.write(f"{elem}\n")
                                fobj.write("\n")
                    
                    # Formatting and writing of other information
                    else:
                        fobj.write(f"{content}\n")
                        fobj.write("\n")
            return True
        else:
            return False  


# FP
def request(url: str, params: dict = None) -> dict:
    response = requests.get(url, params)

    #print(response.status_code)
    #print(response.text)
    return response.json()

def show_hits(response: dict, path: str = "search_hits.txt"):
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

def whoami() -> dict:
    '''
    Method for testing the address.
    Returns the caller's IP address and hostname.

    Parameters required:
    None
    '''
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/helloworld/whoami"
    
    return request(URL)

def logincheck(# Login details
               username: str, password: str,
               # General
               language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/helloworld/logincheck?"

    params = {
        "username": username,
        "password": password,
        "language": language
        }
    
    return request(URL, params)

def find(# Login details
         username: str, password: str,
         # Custom
         term: str, category: str = "all",
         # List control
         pagelength: int = 100,
         # General
         language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/find/find?"

    params = {
        "username": username,
        "password": password,
        "term": term,
        "category": category,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def cubes(# Login details
          username: str, password: str,
          # Filter
          selection: str, area: str = "Alle",
          # List control
          pagelength: int = 100,
          # General
          language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes?"
    
    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def cubes2statistic(# Login details
                    username: str, password: str,
                    # Filter
                    name: str, selection: str, area: str = "Alle",
                    # List control
                    pagelength: int = 100,
                    # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes2statistic?"

    params = {
        "username": username,
        "password": password,
        "name": name,        
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def cubes2variable(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/cubes2variable?"

    params = {
        "username": username,
        "password": password,
        "name": name,        
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def jobs(# Login details
        username: str, password: str,
        # Filter
        searchcriterion: str, selection: str, sortcriterion: str,
        area: str = "Alle", type: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/jobs?"
    params = {
        "username": username,
        "password": password,
        "searchcriterion": searchcriterion,
        "selection": selection,
        "sortcriterion": sortcriterion,
        "area": area,
        "type": type,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def modifieddata(# Login details
        username: str, password: str,
        # Filter
        date: str, selection: str, type: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/modifieddata?"
    params = {
        "username": username,
        "password": password,
        "date": date,
        "selection": selection,
        "type": type,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def qualitysigns(# General
        language: str = "de") -> dict:
    '''
    Returns a list of quality indicators.

    Parameters required:
    - language:
    --- "de" (German) = default
    --- "en" (English)
    '''
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/qualitysigns?"
    
    params = {
        "language": language
        }
    
    return request(URL, params)

def results(# Login details
        username: str, password: str,
        # Filter
        selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/results?"

    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def statistics(# Login details
        username: str, password: str,
        # Filter
        selection: str, searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/statistics?"

    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "searchcriterion": searchcriterion,
        "sortcriterion": sortcriterion,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def statistics2variable(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle", 
        searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/statistics2variable?"
    
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
    
    return request(URL, params)

def tables(# Login details
        username: str, password: str,
        # Filter
        selection: str, area: str = "Alle",
        searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables?"
    
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
    
    return request(URL, params)

def tables2statistic(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables2statistic?"

    params = {
        "username": username,
        "password": password,
        "name": name,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)
    
def tables2variable(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/tables2variable?"

    params = {
        "username": username,
        "password": password,
        "name": name,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def terms(# Login details
        username: str, password: str,
        # Filter
        selection: str,
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/terms?"

    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def timeseries(# Login details
        username: str, password: str,
        # Filter
        selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries?"

    params = {
        "username": username,
        "password": password,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def timeseries2statistic(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries2statistic?"

    params = {
        "username": username,
        "password": password,
        "name": name,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def timeseries2variable(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/timeseries2variable?"

    params = {
        "username": username,
        "password": password,
        "name": name,
        "selection": selection,
        "area": area,
        "pagelength": pagelength,
        "language": language
        }
    
    return request(URL, params)

def values(# Login details
        username: str, password: str,
        # Filter
        selection: str, area: str = "Alle", 
        searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/values?"
    
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
    
    return request(URL, params)

def values2variable(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle",
        searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/values2variable?"
    
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
    
    return request(URL, params)

def variables(# Login details
        username: str, password: str,
        # Filter
        selection: str, area: str = "Alle",
        searchcriterion: str = "code", sortcriterion: str = "code",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/variables?"
    
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
    
    return request(URL, params)

def variables2statistic(# Login details
        username: str, password: str,
        # Filter
        name: str, selection: str, area: str = "Alle", searchcriterion: str = "code",
        sortcriterion: str = "code", type: str = "Alle",
        # List control
        pagelength: int = 100,
        # General
        language: str = "de") -> dict:
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
    URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/catalogue/variables2statistic?"
    
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
    
    return request(URL, params)

# ... work in progress ... :-)