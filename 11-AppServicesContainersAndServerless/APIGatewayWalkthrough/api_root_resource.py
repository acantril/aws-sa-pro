import json
import os

def lambda_handler(event, context):
  print (event)
  body = "cats are the best!"
  statusCode = 200
  return {
    "statusCode": statusCode,
    "body": json.dumps(body),
    "headers": {
      "Content-Type": "application/json"
    }
  }
