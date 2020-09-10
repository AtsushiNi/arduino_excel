void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("number:1,time:10,value1:4.2,value2:-2.3");
  Serial.println("number:2,time:20,value1:4.23,value2:-2.3");
  Serial.println("number:3,time:30,value1:4.223,value2:-2.3");
  Serial.println("number:4,time:40,value1:0.223,value2:-2.3");
  Serial.println("number:5,time:50,value1:4.129,value2:-2.3");
  Serial.println("number:6,time:60,value1:10.2,value2:-2.3");
  Serial.println("number:7,time:70,value1:42.2000,value2:-2.3");
  Serial.println("number:8,time:80,value1:1.2,value2:-2.3");
  Serial.println("number:9,time:90,value1:2.2,value2:-2.3");
  Serial.print("number:10,");
  Serial.print("time:100,");
  Serial.print("value1:");
  int value1 = 10;
  Serial.print(value1);
  Serial.println(",value2:-2.3");
}
