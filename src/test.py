from pyfbsdk import*
from pyfbsdk_additions import*

Editor = FBFCurveEditor()

def PopulateLayout(mainLyt):
    #create Spread

    
    x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
    y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
    w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
    h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
    
    face = FBFindModelByLabelName("Face")

    for prop in face.PropertyList:
        if prop.Name == "a":
            pCurve = prop.GetAnimationNode().FCurve
            pNode = prop.GetAnimationNode()

    mainLyt.AddRegion("FCurveEditor","testEditor", x, y, w, h)
    mainLyt.SetControl("FCurveEditor",Editor)
    Editor.AddAnimationNode(pNode)

def CreateTool():    
    # Tool creation will serve as the hub for all other controls
    t = FBCreateUniqueTool("FCurve editor sample")

    t.StartSizeX = 300
    t.StartSizeY = 300

    PopulateLayout(t)
    ShowTool(t)


CreateTool()


face = FBFindModelByLabelName("Face")

global b 

for prop in face.PropertyList:
    if prop.Name == "a":
        b = prop

for prop in Editor.PropertyList:
    print(prop.Name)

Editor.AddProperty(b)