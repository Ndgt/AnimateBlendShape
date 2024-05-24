#coding: shift-jis

from pyfbsdk import FBMessageBox
import sys
sys.path.append("..//..//..//AppData//Local//Programs//Python//Python311//Lib//site-packages")

# function to read txt file
def ReadLyrics(filename):
    f = open(filename, "r")
    data = f.readlines()
    return_string = ""

    for add_txt in data:
        if not add_txt == "\n":
            return_string += "\n" + add_txt

    return return_string


# function to convert QTextEdit strings 
# option: hiragana / alphabet
def ConvertLyrics(editortext, option):
    try:
        from pykakasi import kakasi
        kks = kakasi()
        return_hiragana_string = ""
        return_alphabet_string = ""

        data = editortext.replace(" ","").replace("？","").replace("！","").split()
        for words in data:
            if not words == "\n":
                # convert method of pykakasi module
                result = kks.convert(words)
                for i in range(len(result)):
                    return_hiragana_string += result[i]["hira"]
                    return_alphabet_string += result[i]["hepburn"]
                # add new line 
                return_hiragana_string += "\n"
                return_alphabet_string += "\n"

        # return results
        if option == "hiragana":
            return return_hiragana_string
        if option == "alphabet":
            return return_alphabet_string


    except ImportError as err:
        FBMessageBox("Caution", "Error : modue \"pykakasi\" is not installed \n Run \"pip install pykakasi\" in the Terminal.", "OK")
        return err