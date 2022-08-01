import pyttsx3

motor=pyttsx3.init()

rate=motor.getProperty('rate')
print(rate)
motor.setProperty('rate',125)

volume=motor.getProperty('volume')
print(volume)
motor.setProperty('volume',1.0)

vozes=motor.getProperty('voices')

motor.setProperty('voice',vozes[1].id)
motor.say("Olá mundo")
motor.say("Minha taxa de fala atual é:"+str(rate))
motor.runAndWait()
motor.stop()

motor.save_to_file("Olá mundo!",'test.mp3')
motor.runAndWait()