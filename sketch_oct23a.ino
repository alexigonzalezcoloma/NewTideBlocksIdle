#include <Servo.h>
int green  = 4;
int red    = 6;
int yellow = 5;
int white  = 13;
int PA     = 3;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(white, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(PA, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(14, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
      int mssg = Serial.read(); //leemos el serial
      if(mssg == 'w'){digitalWrite(white, HIGH);}
      if(mssg == 'r'){digitalWrite(red, HIGH);}
      if(mssg == 'y'){digitalWrite(yellow, HIGH);}
      if(mssg == 'g'){digitalWrite(green, HIGH);}
      if(mssg == 'p'){digitalWrite(PA, HIGH);}
      if(mssg == 's'){
         digitalWrite(white, LOW);
         digitalWrite(red, LOW);
         digitalWrite(yellow, LOW);
         digitalWrite(green, LOW);
         digitalWrite(PA, LOW);}
   }
}
