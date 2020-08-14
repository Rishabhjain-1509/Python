# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:05:44 2020

@author: Rishabh Jain
"""

import JPype1

class PdfToExcel:

    def __init__(self, dataDir):
        print( "init func")
        self.dataDir = dataDir
        self.Document = JPype1.JClass("com.aspose.pdf.Document")
        self.ExcelSaveOptions=JPype1.JClass("com.aspose.pdf.ExcelSaveOptions")

    def main(self):

         # Open the target document
        doc=self.Document()
        pdf = self.Document()
        pdf = self.dataDir +'input1.pdf'

        # Instantiate ExcelSave Option object
        excelsave=self.ExcelSaveOptions();

        # Save the output to XLS format
        doc.save(self.dataDir + "Converted_Excel.xls", excelsave);

        print ("Document has been converted successfully")
