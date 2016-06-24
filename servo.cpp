Servo leftservo;
Servo rightservo;
int posL = 0;
int posR = 0;
int leftSpeed = 30;
int rightSpeed = 30;
bool on = false;

void setup() {

    leftservo.attach(D0);
    Particle.function("setposL", setPosL);
    // Particle.variable("getposR", &posL, INT);

    rightservo.attach(D1);
    Particle.function("setposR", setPosR);
    // Particle.variable("getposL", &posR, INT);

    Particle.function("setpos", setPos);


}

void loop() {
}

int setPosL(String pstnL) {
    posL = pstnL.toInt();
    leftservo.write(90 + posL + 8);
    return posL;
}

int setPosR(String pstnR) {
    posR = pstnR.toInt();
    rightservo.write(90 - posR);
    return posR;
}

int setPos(String s) {
    int commapos = s.indexOf(",");
    setPosL(s.substring(0,commapos));
    setPosR(s.substring(commapos+1, s.length()));
    return 1;
}
