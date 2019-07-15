#include <SPI.h>
#include <string.h>
#include <RF24.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// Zmienne do działania termometru:
OneWire oneWire(A2);
DallasTemperature sensors(&oneWire); 

// Zmienne do działania radia:
RF24 radio(9 ,10);           // 9 -> Pin CE, 10 -> Pin CSN.
uint8_t address[6] = "kor";  // Adres nadawania i odbierania.

// Wiadomości:
char mes_tem[] = "{\"temperature\": %s}\n\0\0\0\0\0\0\0\0\0\0";
char mes_out[30];
 
void rf24_init()
{
    // Konfiguruj nRF24+:
    radio.begin();
    radio.setAddressWidth(3);
    radio.setCRCLength(RF24_CRC_16);
    radio.setAutoAck(false);
    radio.setRetries(0, 0);
    radio.setChannel(110);
    radio.setPayloadSize(30);
    radio.setDataRate(RF24_2MBPS);
    radio.setPALevel(RF24_PA_MAX);
}
 
void rf24_open_pipe()
{
    radio.openWritingPipe(address);
    radio.openReadingPipe(0, address);
}

void setup()
{
    // Inicjalizuj UART:
    Serial.begin(115200);
    Serial.println(F("Rozpoczynam wysłanie pakietów"));

    // Inicjalizuj termometr:
    sensors.begin();

    // Inicjalizacja radia:
    rf24_init();
    rf24_open_pipe();
    radio.stopListening();
}

void loop()
{
    // Pobierz temperaturę i wyślij:
    sensors.requestTemperatures();
    float temp = sensors.getTempCByIndex(0);
    char temp_str[5];
    snprintf(mes_out, 30, mes_tem, dtostrf(temp, 5, 2, temp_str));
    Serial.print("Temperatura to: ");
    Serial.println(temp);
    radio.write(mes_out, 30);

    // Czekaj 2 sekundy:
    delay(2000);
}
