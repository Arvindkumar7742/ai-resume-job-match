from google import genai
from google.genai import types

from app.models.resume import CandidateProfile


client = genai.Client()


def analyze_resume(resume_text: str) -> CandidateProfile:
    prompt = f"""
You are a resume analysis system.

Analyze the resume below and extract a structured candidate profile.

Rules:
1. Extract information only from the resume.
2. Identify skills from the entire resume, not only the Technical Skills section.
3. Consider Skills, Experience, Projects, Education, Certifications,
   Coursework, and Achievements.
4. Do not invent information.
5. For every skill, provide evidence showing where the skill was found.
6. Return the result according to the provided schema.

Resume:
----------------
{resume_text}
----------------
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=CandidateProfile,
        ),
    )

    parsed = response.parsed

    if not isinstance(parsed, CandidateProfile):
        raise ValueError("Gemini returned an unexpected response format.")

    return parsed
