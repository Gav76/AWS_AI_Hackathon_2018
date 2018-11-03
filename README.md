# AWS_AI_Hackathon_2018
This is the repo for entry into the [AWS AI Hackathon](https://aws.amazon.com/machine-learning/2018-Q3-ai-hackathon/)

The basic premise was to build a pipeline where you can provide an image containing some text and have the text extracted, language identified, sentiment evaluated and a translation into English provided if needed.  There are some real-world use-cases where this could be useful, ie.

### Tools used
1. Python
2. AWS Lambda
3. AWS Rekognition
4. AWS Comprehend
5. AWS Simple Email Service (SES)
6. AWS S3

## Flow

![Workflow](https://github.com/Gav76/AWS_AI_Hackathon_2018/blob/master/workflow.png)

### Known Limitations.
The [AWS Rekognition Detect Text Action](https://docs.aws.amazon.com/rekognition/latest/dg/text-detection.html) can only detect 50 words from a single image.

Only jpeg and png images are supported by Rekognition.

## Usage

To use the tool, simply sent an email to AIHackathon@perrie.uk with the image attached.

Within a few minutes the results will be returned to the same email address that was used to send the image.  See the sample response below;

```
Hi,

Thanks for using the AI Hackathon tool, your results are below.

The original message was received from : Sender Name

The original message had the subject : FW: echo

I found the file : echo.png

The recognized text was : Amazon Echo verfugt uber Tausende Skills und es kommen standig neue dazu. Mit Skills werden noch mehr Funktionen hinzugefugt, wie ein Taxi von mytaxi bestellen, Fitnesstracking mit Fitbit, neue Rezepte entdecken mit Chefkoch, Zugfahrplane abrufen mit Deutsche Bahn und mehr. Um neue Skills zu aktivieren, fragen Sie einfach Alexa.

The detected language was : de

The text translated into English is : Amazon Echo has thousands of skills and new skills. Skills add more features such as ordering a taxi from mytaxi, fitness tracking with Fitbit, discovering new recipes with Chef, retrieving a train tarpaulin with Deutsche Bahn and more. To activate new skills, just ask Alexa.

The sentiment of the text is : Sorry, only English and Spanish are currently supported for sentiment detection

Note: No messages to this address are stored or retained. All mails and attachments have been deleted after processing.
```
