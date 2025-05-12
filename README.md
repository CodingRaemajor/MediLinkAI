🤖 MediLink AI – Remote Health Diagnosis & Emergency Alert System

MediLink AI is an AI-powered remote symptom checker designed to assist users in rural or underserved regions with quick health analysis and real-time emergency alerts. Built using AWS services, this tool enables users to input symptoms and receive a smart AI-generated diagnosis — along with automatic emergency notifications for critical health cases.

🌐 Live Demo

Streamlit App: https://medilinkai.streamlit.app/

🚀 Features

✅ AI-Powered Symptom Analysis

Enter symptoms (e.g., "fever, chest pain")

Amazon Bedrock (Claude v2) provides a 3-sentence health insight

✅ Real-Time Emergency Alerts

Critical symptoms like "chest pain" or "shortness of breath" trigger alerts

Sends automated alerts via Amazon SNS (email or SMS) to healthcare responders

✅ Cloud-Based Health Records

Each submission is saved to Amazon DynamoDB

Enables future features like patient history and analytics

✅ Simple, Intuitive Interface

Streamlit-based front end for easy accessibility

Works on mobile, desktop, and low-bandwidth connections

🧠 How It Works

User fills in name, age, gender, and symptoms

Symptoms are analyzed by Amazon Bedrock (Claude v2)

If critical terms are detected, an alert is sent via Amazon SNS

All submissions are logged in Amazon DynamoDB for storage

🔧 Tech Stack

Amazon Bedrock – Generative AI for health insight

Amazon SNS – Sends critical health alerts

Amazon DynamoDB – Stores patient records

Streamlit – Front-end app (deployed via Streamlit Cloud)

📦 Folder Structure

├── symptom_checker_ui.py     # Streamlit UI logic
├── bedrock_handler.py        # Handles Claude v2 AI requests
├── sns_alerts.py             # Sends email/SMS using SNS
├── dynamodb_handler.py       # Interacts with DynamoDB
├── requirements.txt          # App dependencies

🔐 Secrets Configuration (Streamlit Cloud)

Define the following in your Streamlit Cloud secrets:

AWS_ACCESS_KEY_ID = "<your-access-key-id>"
AWS_SECRET_ACCESS_KEY = "<your-secret-access-key>"
AWS_REGION = "us-east-1"

📍 Use Cases

Rural telemedicine diagnosis

Health alerting system for NGOs or mobile clinics

Campus and workplace health monitoring

🛠 Future Enhancements

IoT device integration (wearables)

Multi-language support

Patient health trends dashboard

📫 Contact

Built by Parth Patel

Feel free to fork, improve, or collaborate on MediLink AI!
