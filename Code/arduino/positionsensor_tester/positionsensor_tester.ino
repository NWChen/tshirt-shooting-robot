int sensorPin = A0;    // input pin for the position sensor

// test values
int values[100];
int max_value = 0;
int min_value = 999;
int i = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  i = map(analogRead(sensorPin), 41, 981, 0, 360);
  Serial.println(String(i));
  delay(10);
}

/*
 * Find max value.
 */
/*
void loop() {
  values[i] = analogRead(sensorPin);
  
  // iterate through values
  i++;
  if(i==100) i = 0;

  if(values[i]==0) values[i] = 500;
  if(values[i] > max_value) max_value = values[i];
  if(values[i] < min_value) min_value = values[i];
  
  Serial.println(String(max_value) + ", " + String(min_value) + ", " + String(values[i]));
}
*/
