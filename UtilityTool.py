from guietta import Gui, _, ___,  Quit
from ChatCoder import RunChatCodder
from AutoJoiner import RunAutoJoiner
from CloverMaker import RunCloverMaker
from GroupCreator import RunGroupCreator

gui = Gui(
    ["GW2 Utility Tool by Magomir", _, _],
    ["Start ChatCoder", ["ChatCoder"], _],
    ["Start AutoJoiner", ["AutoJoiner"], _],
    ["Start CloverMaker", ["CloverMaker"], _],
    ["Start GroupCreator", ["GroupCreator"], _],
    [Quit, ___, ___],
)

gui.ChatCoder = RunChatCodder
gui.AutoJoiner = RunAutoJoiner
gui.CloverMaker = RunCloverMaker
gui.GroupCreator = RunGroupCreator

gui.run()