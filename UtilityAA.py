#    This file is part of EQMBox_CCC.

#    EQMBox_CCC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    EQMBox_CCC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with EQMBox_CCC.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import time

from Targeting import *

# class for utility AA activation 
class UtilityAA:

    def __init__(self):
        print("DEBUG: Initializing Utility AA Class")

    # invis requesting party member (must be WHITELISTED in Config.py)
    def mageGroupInvisAA(line):
       print("DEBUG: "+line)
       # get character name from groupsay "soandso tells the group"
       subprocess.call(["xdotool", "type", "/alt activate 1210"])
       subprocess.call(["xdotool", "key", "Return"])

    def mageCoHAA(line):
       print("DEBUG: "+line)
       # get character name from groupsay "soandso tells the group"
       TARGET = Targeting.requested(line)
       time.sleep(1)
       subprocess.call(["xdotool", "type", "/target ", TARGET])
       subprocess.call(["xdotool", "key", "Return"])
       time.sleep(1)
       subprocess.call(["xdotool", "type", "/alt activate 7050"])
       subprocess.call(["xdotool", "key", "Return"])

    # TODO: Add some utility AA's. Ie. Banker, Merchant, Lesson, etc... 

# End of Class
