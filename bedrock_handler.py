import boto3
import json
from botocore.exceptions import ClientError

def get_diagnosis_from_bedrock(symptom_text):
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

        prompt = f"""You are a helpful virtual health assistant. Based on the following symptoms, provide a general possible cause and what the patient can do next. Keep it medically reasonable and within safety limits.

Patient's symptoms: {symptom_text}

Respond in 3 sentences and include general self-care advice. Do not mention you're an AI or disclaim excessively.
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