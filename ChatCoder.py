from guietta import Gui, R2, _, Quit, ___
import ChatCoderUtilities as util

gui = Gui(
    ["img/Logo.png", ___, ___],
    ['Kill Proof Quantity:', "__Amount__", _],
    ['How many times to ping:', "__Ping__", _],
    [R2("Dhuum"), _ , "img/Dhuum's_Token.png"],
    [R2("Quadim v1"), _ , "img/Qadim's_Token.png"],
    [R2("Quadim v2"), _ , "img/Ether_Djinn's_Token.png"],
    [R2("Unstable Cosmic Essence"), _ , "img/UCE.png"],
    [R2("Legendary Insight"), _, "img/LI.png"],
    [R2("Your Own"), "__Inserted__", ___],
    [["Press to activate"], ___, ___]
)

gui.Presstoactivate = util.send_kp

with gui.Dhuum, gui.Quadimv1, gui.Quadimv2, gui.UnstableCosmicEssence:
    print("Rad button changed")
    if gui.Dhuum.isChecked():
        util.chat_code = util.dhuum_chat_code
    if gui.Quadimv1.isChecked():
        util.chat_code = util.quadim_v1_chat_code
    if gui.Quadimv2.isChecked():
        util.chat_code = util.quadim_v2_chat_code
    if gui.UnstableCosmicEssence.isChecked():
        util.chat_code = util.unstable_cosmic_essence_chat_code
    if gui.LegendaryInsight.isChecked():
        util.chat_code = util.legendary_insight_chat_code
    if gui.YourOwn.isChecked():
        util.chat_code = gui.Inserted



gui.Amount = "150"
gui.Ping = "4"
gui.Inserted = "Or you can provide your own in game link here"

gui.run()