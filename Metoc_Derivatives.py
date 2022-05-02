# Metocean variable derivatives module
# Ian P Wade (May 2022)

import math

# constants
g = 9.81
pi = 3.142


# wave steepness, given height and period
def steepness(h, t):
    s = (g * pow(t, 2)) / (2 * pi * h)
    return s


# wave period, given height and steepness
def t_from_hs(h, s):
    t = math.sqrt((2 * pi * h * s) / g)
    return t


# wave height, given period and steepness
def h_from_ts(t, s):
    h = ((g * pow(t, 2)) / (2 * pi * s))
    return h
