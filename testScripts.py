# training for user defined modules
# Ian P Wade (May 2022)

import Metoc_Derivatives as md

# data input
Hs = 5.5
Tz = 12.3

# derive significant wave steepness
Ss = md.steepness(Hs, Tz)
print('Significant Steepness = ' + f"{Ss:0.1f}")

# calculate Tz from Hs and Ss
newTz = md.period_from_hs(Hs, Ss)
print('Original Tz = ' + f"{Tz:0.2f}" + ' s : New Tz = ' + f"{newTz:0.2f}" + ' s')

# calculate Hs from Tz and Ss
newHs = md.height_from_ts(Tz, Ss)
print('Original Hs = ' + f"{Hs:0.2f}" + ' m : New Hs = ' + f"{newHs:0.2f}" + ' m')
