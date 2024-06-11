from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # Headers:
    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21) # x1 & y1 are starting coordinates of line, 2s: ending

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R",
                 ln=1, border=0)


pdf.output("output.pdf")
