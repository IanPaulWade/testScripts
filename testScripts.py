import Metoc_Derivatives as md

Hs = 5.5
Tz = 12.3

Ss = md.steepness(Hs, Tz)
print('Significant Steepness = ' + f"{Ss:0.1f}")

newTz = md.t_from_hs(Hs, Ss)
print('Original Tz = ' + f"{Tz:0.2f}" + ' s : New Tz = ' + f"{newTz:0.2f}" + ' s')

newHs = md.h_from_ts(Tz, Ss)
print('Original Hs = ' + f"{Hs:0.2f}" + ' m : New Hs = ' + f"{newHs:0.2f}" + ' m')
