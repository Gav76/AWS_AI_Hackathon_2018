# Firehose

Use firehose to stream twitter updates into s3

## Prerequisites
Install and configure the aws cli following the instructions here

   [Install and Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)

## Create S3 bucket
Create an S3 bucket to store the scraped Twitter data

## create IAM policies
In firehose_policy.json, replace account_id with your AWS account.

In s3_rw_policy.json replace DEMO_BUCKET_NAME with the name of the bucket created above

Run the commands to create the policies

```
aws iam create-role --role-name firehose_delivery_role --assume-role-policy-document firehose-policy.json

aws iam put-role-policy --role-name firehose_delivery_role --policy-name firehose-s3-rw --policy-document s3-rw-policy.json
```

## Create an EC2 instance to run the twitter producer

Create an EC2 instance and connect over ssh.  Example:

```
ssh -i "AWSAIHackathon2018.pem" ec2-user@ec2-1-2-3-4.eu-west-1.compute.amazonaws.com
```
Install node.js
```
sudo yum -y install nodejs npm --enablerepo=epel
```
configure the AWS CLI
```
aws configure
```
Download and unzip the producer package [Producer Package](https://update me) then install it
```
npm install
```
Update config.js with the following custom parameters

  firehose
  DeliveryStreamName – Name your stream. The app creates the delivery stream if it does not exist.
  BucketARN: Use the bucket matched to the Lambda function.
  RoleARN: Get your account ID from the IAM dashboard users sign-in link https://Your_AWS_Account_ID.signin.aws.amazon.com/console/. Use the Firehose role you created earlier (“firehose_delivery_role”).
  Prefix: Use the same s3 prefix that you used in your Lambda function event source (e.g., twitter/raw-data/).
  twitter – Enter your twitter application keys.
  region – Enter your Firehose region (e.g., us-east-1, us-west-2, eu-west-1).
