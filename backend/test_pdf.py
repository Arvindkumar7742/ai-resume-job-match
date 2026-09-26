from app.services.resume_parser import extract_text_from_pdf

pdf_path = "data/resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)

print("Characters extracted:", len(resume_text))
print()
print(resume_text)
