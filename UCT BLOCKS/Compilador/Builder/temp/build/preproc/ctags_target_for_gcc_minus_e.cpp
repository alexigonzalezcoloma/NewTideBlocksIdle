# 1 "C:\\Users\\Alonso\\Documents\\GitHub\\NewTideBlocksIdle\\Solo_IDLE\\Compilador\\Builder\\temp\\temp\\temp.ino"
# 1 "C:\\Users\\Alonso\\Documents\\GitHub\\NewTideBlocksIdle\\Solo_IDLE\\Compilador\\Builder\\temp\\temp\\temp.ino"
# 2 "C:\\Users\\Alonso\\Documents\\GitHub\\NewTideBlocksIdle\\Solo_IDLE\\Compilador\\Builder\\temp\\temp\\temp.ino" 2
void setup() {
  Serial.begin(9600);
  pinMode(1, 0x1);
  pinMode(2, 0x1);
  pinMode(3, 0x1);
  pinMode(4, 0x1);
  pinMode(5, 0x1);
  pinMode(6, 0x1);
  pinMode(7, 0x1);
  pinMode(8, 0x1);
  pinMode(9, 0x1);
  pinMode(10, 0x1);
  pinMode(11, 0x1);
  pinMode(12, 0x1);
  pinMode(13, 0x1);
}

void loop() {


    for (int i=0; i<=1; i++){
        digitalWrite(13, 0x1);
        digitalWrite(4, 0x1);
        delay(3000);
        digitalWrite(13, 0x0);
        digitalWrite(4, 0x0);
    }
}
