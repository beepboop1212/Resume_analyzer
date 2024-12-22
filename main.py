import os
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from docx import Document

from dotenv import load_dotenv

load_dotenv()  # Load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from a PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Function to extract text from a Word file
def input_word_text(uploaded_file):
    doc = Document(uploaded_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Prompt Template
input_prompt = """
Your task is to evaluate resumes against a given job description.
The jobs or internships are in the roles of Data analyst, Data scientist, ML engineer, AI engineer, LLM engineer. 
Base your evaluation only on the information provided in the resume and job description. Do not assume or fabricate details like years of experience, education, or skills.

Do not provide any additional information such as examples.

Assess the resume thoroughly and only provide the following details:
1. Percentage Match between the resume and the job description.
2. Identify keywords or phrases explicitly mentioned in the job description that are missing from the resume text. These should be skills, tools, or qualifications relevant to the job.
3. A concise profile summary of the given resume, relevant to the job description.


The output should contain only the following:
---------------------
Evaluation Results:
---------------------
Job Description Match: XX%
Missing Keywords: [Keyword1, Keyword2, ...]
Profile Summary: 
"Headline: Your concise headline here.
- Key skill 1
- Key skill 2
- Key skill 3
"
---------------------
"""


# Streamlit app
st.title("JD Matcher")
st.text("Refine your Resume")
jd = st.text_area("Paste Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Please upload a PDF or Word file")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Check the file type
        if uploaded_file.name.endswith(".pdf"):
            text = input_pdf_text(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            text = input_word_text(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF or Word document.")
            text = None

        if text:
            # Format the input prompt with resume text and job description
            formatted_prompt = input_prompt.format(text=text, jd=jd)
            response = get_gemini_response(formatted_prompt)
            st.subheader("Evaluation Results")
            st.text(response)
    else:
        st.error("Please upload your resume file.")
