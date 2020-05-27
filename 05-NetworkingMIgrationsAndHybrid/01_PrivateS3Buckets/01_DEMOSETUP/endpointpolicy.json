{
    "Version":"2012-10-17",
    "Statement":[
    {
        "Effect":"Allow",
        "Principal": "*",
        "Action": "s3:*",
        "Resource":[ 
        "arn:aws:s3:::PRIVATECATSBUCKETNAME/*",
        "arn:aws:s3:::PUBLICCATSBUCKETNAME/*"
        ]
    },
    {
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : "s3:ListBucket",
        "Resource" : [
        "arn:aws:s3:::PRIVATECATSBUCKETNAME",
        "arn:aws:s3:::PUBLICCATSBUCKETNAME"
        ]
    },
    {
        "Effect" : "Allow",
        "Principal": "*",
        "Action":[
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation"
        ],
        "Resource" : "*"
    }
    ]
}