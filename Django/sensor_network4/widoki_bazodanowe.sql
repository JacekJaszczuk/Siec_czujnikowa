CREATE VIEW analiza_temperatura AS
SELECT
date(data) - date(data_urodzenia) AS "wiek_pacjenta",
data AS data_pomiaru,
kontynent,
kraj,
obszar,
wartosc
FROM (SELECT * FROM (SELECT * FROM aplikacja_pomiar AS c JOIN aplikacja_pacjent AS p WHERE c.pacjent_id == p.id) AS c JOIN aplikacja_miejsca AS m WHERE c.miejsce_id == m.id)
WHERE typ_pomiaru == "Temperatura";

CREATE VIEW analiza_glukoza AS
SELECT
date(data) - date(data_urodzenia) AS "wiek_pacjenta",
data AS data_pomiaru,
kontynent,
kraj,
obszar,
wartosc
FROM (SELECT * FROM (SELECT * FROM aplikacja_pomiar AS c JOIN aplikacja_pacjent AS p WHERE c.pacjent_id == p.id) AS c JOIN aplikacja_miejsca AS m WHERE c.miejsce_id == m.id)
WHERE typ_pomiaru == "Glukoza";