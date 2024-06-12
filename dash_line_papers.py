from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # set the header:
    pdf.add_page()
    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)
    # set lines
    for y in range(20, 298, 10):
        pdf.dashed_line(x1=10, y1=y, x2=200, y2=y, dash_length=1, space_length=2) # x1 & y1 are starting coordinates of line, 2s: ending

    # set the footer
    pdf.ln(260) # x mm of break lines
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R",
             ln=1, border=0)

    # make additional pages without a header
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set lines
        for y in range(20, 298, 10):
            pdf.dashed_line(x1=10, y1=y, x2=200, y2=y, dash_length=1, space_length=2)

        # set the footer
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R",
                 ln=1, border=0)


pdf.output("output_dashed.pdf")
