#include <SPI.h>
#include <SD.h>
#include "High_Temp.h"

const int pressurePin = A1;  // Pressure sensor is at A1
const float REFERENCE_VOLTAGE = 5.0;
const int chipSelect = 2;
const int greenLEDPin = 8; // Pin connected to the green LED
const int redLEDPin = 9;   // Pin connected to the red LED

HighTemp ht(A4, A5);

void setup() {
  Serial.begin(9600);
  
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);

  if (!SD.begin(chipSelect)) {
    Serial.println("Card initialization failed!");
    digitalWrite(redLEDPin, HIGH);  // Turn on the red LED continuously
    while (1);  // Halt further execution
}


  if (!SD.exists("data.csv")) {
    File dataFile = SD.open("data.csv", FILE_WRITE);
    dataFile.close();
}
  Serial.println("Card initialized.");
  ht.begin();
}

void loop() {
  int pressureValue = analogRead(pressurePin);
  float pressureVoltage = (pressureValue / 1023.0);
  float P  =(pressureVoltage-0.04+0)/0.009;
  int analogValue;  // Variable to hold the analog value of the room temperature sensor
  float roomTemp = ht.getRoomTmp(analogValue);  // Get the room temperature and its analog value



  File dataFile = SD.open("data.csv", FILE_WRITE);
  
  if (dataFile) {
  dataFile.print(millis()/1000);
    dataFile.print(",");
    dataFile.print(pressureVoltage);
    dataFile.print(",");
    dataFile.print(ht.getThmcVol());
    dataFile.print(",");
    dataFile.print(roomTemp);
    dataFile.print(",");
    dataFile.println(analogValue);  // Print the analog value to the CSV file
    dataFile.close();

    // Print the voltage readings to Serial Monitor
    Serial.print("Pressure Voltage: ");
    Serial.print(pressureVoltage);
    Serial.print(" Pressure [kPa]: ");
    Serial.print(P);
    Serial.print(" Temperature TC: ");
    Serial.print(ht.getThmc());
    Serial.print(" Temperature Voltage: ");
    Serial.print(ht.getThmcVol());
    Serial.print(" [mV] Temperature amb: ");
    Serial.print(ht.getRoomTmp(analogValue));
    Serial.println(" deg C written to SD card.");

    successBlink();
  } else {
    Serial.println("Error opening data.csv");
    errorBlink();
  } 

  // Check if the temperature is below 0 or above 100
  float temperatureTC = ht.getThmc(); // Read the temperature
  if (temperatureTC < 0 || temperatureTC > 100) {
    //temperatureWarningBlink();
  }
  delay(500);  // Wait for 5 seconds before the next reading
}

void successBlink() {
  digitalWrite(greenLEDPin, HIGH);
  delay(1000);  // LED on for 1 second
  digitalWrite(greenLEDPin, LOW);
}

void errorBlink() {
  for (int i = 0; i < 3; i++) {  // Blink the red LED 3 times
    digitalWrite(redLEDPin, HIGH);
    delay(500);  // LED on for 0.5 seconds
    digitalWrite(redLEDPin, LOW);
    delay(500);  // LED off for 0.5 seconds
  }
}

void temperatureWarningBlink() {
  for (int i = 0; i < 10; i++) {  // Blink the red LED 10 times
    digitalWrite(redLEDPin, HIGH);
    delay(100);  // LED on for 0.1 seconds
    digitalWrite(redLEDPin, LOW);
    delay(100);  // LED off for 0.1 seconds
  }
}
