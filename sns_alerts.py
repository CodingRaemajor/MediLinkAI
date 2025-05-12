import boto3

def send_health_alert(symptom_text, name, age):
    sns = boto3.client("sns", region_name="us-east-1")

    topic_arn = "arn:aws:sns:us-east-1:605134432713:MediLinkAlerts"  # Your confirmed topic

    message = f"""🚨 EMERGENCY ALERT 🚨
Patient Name: {name}
Age: {age}
Critical Symptoms: {symptom_text}

Immediate medical attention may be required.
- MediLink AI"""

    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="🚨 MediLink Health Emergency"
    )