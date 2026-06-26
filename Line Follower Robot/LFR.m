IR_SENSOR_LEFT = 11

enableLeftMotor = 9       
leftMotorPin1 = 2         
leftMotorPin2 = 3         

enableRightMotor = 10     
rightMotorPin1 = 4        
rightMotorPin2 = 5        

leftMotorSpeed = 150      
rightMotorSpeed = 150     

def digitalWrite(pin, condition):
  
    status = "HIGH" if condition else "LOW"
    return f"Pin {pin} set to {status}"

def analogWrite(pin, speed):
    return f"Pin {pin} speed set to {speed}"

print(digitalWrite(rightMotorPin1, rightMotorSpeed > 0))
print(digitalWrite(rightMotorPin2, rightMotorSpeed < 0))

print(digitalWrite(leftMotorPin1, leftMotorSpeed > 0))
print(digitalWrite(leftMotorPin2, leftMotorSpeed < 0))

print(analogWrite(enableRightMotor, abs(rightMotorSpeed)))
print(analogWrite(enableLeftMotor, abs(leftMotorSpeed)))
