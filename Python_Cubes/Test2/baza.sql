# Skrypt tworzący testową bazę danych.

CREATE TABLE POMIAR (ROK INTEGER, GRUPA TEXT, WARTOSC REAL);
INSERT INTO POMIAR VALUES
(1996, "temp", 36.6),
(1997, "temp", 37.2),
(1998, "temp", 35.3),
(1996, "temp", 35.8),
(1997, "temp", 36.6),
(1998, "temp", 36.0),
(1996, "temp", 38.1),
(1997, "hum", 78.0),
(1998, "hum", 67.0),
(1996, "hum", 57.0),
(1997, "hum", 64.0);
