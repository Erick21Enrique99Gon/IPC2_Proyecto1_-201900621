import easygui

r = easygui.fileopenbox()
archivo = open(r,'r',encoding="utf8")
print(archivo.read())
archivo.close()