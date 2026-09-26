from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str
    category: str
    evidence: list[str] = Field(default_factory=list)
    confidence: float | None = Field(default=None, ge=0, le=1)


class Experience(BaseModel):
    company: str
    role: str
    location: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: str


class Project(BaseModel):
    name: str
    description: str
    link: str | None = None
    technologies: list[str] = Field(default_factory=list)


class Education(BaseModel):
    institution: str
    degree: str
    field: str | None = None
    board_or_university: str | None = None
    score: float | None = None
    score_type: str | None = None
    year: str | None = None


class CandidateProfile(BaseModel):
    name: str | None = None
    designation: str | None = None
    emails: list[str] = Field(default_factory=list)
    mobile_no: str | None = None
    location: str | None = None

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None

    summary: str | None = None

    skills: list[Skill] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)
    coursework: list[str] = Field(default_factory=list)
    achievements: list[str] = Field(default_factory=list)
    domains: list[str] = Field(default_factory=list)
    key_strengths: list[str] = Field(default_factory=list)
