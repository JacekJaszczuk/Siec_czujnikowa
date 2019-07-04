from cubes import Workspace

print("Python Cubes - Test2")

# Stwórz Workspace z pliku konfiguracyjnego:
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///baza.sqlite")

# Ładuj model:
workspace.import_model("model.json")

# Twórz obiekt browser:
browser = workspace.browser("POMIAR")

# Twórz wyniki agregacji, agreguj po GRUPA:
res = browser.aggregate(drilldown=["GRUPA"])
res2 = browser.aggregate(drilldown=["ROK"])

# Wyświetl podsumowanie całkowite i dla grupy:
print(res.summary)
for r in res:
    print(r)

print("Ala ma kota!")

print(res2.summary)
for r in res2:
    print(r)