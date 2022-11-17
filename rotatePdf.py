import PyPDF2

def rotate(fileName,degree,number):

    pdf_in = open(fileName, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    print(pdf_in)
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum ==number-1:
            page.rotateClockwise(degree)
        pdf_writer.addPage(page)

    pdf_out = open('tmp/test.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return 'tmp/test.pdf'

