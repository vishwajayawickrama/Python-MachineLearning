import xml.etree.ElementTree as ET

tree = ET.parse('vehicles.xml')

root = tree.getroot()

# root = ET.fromstring(vehicle_xml_data_as_string)

print(root.tag)
print(root.attrib)

for child in root:
    print(root.tag, root.attrib)
    
#searching

for element in root.iter(tags='registration_no'):
    print(element.text)
    
for element in root.findall('vehicle'):
    reg = element.find('registration_no').text
    make = element.find('make').text
    print(reg, make)
    

# Modifine

for element in root.iter(tag='make'):
    newmake = 'Nissan'
    element.text = 'Nissan'
    
tree.write('output.xml')

data = ET.Element('chess')
 
# Adding a subtag named `Opening`
# inside our root tag
element1 = ET.SubElement(data, 'Opening')
 
# Adding subtags under the `Opening`
# subtag
s_elem1 = ET.SubElement(element1, 'E4')
s_elem2 = ET.SubElement(element1, 'D4')