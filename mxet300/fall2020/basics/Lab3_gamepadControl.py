# this file will let you use your gamepad to drive the SCUTTLE robot

import time
import L2_speed_control as sc
import L2_inverse_kinematics as inv


def manual_nav():
	c = inv.getPdTargets()			
	sc.driveOpenLoop(c)


if __name__ == "__main__":
	while 1:
		manual_nav()
		time.sleep(0.02)
