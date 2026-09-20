# AI Resume & Job Match Platform

An AI-powered job discovery and resume optimization platform.

## Goal

The platform helps users:

1. Analyze their resume and extract relevant skills, experience,
   projects, education, etc.
2. Improve their resume based on their career profile and target jobs.
3. Discover relevant jobs from multiple job platforms.
4. Match resumes against job descriptions.
5. Get explainable recommendations and improvement suggestions.

## Architecture

React Native
↓
Python / FastAPI
↓
AI Service
↓
Gemini / OpenAI / AWS Bedrock

Backend
↓
PostgreSQL
S3
Job ingestion workers

## Technology Stack

### Frontend

- React Native

### Backend

- Python
- FastAPI

### AI

- Gemini
- OpenAI
- AWS Bedrock

### AWS

- S3
- PostgreSQL/RDS
- ECS
- ECR
- SQS
- CodePipeline
- CodeBuild

## Documentation

- [Product Requirements](docs/01-product-requirements.md)
- [System Architecture](docs/02-system-architecture.md)
- [API Specification](docs/03-api-specification.md)
- [Data Model](docs/04-data-model.md)
- [AI Design](docs/05-ai-design.md)
- [Job Source Integration](docs/06-job-source-integration.md)
- [Security & Privacy](docs/07-security-and-privacy.md)
- [AWS & CI/CD](docs/08-aws-and-cicd.md)

## Current Status

Phase 1 - AI resume analysis
