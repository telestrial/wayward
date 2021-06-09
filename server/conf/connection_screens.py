# -*- coding: utf-8 -*-
"""
Connection screen

This is the text to show the user when they first connect to the game (before
they log in).

To change the login screen in this module, do one of the following:

- Define a function `connection_screen()`, taking no arguments. This will be
  called first and must return the full string to act as the connection screen.
  This can be used to produce more dynamic screens.
- Alternatively, define a string variable in the outermost scope of this module
  with the connection string that should be displayed. If more than one such
  variable is given, Evennia will pick one of them at random.

The commands available to the user when the connection screen is shown
are defined in evennia.default_cmds.UnloggedinCmdSet. The parsing and display
of the screen is done by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

# CONNECTION_SCREEN = """
# |b==============================================================|n
#  Welcome to |g{}|n, version {}!

#  If you have an existing account, connect to it by typing:
#       |wconnect <username> <password>|n
#  If you need to create an account, type (without the <>'s):
#       |wcreate <username> <password>|n

#  Enter |whelp|n for more info. |wlook|n will re-show this screen.
# |b==============================================================|n""".format(
#     settings.SERVERNAME, utils.get_evennia_version("short")
# )

CONNECTION_SCREEN = """
|b================================================================================|n
                 ,                                                             ,
                @"===,                                                ,_____cctI
                "?AAAAAAAAAAAAAAAA,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;LLLLLLLLLL
      ~",,,      1''''''''''''###OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
       '"EEEEE, !'"***"~~~~~~"OOOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
          ,EEEEE)>"'''???????"WWW!MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
           "E.,)+="WWW~~~~~~#"OOO1OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        ,~:#")LLL!"+++???????"$$$1==========##/
         &LLLLLLLLL;;;;;;;;;;;;,,,/
         1#LLLLLLLLLLLLLLLLLLLLLL!
       ,!###LLLLLL"'EEEE,'"LLLLL!
       !######LLL"  "EEE"  "LLLL"
      !#########L!   "EEJ. "LL!
     !##########1      "JJ*,l"
    !############"!       ,l"
    1##########"  1"~~,~~"  __      __                                      .___
   !##########"            /  \    /  \____  ___.____  _  ______ _______  __| _/
  !###########!            \   \/\/   \__  \<   |  \ \/ \/ \__  \\_  __ \/ __ | 
  !###########1             \        / / __ \\___  |\     / / __ \|  | \/ /_/ | 
 !############!              \__/\  / (____  / ____| \/\_/ (____  |__|  \____ | 
 1#############                   \/       \/\/                 \/           \/ 
!"#############"
!##############!                                  Written by Telestrial
1##########"'
1#####"'
|b================================================================================|n""".format(
    settings.SERVERNAME, utils.get_evennia_version("short")
)
# CONNECTION_SCREEN = """
# |b================================================================================|n
#                  ,                                                             ,
#                 @"===,                                                ,_____cctI
#                 "?AAAAAAAAAAAAAAAA,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;LLLLLLLLLL
#       ~",,,      1''''''''''''###OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#        '"EEEEE, !'"***"~~~~~~"OOOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
#           ,EEEEE)>"'''???????"WWW!MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#            "E.,)+="WWW~~~~~~#"OOO1OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#         ,~:#")LLL!"+++???????"$$$1==========##/
#          &LLLLLLLLL;;;;;;;;;;;;,,,/
#          1#LLLLLLLLLLLLLLLLLLLLLL!
#        ,!###LLLLLL"'EEEE,'"LLLLL!
#        !######LLL"  "EEE"  "LLLL"
#       !#########L!   "EEJ. "LL!
#      !##########1      "JJ*,l"
#     !############"!       ,l"
#     1##########"  1"~~,~~"  __      __                                      .___
#    !##########"            /  \    /  \____  ___.____  _  ______ _______  __| _/
#   !###########!            \   \/\/   \__  \<   |  \ \/ \/ \__  \\_  __ \/ __ | 
#   !###########1             \        / / __ \\___  |\     / / __ \|  | \/ /_/ | 
#  !############!              \__/\  / (____  / ____| \/\_/ (____  |__|  \____ | 
#  1#############                   \/       \/\/                 \/           \/ 
# !"#############"
# !##############!                                  Written by Telestrial
# 1##########"'
# 1#####"'
# |b================================================================================|n""".format(
#     settings.SERVERNAME, utils.get_evennia_version("short")
# )
