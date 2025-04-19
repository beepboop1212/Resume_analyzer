Still needs a lot of improvement, as it keeps on deviating and not providing exact and specific responses. Hallucinating is a big issue. _just AI things..._



# 📄 JD Matcher – Resume & Job Description Evaluator (Gemini AI)

This project is a **Streamlit-based web application** that helps users evaluate how well their resume matches a given **job description (JD)** using **Google Gemini AI**. It's ideal for roles in **Data Science, Machine Learning, and AI Engineering** fields.

---

## 🔍 Features

- 🧠 **AI-Powered Resume Evaluation**:
  - Uses Google's **Gemini 1.5 Pro** to analyze and match resumes to job descriptions.
- 📈 **Match Score**:
  - Calculates a percentage match based on skills, tools, and qualifications.
- 🧩 **Keyword Gap Analysis**:
  - Identifies missing skills or keywords from the resume based on the job description.
- 🧾 **Profile Summary Generator**:
  - Produces a concise, job-specific profile summary from the resume.

---

## 🧰 Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- Google Generative AI (Gemini)
- `PyPDF2` (for reading PDF resumes)
- `python-docx` (for parsing `.docx` resumes)
- `dotenv` (for managing API keys securely)

---

## 📂 File Support

✅ Supported formats:
- PDF (`.pdf`)
- Word (`.docx`)

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install streamlit google-generativeai python-dotenv python-docx PyPDF2

2. Set Your API Key

Create a .env file in your project root with the following:

GOOGLE_API_KEY=your_google_api_key_here

🔑 You can get your Gemini API key from Google AI Studio

3. Run the App

streamlit run app.py



⸻

✨ Output Format

The app will generate a response in the following structured format:

---------------------
Evaluation Results:
---------------------
Job Description Match: 78%
Missing Keywords: [TensorFlow, Docker, GCP]
Profile Summary: 
"Headline: Machine Learning Engineer with strong data analytics background.
- Proficient in Python and SQL
- Experienced in model development and deployment
- Adept in data preprocessing and visualization"
---------------------



⸻

💡 Use Cases
	•	Students and professionals refining resumes for Data/AI/ML jobs
	•	Recruiters seeking quick JD alignment
	•	Career counselors and resume reviewers

⸻

⚠️ Disclaimer

The tool is for educational and preliminary evaluation purposes only. Do not rely solely on the AI evaluation for job applications.

⸻

🙌 Credits
	•	Google Gemini (Generative AI)
	•	Streamlit Community
	•	Python Open Source Libraries

