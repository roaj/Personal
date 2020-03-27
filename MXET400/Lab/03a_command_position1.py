#!/usr/bin/env python3

import hebi
from math import pi, sin
from time import sleep, time

lookup = hebi.Lookup()

# Wait 2 seconds for the module list to populate
sleep(2.0)

family_name = "Arm2"
module_name = "Team3"

group = lookup.get_group_from_names([family_name], [module_name])

if group is None:
  print('Group not found! Check that the family and name of a module on the network')
  print('matches what is given in the source file.')
  exit(1)

group_command  = hebi.GroupCommand(group.size)
group_feedback = hebi.GroupFeedback(group.size)

# Start logging in the background
group.start_log('logs', mkdirs=True)

freq_hz = .25                # [Hz]
freq = freq_hz * 2.0 * pi  # [rad / sec]
amp     = pi * 0.10           # [rad]

amp = 3.14

duration = 10.0               # [sec]
start = time()
t = time() - start
i = 0

while t < duration:
  # Even though we don't use the feedback, getting feedback conveniently
  # limits the loop rate to the feedback frequency
  group.get_next_feedback(reuse_fbk=group_feedback)

  ## get position feedback once
  if i == 0:
    positions = group_feedback.position
    print(f'Position Feedback:\n{positions}')
    i = 1


  t = time() - start

  #group_command.position = amp * sin(freq * t)
  #group_command.position = .1*t
  #group.send_command(group_command)

# Stop logging. `log_file` contains the contents of the file
log_file = group.stop_log()
hebi.util.plot_logs(log_file, 'position')