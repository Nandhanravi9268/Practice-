c:\Users\HP\OneDrive\文档\student_data.csv
import pandas as pd
from fpdf import FPDF

# Read the CSV file
df = pd.read_csv("student_data.csv")

# Basic Analysis
total_students = len(df)
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

# PDF Report Generation
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "CodTech Internship - Task 2 Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Students: {total_students}", ln=True)
pdf.cell(200, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(200, 10, f"Lowest Marks: {lowest_marks}", ln=True)
pdf.ln(10)

# Add table of student data
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", border=1)
pdf.cell(60, 10, "Department", border=1)
pdf.cell(60, 10, "Marks", border=1)
pdf.ln()

pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(60, 10, row["Name"], border=1)
    pdf.cell(60, 10, row["Department"], border=1)
    pdf.cell(60, 10, str(row["Marks"]), border=1)
    pdf.ln()

# Save the PDF
pdf.output("student_report.pdf")
print("PDF Report Generated Successfully!")
