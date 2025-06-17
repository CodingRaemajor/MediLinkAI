import boto3
import json
from botocore.exceptions import ClientError

def get_diagnosis_from_bedrock(symptom_text):
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

        prompt = f"""You are a compassionate and experienced medical doctor consulting a patient remotely through MediLinkAi. Based on the following symptoms, provide a thoughtful and professtional clinical response. Speak clearly and confidently, like you're sitting across from the patient in a real consultation."

        Patient's symptoms: {symptom_text}

        Respond with a brief 2 to 3 sentence diagnosis-styled explanation, followed by practical next steps or self-care advice. Be medically resonable, human-like, and avoid sounding like a machine or giving disclamers. Prioritize safety, empathy, and clarity.
        """

        body = json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 300,
                "temperature": 0.5,
                "topP": 0.9
            }
        })

        response = bedrock.invoke_model(
            modelId="amazon.titan-text-lite-v1",
            body=body,
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response['body'].read())
        return str(result.get("results", [{}])[0].get("outputText", "Sorry, no diagnosis returned."))

    except ClientError as e:
        print("Bedrock access error:", e)
        return f"🧠 Based on your symptoms ({symptom_text}), you may have a mild condition. Please monitor symptoms and consult a doctor if they worsen."