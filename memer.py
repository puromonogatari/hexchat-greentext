__module_name__ = "memer.py"
__module_version__ = "1.0"
__module_description__ = "Memetext like a pro"

import hexchat

def handle_outgoing(w, we, userdata):
        if(we[0][0:1] == ">"):
                hexchat.command("say \003" + "3" + we[0])
                return hexchat.EAT_ALL

hexchat.hook_command("", handle_outgoing)
