/**
 *
 * HX711 library for Arduino - example file
 * https://github.com/bogde/HX711
 *
 * MIT License
 * (c) 2018 Bogdan Necula
 *
**/
#include "HX711.h"


// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;


HX711 scale;

void setup() {
  Serial.begin(38400); //init serial output d=baud rate
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN); //pass pin
  // scale.read();
  // scale.read();
  // scale.read_average(20);
  // scale.get_value(5);
  // scale.get_units(5);
  scale.set_scale(2280.f);                      // this value is obtained by calibrating the scale with known weights; see the README for details
  scale.tare(); //reset zero 
  // scale.read();              // print a raw reading from the ADC
  // scale.read_average(20);
  // scale.get_value(5);	
  // scale.get_units(5);      
}

void loop() {

  Serial.println(scale.get_units(), 1);
  // Serial.print("\n");
  delay(200);

}
