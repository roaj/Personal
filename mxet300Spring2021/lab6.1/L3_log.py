import L2_log as log
import L2_vector as vec

import time

while(1):
    nearest = vec.getNearest()
    log.tmpFile(nearest[0], 'distance')
    log.tmpFile(nearest[1], 'angle')
    time.sleep(0.2) 