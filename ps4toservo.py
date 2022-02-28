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
        servos.write(b'#5WD100\r')

    def on_R1_release(self):
        servos.write(b'#5WD0\r')

    def on_R2_press(self, value):
        servos.write(b'#5WD-100\r')

    def on_R2_release(self):
        servos.write(b'#5WD0\r')
    
    def on_up_arrow_press(self):
        servos.write(b'#2WD50\r')

    def on_up_down_arrow_release(self):
        servos.write(b'#2WD0\r')
        
    def on_down_arrow_press(self):
        servos.write(b'#2WD-50\r')

    def on_L3_up(self, value):
        servos.write(b'#3WD50\r')

    def on_L3_y_at_rest(self):
        servos.write(b'#3WD0\r')

    def on_L3_down(self, value):
        servos.write(b'#3WD-50\r')
        
    def on_R3_up(self, value):
        servos.write(b'#4WD50\r')

    def on_R3_y_at_rest(self):
        servos.write(b'#4WD0\r')

    def on_R3_down(self, value):
        servos.write(b'#4WD-50\r')

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
