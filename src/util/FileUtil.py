from lxml import etree

#Function to validate generated Xml with dtd
def validateXML(filename):
    parser = etree.XMLParser(dtd_validation=True);
    tree = etree.parse(filename, parser);
    if tree:
        print("Validated");
    else:
        print("Not Validated");

# Function to generate XML
def generateXml(radius,length):
    root = etree.Element('TestResult');
    child_radius = etree.Element('radius');
    child_radius.text = radius;
    root.append(child_radius);
    child = etree.Element('length');
    child.text = length;
    root.append(child);
    s = etree.tostring(root, pretty_print=True);
    return s

# Method to write text into given file name
def writeIntoFile(filename,mode,text):
    file = open(filename,mode);
    file.write(text);
    print (file);
    file.close();
