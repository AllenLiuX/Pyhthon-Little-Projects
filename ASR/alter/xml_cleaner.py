import xml.dom.minidom as XmlDocument
import sys
import os
import re
import xml.etree.ElementTree as ET

def change_all_xml(xml_path):
    filelist = os.listdir(xml_path)
    print(filelist)
    for xmlfile in filelist:
        doc = ET.parse(xml_path+xmlfile)
        root = doc.getroot()
        print(root)
        Roles = root.find('Speech').find('Subject').findall('Role')
        for r in Roles:
            Items = r.find('EndPoint').findall('Item')
            for i in Items:
                text = i.find('Text').text
                print(text)
                text = re.sub(r'[-_][0-9]+', '', text)
                i.find('Text').text = text
                print(text)
        doc.write(xml_path, encoding='utf-8')


def change_one_xml(xml_path):
    doc = ET.parse(xml_path)
    root = doc.getroot()
    print(root)
    Roles = root.find('Speech').find('Subject').findall('Role')
    for r in Roles:
        Items = r.find('EndPoint').findall('Item')
        for i in Items:
            text = i.find('Text').text
            print(text)
            text = re.sub(r'[-_][0-9]+', '', text)
            i.find('Text').text = text
            print(text)
    doc.write(xml_path, encoding='utf-8')


inp = sys.argv[1]
change_one_xml(inp)



# doc = XmlDocument.parse(inp)
# RR = doc.getElementsByTagName('RecognizeResult')
# Speech = RR[0].getElementsByTagName('Speech')
# Subject = Speech[0].getElementsByTagName('Subject')
# Role = Subject[0].getElementsByTagName('Role')
# for i in Role:
#     Endpoint1 = Role[i].getElementsByTagName('Endpoint')
# print(Subject)
# for i in texts:
#     print(i.data)
