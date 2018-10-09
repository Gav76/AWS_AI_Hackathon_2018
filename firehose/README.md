# Firehose

Use firehose to stream twitter updates into s3 

## Prerequisites
Install and configure the aws cli following the instructions here

   [Install and Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)

## Create S3 bucket
Create an S3 bucket to store the scraped Twitter data

## create IAM policies
In s3_rw_policy.json replace DEMO_BUCKET_NAME with the name of the bucket created above

Run the commands to create the policies

```
aws iam create-role --role-name firehose_delivery_role --assume-role-policy-document file://firehose-policy.json

aws iam put-role-policy --role-name firehose_delivery_role --policy-name firehose-s3-rw --policy-document file://s3-rw-policy.json
```



 
