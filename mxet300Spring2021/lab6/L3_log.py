import L2_log as log
import L2_vector as vec

import time

while(1):
    nearest = vec.getNearest()
    log.tmpFile(nearest[0], 'distance')
    log.tmpFile(nearest[1], 'angle')
    
    nearestxy = vec.polar2cart(nearest[0],nearest[1])
    log.tmpFile(nearestxy[0], 'x')
    log.tmpFile(nearestxy[1], 'y')
    
    time.sleep(0.2) 