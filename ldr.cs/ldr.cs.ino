
const int ledPin = 13;
const int ldrPin = A0;

void setup() 
{
  Serial.begin(38400);
  pinMode(ledPin, OUTPUT);
  pinMode(ldrPin, INPUT);
}

void loop() 
{
  int ldrStatus = analogRead(ldrPin);
  Serial.println(ldrStatus);
  if (ldrStatus<=200)
  {
    digitalWrite(ledPin, LOW);
  }
  else
  {
    digitalWrite(ledPin, HIGH);
  }
}
