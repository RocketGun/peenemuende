import os
import nuke


def saveFrame(filePath = ""):
    viewer = nuke.activeViewer()
    inputNode = nuke.ViewerWindow.activeInput(viewer)
    viewNode = nuke.activeViewer().node()

    if inputNode != None:
        selInput = nuke.Node.input(viewNode, inputNode)

        if filePath == "":
            filePath = nuke.getFilename('Save File', "*.png *.jpg *.tga *.exr *.dpx", type = 'save')
        
        filePath = os.path.normpath(filePath)

        if filePath != None:

            #Check Path
            path, ext = os.path.split(filePath)
            if not os.path.isdir(path):
                os.makedirs(path)          


            write = nuke.nodes.Write(file = filePath, name = 'WriteSaveThisFrame', file_type=ext)
            write.setInput(0,selInput)
            curFrame = int(nuke.knob("frame"))
            nuke.execute(write.name(), curFrame, curFrame)
            nuke.delete(write)
            print "saved: " + filePath

    else:
        nuke.message("This viewer don't have any input connected!")

def getSeqName():
    res = ""    
    scriptpath = str.split(nuke.root().knob('name').value() , "/")    
    res = scriptpath[len(scriptpath)-3]
    return res


def getNextRefFrame():
    return "rf01"
    


def getSeqRefFramePath():
    res = ""

    res = os.path.join("O:/projects/130226_pin_film/production/comp/nuke/output/", getSeqName(), "_seqRefs")

    return res



def saveRefFrame():
    refPath = getSeqRefFramePath()
    seqName = getSeqName()
    nextRefFrame = getNextRefFrame()


    saveFrame(os.path.join(refPath, seqName + "_" + nextRefFrame + ".exr" ))
    
    
    
saveRefFrame()
