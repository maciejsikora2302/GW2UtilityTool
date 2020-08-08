from guietta import Gui, R1, Quit, ___, _
import ChatCoderUtilities as util


def RunChatCodder(mainGui):
    gui = Gui(
        ["ChatCoderImg/Logo.png", ___, ___],
        ['Kill Proof Quantity:', "__Amount__", _],
        ['How many times to ping:', "__Ping__", _],
        ['Then optional how much and how many times you want to ping extra', "__Amount2__", "__Ping2__"],
        [R1("Dhuum"), _ , "ChatCoderImg/Dhuum's_Token.png"],
        [R1("Quadim v1"), _ , "ChatCoderImg/Qadim's_Token.png"],
        [R1("Quadim v2"), _ , "ChatCoderImg/Ether_Djinn's_Token.png"],
        [R1("Unstable Cosmic Essence"), _ , "ChatCoderImg/UCE.png"],
        [R1("Legendary Insight"), _, "ChatCoderImg/LI.png"],
        [R1("Your Own"), "__Inserted__", ___],
        [["Press to activate"], ___, ___],
        [Quit, ___, ___]
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
    gui.Amount2 = "0"
    gui.Ping2 = "0"
    gui.Inserted = "Or you can provide your own in game link here"

    gui.run()