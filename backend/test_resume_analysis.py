from app.services.resume_parser import extract_text_from_pdf
from app.services.ai.gemini_provider import analyze_resume


pdf_path = "data/resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)

if not resume_text:
    raise ValueError("No text could be extracted from the resume.")

candidate = analyze_resume(resume_text)

print("\n========== CANDIDATE PROFILE ==========\n")

print("Name:", candidate.name)
print("Designation:", candidate.designation)
print("Emails:", candidate.emails)
print("Mobile:", candidate.mobile_no)
print("Location:", candidate.location)

print("\nSkills:")
for skill in candidate.skills:
    print(f"\n- {skill.name}")
    print("  Category:", skill.category)
    print("  Confidence:", skill.confidence)
    print("  Evidence:", skill.evidence)

print("\nExperience:")
for experience in candidate.experience:
    print(f"\n- {experience.role} @ {experience.company}")
    print("  Location:", experience.location)
    print("  Dates:", experience.start_date, "-", experience.end_date)
    print("  Description:", experience.description)

print("\nProjects:")
for project in candidate.projects:
    print(f"\n- {project.name}")
    print("  Technologies:", project.technologies)
    print("  Link:", project.link)

print("\nEducation:")
for education in candidate.education:
    print(f"\n- {education.degree} @ {education.institution}")
    print("  Field:", education.field)
    print("  Score:", education.score, education.score_type)
    print("  Year:", education.year)

print("\nAchievements:")
for achievement in candidate.achievements:
    print("-", achievement)
