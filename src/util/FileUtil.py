from lxml import etree

def validateXML(filename):
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(filename, parser)
    if tree:
        print("Validated");
    else:
        print("Not Validated");

def generateXml(radius,length):
    root = etree.Element('TestResult')
    child_radius = etree.Element('radius')
    child_radius.text = radius
    root.append(child_radius)
    child = etree.Element('length')
    child.text = length
    root.append(child)
    s = etree.tostring(root, pretty_print=True)
    return s

def writeIntoFile(filename,mode,text):
    file = open(filename,mode)
    file.write(text)
    print file
    file.close()



# validateXML();
# print generateXml('10','15');
# writeIntoFile("xample1.xml","w",generateXml('10','15'));

validateXML("xample1.xml");