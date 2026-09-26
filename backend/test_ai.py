from app.services.ai.gemini_provider import analyze_resume


sample_resume = """
Arvind Kumar
+917742963339
Software Developer

Skills:
React Native, React, JavaScript, TypeScript, Node.js, Express.js

Experience:
Software Developer at Avis Budget Group.
Worked on a React Native global car rental application.
Used Firebase Analytics.

Projects:
Built a Spotify clone using React Native and Redux.
Implemented OAuth 2.0 and Web APIs.
"""


result = analyze_resume(sample_resume)

print(result)
print()
print("Name:", result.name)
print("Designation:", result.designation)
print("Skills:")

for skill in result.skills:
    print("-", skill.name)
    print("  Evidence:", skill.evidence)
    print("  Confidence:", skill.confidence)
