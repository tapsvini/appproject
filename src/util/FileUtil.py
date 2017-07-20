from lxml import etree


class FileUtility:
    #Function to validate generated Xml with dtd
    '''
    INPUT

    filename=filename(which should be xml) which is required to be validated

    '''
    def validateXML(self,filename):
        parser = etree.XMLParser(dtd_validation=True);
        tree = etree.parse(filename, parser);
        if tree:
            print("Validated");
        else:
            print("Not Validated");

    # Function to generate XML
    '''
    INPUT
    
    radius=Radis which is taken as input from user
    length=which is output after doing calculation
    
    '''
    def generateXml(self,radius,length):
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
    '''
    INPUT
    
    filename=Filename where results should be saved
    mode=valid values w,a. whether to create new file or append the result in previous file.
    text= text which needs to be write into the filename
    '''
    def writeIntoFile(self,filename,mode,text):
        file = open(filename,mode);
        file.write(text);
        print (file);
        file.close();
