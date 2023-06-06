#include<Servo.h>
Servo my_servo;
char incoming_data;
int sled1=12;
void setup()
{
  Serial.begin(9600);
  my_servo.attach(9);
  pinMode(sled1,1);
}
void loop()
{
  if(Serial.available())
  {
    incoming_data = Serial.read();
    if(incoming_data == 'L')
    {
      my_servo.write(120);
      digitalWrite(sled1,1);
    }
    if(incoming_data == 'U')
    {
      my_servo.write(0);
      digitalWrite(sled1,0);
    }
  }
}
