from guietta import Gui, R1, Quit, ___, _
import ChatCoderUtilities as util


def RunChatCodder(mainGui):
    gui = Gui(
        ["ChatCoderImg/Logo.png", ___, ___],
        ['Kill Proof Quantity (16-994):', "__Amount__", _],
        ['How many times to ping (random between lower and upper):', "__PingLower__", "__PingUpper__"],
        ['If you want to ping more than 250, they will be pinged separately. '
         'Fe: 350kp will be pinged in form of 250 and 100 separated. ', _, _],
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


    gui.Amount = "150"
    gui.PingLower = "2"
    gui.PingUpper = "4"
    gui.Inserted = "Or you can provide your own in game link here"

    gui.run()