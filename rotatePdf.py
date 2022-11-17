import PyPDF2

def rotate(filePath,degree,pageNumber):

    pdf_in = open(filePath, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    print(pdf_in)
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum == pageNumber-1:
            page.rotateClockwise(degree)
        pdf_writer.addPage(page)

    filename = filePath.split("/")[-1]
    path = "tmp/test_"+ filename
    pdf_out = open(path, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return path

