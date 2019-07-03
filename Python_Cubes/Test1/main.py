from cubes import Workspace
from cubes.compat import ConfigParser

print("Python Cubes - Test1")

# Stwórz Workspace z pliku konfiguracyjnego:
conf = ConfigParser()
conf.read("slicer.ini")
workspace = Workspace(config = conf)

# Ładuj model:
workspace.import_model("model.json")

# Twórz obiekt browser:
browser = workspace.browser("POMIAR")

# Twórz wyniki agregacji, agreguj po GRUPA:
res = browser.aggregate(drilldown=["GRUPA"])

# Wyświetl podsumowanie całkowite i dla grupy:
print(res.summary)
for r in res:
    print(r)