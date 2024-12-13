from objects import Obj
from mirror import Mirror
from lights import Lights
from game import surface


def resetbutton(objects):
    objects.clear()
    return 

def addMirror(objects):
    newMirror = Mirror(360, 360, 50, surface)
    objects.append(newMirror)
    return

def addLight(objects):
    newLight = Lights(360, 360, (0, 0, 0), 500)
    objects.append(newLight)
    return 

def addObject(objects):
    newObj = Obj((110, 220, 110), 50, (360, 360), 360, 360)
    objects.append(newObj)
    return



