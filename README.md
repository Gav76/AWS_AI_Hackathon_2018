# AWS_AI_Hackathon_2018
This is the repo for entry into the [AWS AI Hackathon](https://aws.amazon.com/machine-learning/2018-Q3-ai-hackathon/)

The basic premise was to build a pipeline where you can provide an image containing some text and have the text extracted, language identified, sentiment evaluated and a translation into English provided if needed.  There are some real-world use-cases where this could be useful, ie.

### Tools used
Python
AWS Lambda
AWS Rekognition
AWS Comprehend
AWS Simple Email Service (SES)
AWS S3

## Flow

![Workflow](https://github.com/Gav76/AWS_AI_Hackathon_2018/blob/master/workflow.png)

### Known Limitations.
The [AWS Rekognition Detect Text Action](https://docs.aws.amazon.com/rekognition/latest/dg/text-detection.html) can only detect 50 words from a single image.

##
