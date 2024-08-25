import mesop as me
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)

GPIO.output(3,GPIO.HIGH)

@me.page(path="/")
def app():
  me.text("Hello World")
  me.button(
    'click me',
    on_click = hello_world()
  )
  me.text(
    'hi'
  )

def hello_world():
  print('hello world')