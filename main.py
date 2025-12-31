from fpdf import  FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format = 'A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    # Set the header
    pdf.set_font('Times', 'B', size=24)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=0, h=12, text=row["Topic"],align='L')
    #pdf.line(10,21,200,21)
    for y  in range(20,298,10):
        pdf.line(10, y, 200, y)

    pdf.ln(275)
    # Set the footer
    pdf.set_font('Times', 'I', size=8)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=0, h=12, text=row["Topic"], align='R')

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(275)
        # Set the footer
        pdf.set_font('Times', 'I', size=8)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(w=0, h=12, text=row["Topic"], align='R')
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")