import os
import nuke


def saveFrame(filePath = ""):
    viewer = nuke.activeViewer()
    inputNode = nuke.ViewerWindow.activeInput(viewer)
    viewNode = nuke.activeViewer().node()

    if inputNode != None:
        selInput = nuke.Node.input(viewNode, inputNode)

        if filePath = "":
            filePath = nuke.getFilename('Save File', "*.png *.jpg *.tga *.exr *.dpx", type = 'save')
        


        if filePath != None:

            #Check Path
            path, ext = os.path.split(filePath)
            if not os.path.isdir(path):
                pass
                ### TODO: Build Path            


            write = nuke.nodes.Write(file = filePath, name = 'WriteSaveThisFrame', file_type=ext)
            write.setInput(0,selInput)
            curFrame = int(nuke.knob("frame"))
            nuke.execute(write.name(), curFrame, curFrame)
            nuke.delete(write)

    else:
        nuke.message("This viewer don't have any input connected!")

def getSeqName():
    res = ""    
    scriptpath = str.split(nuke.root().knob('name').value() , "/")    
    res = scriptpath[len(scriptpath)-3]
    return res


def getNextRefFrame():
    ret = "rf01"


def getRefFramePath():
    res = ""

    res = " /Users/jonas/Desktop/test1.ext"

    return res



def saveRefFrame():
    refPath = getRefFramePath()
    seqName = getSeqName()

    saveFrame(os.path.join(getRefFramePath(), getSeqName(), getSeqName() + "_" + getNextRefFrame() + ".exr" ))
