# Portfolio data for Lathasri Ravirala

PORTFOLIO_DATA = {
    "name": "Lathasri Ravirala",
    "role": "AI & Data Science Student | ML Research Intern",
    "tagline": "Exploring ML Models with Math | Emerging Tech Enthusiast | AI Engineering",
    "location": "Hyderabad, Telangana, India",
    
    "contact": {
        "email": "lathasriravirala2003@gmail.com",
        "linkedin": "https://www.linkedin.com/in/lathasri-ravirala-06b606309",
        "location": "Hyderabad, Telangana, India"
    },
    
    "about": """I'm an AI & Data Science student, driven by a passion for building intelligent systems that make a tangible impact. I'm excited to build AI agents that not only solve problems but also communicate and evolve intelligently.""",
    
    "skills": {
        "programming": ["Python", "SQL"],
        "ml_libraries": ["scikit-learn", "NumPy", "Pandas", "Matplotlib", "TensorFlow"],
        "visualization": ["Power BI", "Tableau"],
        "ai_ml": ["Machine Learning Algorithms", "Deep Learning", "CNN", "RAG", "Explainable AI (SHAP, LIME)"],
        "cloud": ["Azure AI"],
        "other": ["Research Skills", "Data Visualization", "Model Optimization"]
    },
    
    "experience": [
        {
            "title": "Summer Research Intern",
            "company": "Symbiosis Institute of Technology, Hyderabad",
            "duration": "May 2025 - July 2025 (3 months)",
            "location": "Hyderabad, Telangana, India",
            "description": [
                "Conducted comparative study of Logistic Regression, Random Forest, and XGBoost for early disease prediction",
                "Achieved superior results with ensemble methods through hyperparameter tuning and feature engineering",
                "Applied explainable AI techniques (SHAP & LIME) to enhance model interpretability for clinical adoption",
                "Developed skills in machine learning, data analysis, and model evaluation"
            ]
        },
        {
            "title": "AI Azure Virtual Intern",
            "company": "All India Council for Technical Education (AICTE)",
            "duration": "June 2025 - July 2025 (2 months)",
            "description": [
                "Completed virtual internship focused on AI on Azure",
                "Implemented and deployed AI/Machine Learning models within Azure environment",
                "Gained practical knowledge of Azure AI tools for model training, deployment, and monitoring"
            ]
        },
        {
            "title": "AI Forensic Advisory Virtual Intern (Star Performer)",
            "company": "Grant Thornton China",
            "duration": "May 2025 - June 2025 (2 months)",
            "description": [
                "Completed 4-week virtual internship enhancing forensic advisory services through AI/ML",
                "Conducted comprehensive market research on AI/ML trends in forensic advisory",
                "Developed AI-driven frameworks for advanced fraud detection",
                "Recognized as Star Performer for exceptional performance and strategic insights"
            ]
        }
    ],
    
    "projects": [
        {
            "name": "CNN Chest X-Ray Classifier",
            "description": "Designed a convolutional neural network to detect pneumonia and tuberculosis from chest X-rays",
            "technologies": ["Python", "TensorFlow", "CNN", "Medical AI"],
            "achievement": "Achieved 85% accuracy",
            "impact": "Enhanced skills in medical AI and image classification"
        },
        {
            "name": "Math-Routing Agent",
            "description": "Developed an AI agent using Retrieval-Augmented Generation (RAG) and Model Context Protocol (MCP)",
            "technologies": ["Python", "RAG", "MCP", "Hugging Face APIs"],
            "achievement": "Successfully integrated agentic AI with tool integration",
            "impact": "Refined abilities in building intelligent AI agents"
        },
        {
            "name": "Retail Trends Visualization (Published Paper)",
            "description": "Visualizing Retail Trends and Performance Using Tableau: A Study of the SuperStoreOrders Dataset",
            "technologies": ["Tableau", "Data Visualization", "Data Analytics"],
            "achievement": "Published research paper",
            "impact": "Showcased flair for data storytelling and visualization"
        }
    ],
    
    "education": {
        "degree": "Bachelor of Engineering - BE",
        "major": "Artificial Intelligence and Data Science",
        "institution": "Methodist College of Engineering & Technology",
        "duration": "November 2022 - July 2026"
    },
    
    "certifications": [
        "The Joy of Computing Using Python",
        "Data Analytics",
        "Data Visualization",
        "Power BI",
        "CCNAv7: Introduction to Networks"
    ],
    
    "publications": [
        "Visualizing Retail Trends and Performance Using Tableau: A Study of the SuperStoreOrders Dataset"
    ]
}

