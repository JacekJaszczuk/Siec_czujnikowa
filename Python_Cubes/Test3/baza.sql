# Skrypt tworzący testową bazę danych.

PRAGMA foreign_keys = ON;

CREATE TABLE PACJENT (PESEL INTEGER NOT NULL PRIMARY KEY, IMIE TEXT, NAZWISKO TEXT, PLEC TEXT);
INSERT INTO PACJENT VALUES
(1, "BARBARA", "KOT", "K"),
(2, "TOMASZ", "GRZYB", "M"),
(3, "HUBERT", "CZARODZIEJ", "M");

CREATE TABLE POMIAR (PESEL INTEGER, ROK INTEGER, GRUPA TEXT, WARTOSC REAL, FOREIGN KEY(PESEL) REFERENCES PACJENT(PESEL));
INSERT INTO POMIAR VALUES
(1, 1996, "temp", 36.6),
(2, 1997, "temp", 37.2),
(3, 1998, "temp", 35.3),
(1, 1996, "temp", 35.8),
(2, 1997, "temp", 36.6),
(2, 1998, "temp", 36.0),
(2, 1996, "temp", 38.1),
(3, 1997, "gluk", 78.0),
(3, 1998, "gluk", 67.0),
(1, 1996, "gluk", 57.0),
(1, 1997, "gluk", 64.0);

CREATE VIEW WIDOK AS
SELECT P.PLEC, M.ROK, M.GRUPA, M.WARTOSC FROM POMIAR AS M LEFT JOIN PACJENT AS P ON M.PESEL == P.PESEL;