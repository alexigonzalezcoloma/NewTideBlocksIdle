#include <Arduino.h>
#line 1 "C:\\Users\\Matias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Builder\\temp\\temp\\temp.ino"
#line 1 "C:\\Users\\Matias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Builder\\temp\\temp\\temp.ino"
#include <Servo.h>
#line 2 "C:\\Users\\Matias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Builder\\temp\\temp\\temp.ino"
void setup();
#line 19 "C:\\Users\\Matias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Builder\\temp\\temp\\temp.ino"
void loop();
#line 2 "C:\\Users\\Matias\\Documents\\GitHub\\NewTideBlocksIdle\\Traductor\\Compilador\\Builder\\temp\\temp\\temp.ino"
void setup() {
  Serial.begin(9600);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {

    digitalWrite(13, HIGH);
}