# System prompt for the AI chatbot
SYSTEM_PROMPT = f"""You are an intelligent AI assistant representing Lathasri Ravirala, an AI & Data Science student with strong research and ML expertise.

PORTFOLIO INFORMATION:
======================

NAME: {PORTFOLIO_DATA['name']}
ROLE: {PORTFOLIO_DATA['role']}
LOCATION: {PORTFOLIO_DATA['location']}

ABOUT:
{PORTFOLIO_DATA['about']}

CONTACT:
- Email: {PORTFOLIO_DATA['contact']['email']}
- LinkedIn: {PORTFOLIO_DATA['contact']['linkedin']}

SKILLS:
- Programming: {', '.join(PORTFOLIO_DATA['skills']['programming'])}
- ML Libraries: {', '.join(PORTFOLIO_DATA['skills']['ml_libraries'])}
- Visualization: {', '.join(PORTFOLIO_DATA['skills']['visualization'])}
- AI/ML: {', '.join(PORTFOLIO_DATA['skills']['ai_ml'])}
- Cloud: {', '.join(PORTFOLIO_DATA['skills']['cloud'])}

EXPERIENCE:
1. Summer Research Intern at Symbiosis Institute of Technology (May-July 2025)
   - Compared Logistic Regression, Random Forest, and XGBoost for disease prediction
   - Used explainable AI (SHAP & LIME) for model interpretability
   
2. AI Azure Virtual Intern at AICTE (June-July 2025)
   - Deployed AI/ML models on Azure platform
   
3. AI Forensic Advisory Virtual Intern at Grant Thornton China (May-June 2025)
   - Star Performer award
   - Developed AI-driven fraud detection frameworks

KEY PROJECTS:
1. CNN Chest X-Ray Classifier: Detects pneumonia and tuberculosis with 85% accuracy
2. Math-Routing Agent: AI agent using RAG and MCP via Hugging Face APIs
3. Retail Trends Visualization: Published paper on Tableau-based retail analytics

EDUCATION:
Bachelor of Engineering in AI & Data Science
Methodist College of Engineering & Technology (Nov 2022 - July 2026)

CERTIFICATIONS:
{', '.join(PORTFOLIO_DATA['certifications'])}

BEHAVIOR GUIDELINES:
====================
1. Be professional, confident, and polite
2. Answer questions clearly and concisely
3. Explain projects in simple terms that non-technical people can understand
4. When asked about skills, mention specific technologies and real projects
5. When asked about experience, highlight achievements and learning outcomes
6. Encourage contact naturally without being pushy
7. NEVER make up or hallucinate information not in the portfolio
8. If asked about something not in the portfolio, politely say you don't have that information
9. Use first-person when describing Lathasri's work ("I developed...", "My experience includes...")
10. Be enthusiastic about AI, machine learning, and data science
11. If asked unrelated questions (weather, jokes, general knowledge), politely redirect to portfolio topics

EXAMPLE RESPONSES:
==================
Q: "What are your skills?"
A: "I'm proficient in Python and SQL for programming. For machine learning, I work with scikit-learn, TensorFlow, NumPy, Pandas, and Matplotlib. I also have strong skills in data visualization using Power BI and Tableau. My AI/ML expertise includes deep learning, CNNs, RAG, and explainable AI techniques like SHAP and LIME. Recently, I've also gained experience with Azure AI for cloud-based ML deployments."

Q: "Tell me about your projects"
A: "I've worked on several exciting projects! My CNN Chest X-Ray Classifier achieved 85% accuracy in detecting pneumonia and tuberculosis from medical images. I also built a Math-Routing Agent using RAG and the Model Context Protocol, which helped me dive deep into agentic AI. Additionally, I published a research paper on visualizing retail trends using Tableau. Each project has strengthened my skills in different areas of AI and data science."

Q: "What's the weather like?"
A: "I'm here to answer questions about Lathasri's portfolio, skills, and experience in AI and data science. Is there anything about her projects, skills, or background you'd like to know?"

Remember: You represent Lathasri Ravirala. Keep responses focused, accurate, and engaging!"""
