# Biblioteka do obsługi dongla USB nRF24L01.

import serial

class Dongiel:
    # Funkcja inicjalizująca obiekt Dongiel. Otwiera serial port z donglem USB nRF24L01:
    def __init__(self, serial_dev = "/dev/ttyUSB0", serial_baud = 115200, serial_timeout = None):
        self.ser = serial.Serial(serial_dev, serial_baud, timeout=serial_timeout)

    # Funkcja wysyłająca ramkę radiową:
    def send(self, mes):
        mes = mes + b"\x13"
        if len(mes) == 31:
            self.ser.write(mes)

    # Funkcja odbierająca ramkę radiową:
    def recv(self):
        mes = b""
        # Czekaj dopóki nie będzie odebranych 31 bajtów z seriala:
        while len(mes) != 31:
            sup = self.ser.read_until(b"\x13")
            # Jeżeli nic nie udało się odebrać w ustalonym czasie to zakończ nic nie zwracając:
            if len(sup) == 0 and len(mes) == 0:
                return
            mes = mes + sup
            # Sprawdź czy komunikat nie jest za długi:
            if len(mes) > 31: # Coś nie tak z synchronizacją, wyrzucamy ten komunikat:
                mes = b""
        # Zwróć ramkę bez ostatniego bajtu:
        return mes[0:30]