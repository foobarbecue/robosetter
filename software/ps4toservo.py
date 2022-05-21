from pyPS4Controller.controller import Controller
import serial
import logging
from datetime import datetime
servos = serial.Serial('/dev/ttyUSB0',115200)
log_filename = f"robosetter_{datetime.now()}.txt".replace(' ','_')
logging.basicConfig(filename=log_filename, level=logging.INFO)
# log csv header
servo_nums = range(1,5)
telemetry_queries = {'status':'Q', 'position':'QD', 'current':'QC', 'voltage':'QV'}
logging.info(
    'timestamp'+','.join([f' servo{servo_num}{k}' for servo_num in servo_nums for k, v in telemetry_queries.items()])
)

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



def log_servos_telemetry():
    """
    Poll servos for status, current, and voltage and write a comma-delimited row with:
        timestamp, status 1 to 5, position 1 to 5, current 1 to 5, voltage 1 to 5
    """
    telemetry_log_row=[]
    for servo_num in servo_nums:
        for telem_type, query_str in telemetry_queries.items():
            servos.write(bytes(f'#{servo_num}{query_str}\r','ascii'))
            servo_outp = servos.read_until(b'\r') 
            telemetry_log_row.append(servo_outp)
    logging.info(str(datetime.now()) + ','.join([v.decode() for v in telemetry_log_row]))
    return
    
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_sequence=[{'inputs':[], 'callback':log_servos_telemetry}]) 