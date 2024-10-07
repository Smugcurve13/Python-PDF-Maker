from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

print(type(pdf))

pdf.add_page()

pdf.set_font(family="Times",style="b", size=12)
pdf.cell(w=0,h=12, txt="hello there",align='L', ln=1,border=1)
pdf.cell(w=0,h=12, txt="hi there",align='L', ln=1,border=1)

pdf.output("output.pdf")