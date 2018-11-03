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

The original message was received from : sender name

The original message had the subject : MovieReview

I found the file : moviereview.png

The recognized text was : 10/10 This old Marines thoughts silvaback-13517 8 October 2018 I did not want to watch this movie but took my wife to see it, because we both saw the one with Kris Kristofferson and Barbra Streisand, growing up. The crowd was a lot older than we were(we are almost 50)

The detected language was : en

The sentiment of the text is : NEUTRAL

Note: No messages to this address are stored or retained. All mails and attachments have been deleted after processing.
```
