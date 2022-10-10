import fitz

result_report = fitz.open()

for pdf in ['1.pdf', '2.pdf', '3.pdf']:
    with fitz.open(pdf) as mfile:
        result_report.insert_pdf(mfile)
    
result_report.save("report.pdf")