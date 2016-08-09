#include <Servo.h>

#define INSERTER_INPUT_PIN 8
#define INDEXER_OUTPUT_PIN 8 
#define INSERTER_OUTPUT_PIN 9

Servo indexer;
Servo inserter;
String input, lastInput;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(20);

  pinMode(INSERTER_INPUT_PIN, INPUT);
  indexer.attach(INDEXER_OUTPUT_PIN);
  inserter.attach(INSERTER_OUTPUT_PIN);
  lastInput = "";
}


void loop() {
     if(digitalRead(INSERTER_INPUT_PIN) == 1) {
      Serial.println("BUTTON_PRESS");
      inserter.write(0);
      delay(900);
      inserter.write(180);
      delay(900);
    }
    while(Serial.available()) {
      input = Serial.readString();
      if(lastInput != input)
        indexer.write(input.toInt());
      Serial.println(input);
      lastInput = input;
    }
}
