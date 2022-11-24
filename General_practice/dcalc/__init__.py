import sys
import os
sys.path.append(os.path.dirname(__file__))

from .deg_to_gms import *
from .deg_to_rad import *
from .gms_to_deg import *
from .rad_to_deg import *

print(deg_to_gms(39.97))
print(gms_to_deg(39, 58, 12))
print(deg_to_rad(39.97))
print(rad_to_deg(deg_to_rad(39.97)))
