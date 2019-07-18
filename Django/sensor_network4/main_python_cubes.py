from cubes import Workspace

print("Python Cubes Test!")

# Stwórz Workspace z pliku konfiguracyjnego:
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///db.sqlite3")

# Ładuj model:
workspace.import_model("model.json")

# Twórz obiekt browser:
browser = workspace.browser("analiza_temperatura")

# Twórz wyniki agregacji, agreguj po GRUPA:
res = browser.aggregate(drilldown=["kontynent"])

# Wyświetl podsumowanie całkowite i dla grupy:
print(res.summary)
for r in res:
    print(r)