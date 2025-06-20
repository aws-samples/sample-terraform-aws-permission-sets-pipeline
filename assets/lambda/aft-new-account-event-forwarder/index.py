"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import sys
import logging
import json
import os
import boto3
from botocore.config import Config

# Logging configuration
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger()
log.setLevel(logging.INFO)

# Config to handle throttling for each boto3 client
config = Config(retries={"max_attempts": 50, "mode": "adaptive"})

# Boto client
client = boto3.client("events")


def lambda_handler(event, context):
    """Lambda handler for new account event forwarder"""

    try:
        log.info("Incoming event: %s", json.dumps(event))
        for record in event["Records"]:
            message = json.loads(record["Sns"]["Message"])
            response = client.put_events(
                Entries=[
                    {
                        "Source": "aft-new-account-event-forwarder",
                        "DetailType": message["Input"]["control_tower_event"][
                            "detail-type"
                        ],
                        "Detail": json.dumps(
                            message["Input"]["control_tower_event"]["detail"]
                        ),
                        "EventBusName": os.environ.get("EVENT_BUS_ARN"),
                    }
                ]
            )
            log.info(
                "Event sent: %s",
                json.dumps(message["Input"]["control_tower_event"]["detail"]),
            )
            log.debug(json.dumps(response))
            return response
    except Exception as e:
        log.error(str(e))
        raise e
