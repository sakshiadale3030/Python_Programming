# Duck Typing : It is concept where the type of a object is determined 
# by its behaviour, not by its class

class InkjectPrinter:
    def printdocument(self, document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self, document):
        print("Laser printer printing : ",document)

class PDFWriter:
    def printdocument(self, document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marvellous notes")

def main():
    StartPrinting(InkjectPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()    
