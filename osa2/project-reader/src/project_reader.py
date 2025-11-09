from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        parsed_toml = toml.loads(content)
        poetryinfo = parsed_toml.get("tool").get("poetry")
        name = poetryinfo.get("name")
        description = poetryinfo.get("description")
        dependencies = poetryinfo.get("dependencies")
        devdep = poetryinfo.get("group").get("dev").get("dependencies")
        authors = poetryinfo.get("authors")
        lisenssi = poetryinfo.get("license")
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, devdep, lisenssi, authors)
