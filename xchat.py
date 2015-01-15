__module_name__ = "memer.py"
__module_version__ = "1.0"
__module_description__ = "Memetext like a pro"

import xchat

def handle_outgoing(w, we, userdata):
        if(we[0][0:1] == ">"):
                xchat.command("say \003" + "3" + we[0])
                return xchat.EAT_ALL

xchat.hook_command("", handle_outgoing)