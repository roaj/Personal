#include <Arduino.h>
#include <AccelStepper.h>

unsigned long startTime ;
unsigned long waitTime = 240000; //4 minutes
int microsteping = 800; // steps/rev
int leadPitch = 10; // mm/rev


// PINS
int leftDIR = 6; 
int leftSTEP = 7; 
AccelStepper leftStepper(1,leftSTEP,leftDIR);

int flag = 2; // 1 if activated 

//FLAGS
int DIR = HIGH; // flag to switch leftDIRection of motion  
boolean home = false;
boolean newData = false;
boolean goingDown = false;
char receivedChar;

float mm2step(float mm){  
  float revolutions = mm / leadPitch ;
  float steps = revolutions * microsteping; 
  return steps;
}

void Up(){
  leftStepper.move(mm2step(400));
}

void Down(){
  leftStepper.move(mm2step(-395));
}

void updateFlag() {
    if (digitalRead(flag) == 1 ) {
      home = true;
    }  
    else if (digitalRead(flag) == 0){
      home = false;
    }
}

void stopStepper(){
  leftStepper.stop();
}

void zeroPosition(){
  leftStepper.setCurrentPosition(0);
}

void recvOneChar() {
 if (Serial.available() > 0){
 receivedChar = Serial.read();
 newData = true;
 }
}

void wait(){
  startTime = millis();
  while (millis() - startTime < waitTime){   
          }
}



void setup() {
  Serial.begin(9600);
  pinMode(flag,INPUT);
  //ACCEL STEPPER
  leftStepper.setMaxSpeed(2000); // step/sec
  leftStepper.setAcceleration(1000000); // step/sec^2
  updateFlag();
  delay(2000);
}

void loop() { 

  if (leftStepper.distanceToGo() == 0 )
    {
      goingDown = false;
      recvOneChar();

      if (newData == true && receivedChar == 'u'){
        Serial.println(receivedChar);
        leftStepper.setMaxSpeed(4000); // step/sec
        Up();
        newData = false;
      }

      else if (newData == true && receivedChar == 'd'){
        Serial.println(receivedChar);
        leftStepper.setMaxSpeed(1000); // step/sec
        Down();
        goingDown = true;
        newData = false;
      }



      else if (newData == true && receivedChar == 'p'){


        Serial.println("...Proccess beginning...");
        updateFlag();

        if (home == false){
          Up();
          delay(2000);
          Serial.println("going up");
          while (leftStepper.distanceToGo() != 0){
              leftStepper.run();
              updateFlag();
              if (home == true){
                stopStepper();
                zeroPosition();
              }
          }
          
        }
        
        delay(2000);

        if (home == true){
          //the process begins here 
        }
        // else if (home == true){
        //   Serial.println("Ready to start process...");
        //   delay(2000);
        //   Down();
        //   Serial.println("PROCESS --> going down");
        //   while(leftStepper.distanceToGo() != 0){
        //     leftStepper.run();
        //     }
        //   wait();
        //   Up();
        //   Serial.println("PROCESS --> going up");
        //   while(leftStepper.distanceToGo() != 0){
        //     leftStepper.run();
        //     updateFlag();

        //     }
        // }
      
      }
    
    
    }  // inside this   

  leftStepper.run();
  updateFlag();

    if (home == true && goingDown == false){
      stopStepper();
      zeroPosition();
    }
  
  }



