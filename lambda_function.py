import boto3
import botocore
import mailparser
import email
import json


def lambda_handler(event, context):
    s3 = boto3.client('s3', region_name='eu-central-1')

    s3bucket = event['Records'][0]['s3']['bucket']['name']
    print (s3bucket)
    s3bucketTemp = s3bucket + '-temp'
    s3object = event['Records'][0]['s3']['object']['key']
    print (s3object)

    filecontents = s3.get_object(Bucket=s3bucket, Key=s3object)
    j = filecontents['Body'].read().decode('utf-8')

    msg = email.message_from_string(j)

    msg_from = msg['from']
    msg_subject = msg['subject']
    foundattachment = False

    for part in msg.walk():
        print(part.get_content_type())
        if part.get_content_type() in ['image/jpeg', 'image/png', 'image/jpg']:
            print (part.get_filename())
            filename = part.get_filename()
            BODY_TEXT_ERROR = "I found the file : " + filename
            foundattachment = True
            attachment = part.get_payload(decode=True)
            attachmentnameons3 = save_attachment_to_s3(attachment,filename,s3bucketTemp,s3object)
            detectedText = extract_text_from_image(s3bucketTemp, attachmentnameons3)
            detectedLanguage = detect_language(detectedText)

            if detectedLanguage in ['en', 'es']:
                detectedSentiment = detect_sentiment(detectedText, detectedLanguage)
            else:
                detectedSentiment = 'Sorry, only English and Spanish are currently supported for sentiment detection'

            cleanup_files(s3bucket, s3object, s3bucketTemp, filename)

            send_return_mail(msg_from, msg_subject, BODY_TEXT_ERROR, detectedText, detectedLanguage, detectedSentiment)

        else:
            #not an attachment
            print("not an attachment")


        if foundattachment == True:
            print ("foundattachment was true")
        else:
            BODY_TEXT_ERROR = "Sorry, no supported attachments were found.  PLease try again with either jpeg or png"


def send_return_mail(msg_from,msg_subject,BODY_TEXT_ERROR,detectedText, detectedLanguage, detectedSentiment):

    SENDER = "AI Hackathon <AIHackathon@perrie.uk>"
    RECIPIENT = msg_from
    AWS_REGION = "eu-west-1"
    SUBJECT = "AI Hackathon Response"
    BODY_TEXT = ("Hi, \n"
                "Thanks for using the AI Hackathon tool, your results are below.  \n \n"
                "The original message was received from : " + msg_from + "\n"
                "The original message had the subject : " + msg_subject + "\n"
                "" + BODY_TEXT_ERROR + "\n"
                "The recognized text was : " + detectedText + "\n"
                "The detected language was : " + detectedLanguage + "\n"
                "The sentiment of the text is : " + detectedSentiment + "\n"
                "\n \n"
                "Note: No messages to this address are stored or retained.  All mails and attachments have been deleted after processing."
                 )
    BODY_HTML = """<html>
    <head></head>
    <body>
      <p>Hi,</p>
      <p>Thanks for using the AI Hackathon tool, your results are below. </p>
      <p>The original message was received from : """ + msg_from + """ </p>
      <p>The original message had the subject : """ + msg_subject + """ </p>
      <p> """ + BODY_TEXT_ERROR + """ </p>
      <p>The recognized text was : """ + detectedText + """ </p>
      <p>The detected language was : """ + detectedLanguage + """ </p>
      <p>The sentiment of the text is : """ + detectedSentiment + """ </p>
      <p></p>
      <p>Note: No messages to this address are stored or retained.  All mails and attachments have been deleted after processing.</p>
    </body>
    </html>
                """
    CHARSET = "UTF-8"
    ses = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.

    #Provide the contents of the email.
    response = ses.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )

def extract_text_from_image(s3bucket,objectname):

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':s3bucket,'Name':objectname}})

    textDetections=response['TextDetections']
    print (response)
    print ('Detecting text')
    completeText = ''
    for text in textDetections:
            #print ('Detected text:' + text['DetectedText'])
            if text['Type'] == 'WORD':
                completeText = completeText + ' ' + text['DetectedText']

    return completeText

def save_attachment_to_s3(attachment, filename,s3bucket, s3object):
    client = boto3.client('s3')
    objectname = s3object + '/' + filename
    print (objectname)
    client.put_object(Body=attachment, Bucket=s3bucket, Key=objectname)

    return objectname

def detect_language(detectedText):
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

    print('Calling DetectDominantLanguage')
    detectedLanguage = comprehend.detect_dominant_language(Text = detectedText)
    print(detectedLanguage)

    return detectedLanguage['Languages'][0]['LanguageCode']

def detect_sentiment(detectedText, detectedLanguage):
    comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

    print('Calling DetectSentiment')
    detectedSentiment = comprehend.detect_sentiment(Text=detectedText, LanguageCode=detectedLanguage)
    print(detectedSentiment)

    return detectedSentiment['Sentiment']

def cleanup_files(s3bucket,s3object,s3bucketTemp,filename):
    client = boto3.client('s3')
    client.delete_object(Bucket=s3bucket, Key=s3object)
    client.delete_object(Bucket=s3bucketTemp, Key=filename)


    return
