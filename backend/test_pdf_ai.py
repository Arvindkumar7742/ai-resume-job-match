from app.services.resume_parser import extract_text_from_pdf
from app.services.ai.gemini_provider import analyze_resume
pdf_path = "data/resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)

result = analyze_resume(resume_text)

# print(result)
# print()
print("Name:", result.name)
print("Designation:", result.designation)
print("Skills:", result.skills)
print("mobile_no", result.mobile_no)

# for skill in result.skills:
#     print("-", skill.name)
#     print("  Evidence:", skill.evidence)
#     print("  Confidence:", skill.confidence)
