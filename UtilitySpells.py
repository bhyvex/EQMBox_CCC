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

# classes
from Config import *
from Targeting import *

# class for triggering utility spells 
# NOTE: BIND, INVIS, ITU, SOW, CRACK, etc.. 
#	must be defined in Config.py

class UtilitySpells:

    def __init__(self):
        print("DEBUG: Initializing UtilitySpells Class")

    # bind requesting party member (must be WHITELISTED in Config.py)
    def bindMe(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", BIND])
        subprocess.call(["xdotool", "key", "Return"])

    # invis requesting party member (must be WHITELISTED in Config.py)
    def invisMe(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", INVIS])
        subprocess.call(["xdotool", "key", "Return"])

    # itu requesting party member (must be WHITELISTED in Config.py)
    def ituMe(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", ITU])
        subprocess.call(["xdotool", "key", "Return"])

    # sow requesting party member (must be WHITELISTED in Config.py)
    def sowMe(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", SOW])
        subprocess.call(["xdotool", "key", "Return"])

    # crack (clarity line) requesting party member (must be WHITELISTED in Config.py)
    def crackMe(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", CRACK])
        subprocess.call(["xdotool", "key", "Return"])

# End of Class
