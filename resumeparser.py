import spacy
from spacy.matcher import Matcher
import re

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def extract_entities(doc):
    """
    Extract entities like name, email, and phone number from the document.
    """
    matcher = Matcher(nlp.vocab)

    # Define patterns for name, email, and phone number
    name_pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
    email_pattern = [{"LIKE_EMAIL": True}]
    phone_pattern = [{"TEXT": {"REGEX": r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'}}]

    matcher.add("NAME", [name_pattern])
    matcher.add("EMAIL", [email_pattern])
    matcher.add("PHONE", [phone_pattern])

    matches = matcher(doc)

    entities = {}
    for match_id, start, end in matches:
        entity = doc[start:end]
        entities[match_id] = entity.text

    return entities

def parse_resume(file_path):
    with open('resume.txt', 'r',encoding=None) as file:
        content = file.read()

    # Preprocess the content (remove extra whitespaces, newlines, etc.)
    content = re.sub(r'\s+', ' ', content)

    # Parse the document using SpaCy
    doc = nlp(content)

    # Extract entities
    entities = extract_entities(doc)

    # Extract other common resume sections (e.g., education, experience, skills)
    education = extract_education(doc)
    experience = extract_experience(doc)
    skills = extract_skills(doc)

    return {
        'entities': entities,
        'education': education,
        'experience': experience,
        'skills': skills
    }

def extract_education(doc):
    # Add logic to extract education details from the document
    # This could involve searching for patterns like degree names, universities, graduation years, etc.
    return []

def extract_experience(doc):
    # Add logic to extract work experience details from the document
    # This could involve searching for patterns like job titles, company names, dates, etc.
    return []

def extract_skills(doc):
    # Add logic to extract skills from the document
    # This could involve identifying keywords or phrases related to skills
    return []

if _name_ == "_main_":
    file_path = input("Enter the path to the resume file: ")
    resume_data = parse_resume(file_path)
    print("\nResume Data:")
    print("Entities:")
    for entity_type, entity_text in resume_data['entities'].items():
        print(f"{entity_type.capitalize()}: {entity_text}")
    print("\nEducation:")
    for item in resume_data['education']:
        print(item)
    print("\nExperience:")
    for item in resume_data['experience']:
        print(item)
    print("\nSkills:")
    print(", ".join(resume_data['skills']))