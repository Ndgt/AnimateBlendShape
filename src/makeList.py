from pyfbsdk import*
from pyfbsdk_additions import*

# return List of all shapekey which will be used for user selection in UI

def ReturnList(chara:FBCharacter):
    OutputList = FBModelList()
    chara.GetSkinModelList()
    