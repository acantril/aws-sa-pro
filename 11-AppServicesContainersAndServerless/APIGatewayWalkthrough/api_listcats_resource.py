import json
import os

def lambda_handler(event, context):
  print (event)
  statusCode = 200
  return {
    "statusCode": statusCode,
    # Imagine this is being loaded from a database
    "body": json.dumps(["roffle", "truffles", "penny", "winkie"]),
    "headers": {
      "Content-Type": "application/json"
    }
  }
