'''import easygui
from xml.dom.minidom import parse

#r = easygui.fileopenbox()
#archivo = open(r,'r',encoding="utf8")
#print(archivo.read())
a = minidom.parse("datos.xml")
#archivo.close()

#if __name__ == '__main__':
#    print("main")'''

from xml.dom.minidom import parse 

doc = parse("datos.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))