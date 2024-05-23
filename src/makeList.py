import pyfbsdk
from pyfbsdk import*
from pyfbsdk_additions import*

# return List of all shapekey which will be used for user selection in UI

def ReturnList():
    OutputList = list()
    
    def ExamineAllObjects(model):
        if len(model.Children) > 0:
            for child in model.Children:
                if type(child) == pyfbsdk.FBModel:
                    geo = child.Geometry
                    for i in range(geo.ShapeGetCount()):
                        name = geo.ShapeGetName(i)
                        
                        if not name in OutputList:
                            OutputList.append(name)
                
                ExamineAllObjects(child)
    
    ExamineAllObjects(FBSystem().Scene.RootModel)        
    return OutputList