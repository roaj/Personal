#!/usr/bin/env python3
# import python libraries
import time, math
import getopt, sys

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.servo as servo
import rcpy.clock as clock

def usage():
    print("""usage: python rcpy_test_servos [options] ...
Options are:
-d duty     define a duty cycle from -1.5 to 1.5
-c servo    specify a single servo from 1-8, 0 for all servos
-s          sweep servos back and forward at duty cycle
-t period   period
-h          print this help message""")

def main(duty):

    # # exit if no options
    # if len(sys.argv) < 2:
    #     usage()
    #     sys.exit(2)
    
    # # Parse command line
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], "hst:d:c:", ["help"])

    # except getopt.GetoptError as err:
    #     # print help information and exit:
    #     print('rcpy_test_servos: illegal option {}'.format(sys.argv[1:]))
    #     usage()
    #     sys.exit(2)

    # defaults
    # duty = 1.5
    period = 0.02
    channel = 0
    sweep = False
    brk = False
    free = False

    rcpy.set_state(rcpy.RUNNING)
    srvo = servo.Servo(channel)
    srvo.set(duty)
    clck = clock.Clock(srvo, period)
    
    servo.enable()
    clck.start()
    # try:

        # enable servos
        # print("here")
        # start clock
        # print("here2")
        # # sweep
        # if sweep:

        #     d = 0
        #     direction = 1
        #     duty = math.fabs(duty)
        #     delta = duty/100
            
        #     # keep running
        #     while rcpy.get_state() != rcpy.EXITING:

        #         # increment duty
        #         d = d + direction * delta

        #         # end of range?
        #         if d > duty or d < -duty:
        #             direction = direction * -1
        #             if d > duty:
        #                 d = duty
        #             else:
        #                 d = -duty
                    
        #         srvo.set(d)

        #         # sleep some
        #         time.sleep(.02)

        # # or do nothing
        # else:

            # keep running
    # while rcpy.get_state() != rcpy.EXITING:
            
            # sleep some
        # time.sleep(0.5)
            
    # except KeyboardInterrupt:
        # handle what to do when Ctrl-C was pressed
        # servo.disable()
        # clck.stop()
        
if __name__ == "__main__":
    main(1.5)