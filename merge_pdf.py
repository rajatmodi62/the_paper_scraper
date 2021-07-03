from PyPDF2 import PdfFileMerger, PdfFileReader
import glob 

def merge_pdf():

    pdf_list = sorted(glob.glob('./pdf_artifacts/*.pdf'))
    
    mergedObject = PdfFileMerger()

    for pdf_path in pdf_list:
        mergedObject.append(PdfFileReader(pdf_path, 'rb'))

    mergedObject.write("mergedfilesoutput.pdf")
