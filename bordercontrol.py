# bordercontrol.py

def border_control(playerC1, playerC3, screenW, screenH):
    allowA = allowW = allowD = allowS = True
    
    if playerC1.x == 0:
        allowA = False
    if playerC1.y == 0:
        allowW = False
    if playerC3.x == screenW:
        allowD = False
    if playerC3.y == screenH:
        allowS = False
    
    return allowA, allowW, allowD, allowS
