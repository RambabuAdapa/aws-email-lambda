import boto3
import json

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    name = data['name']
    email = data['email']
    phone = data['phone']
    message = data['message']

    sender_email = 'rambabuadapa3333@gmail.com'  # Replace with your verified sender email
    recipient_email = 'rambabuadapa3333@gmail.com'  # Replace with the recipient's email address

    subject = 'Titcket booked'
    email_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    try:
        # Send email
        response = ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': email_content}}
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Email sent successfully through lambda service')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error sending email: {str(e)}')
        }
