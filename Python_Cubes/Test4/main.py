from cubes import Workspace

print("Python Cubes - Test3")

# Stwórz Workspace z pliku konfiguracyjnego:
workspace = Workspace()
workspace.register_default_store("sql", url="sqlite:///baza.sqlite")

# Ładuj model:
workspace.import_model("model.json")

# Twórz obiekt browser:
browser = workspace.browser("WIDOK")

# Twórz wyniki agregacji, agreguj po GRUPA:
res = browser.aggregate(drilldown=["GRUPA"])
res2 = browser.aggregate(drilldown=["ROK"])
res3 = browser.aggregate(drilldown=["PLEC"])
res4 = browser.aggregate(drilldown=["WIEK_CAT"])
res5 = browser.aggregate(drilldown=["WIEK_CAT", "GRUPA"])

# Wyświetl podsumowanie całkowite i dla grupy:
print(res.summary)
for r in res:
    print(r)

print("Ala ma kota!")

print(res2.summary)
for r in res2:
    print(r)

print("Ala ma kota!")

print(res3.summary)
for r in res3:
    print(r)

print("Ala ma kota!")

print(res4.summary)
for r in res4:
    print(r)

print("Ala ma kota!")

print(res5.summary)
for r in res5:
    print(r)