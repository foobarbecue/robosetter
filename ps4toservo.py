from pyPS4Controller.controller import Controller
import serial

servos = serial.Serial('/dev/ttyUSB0',115200)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L1_press(self):
        servos.write(b'#1WD100\r')

    def on_L1_release(self):
        servos.write(b'#1WD0\r')

    def on_L2_press(self, value):
        servos.write(b'#1WD-100\r')

    def on_L2_release(self):
        servos.write(b'#1WD0\r')

    def on_R1_press(self):
        servos.write(b'#4WD100\r')

    def on_R1_release(self):
        servos.write(b'#4WD0\r')

    def on_R2_press(self, value):
        servos.write(b'#4WD-100\r')

    def on_R2_release(self):
        servos.write(b'#4WD0\r')

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
