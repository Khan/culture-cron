#!/usr/bin/env python3

"""Send a message to slack every time this is run.

This is meant to be called from cron.  It requires the alertlib
secret, e.g. via a ./secrets.py file with this content:
    slack_alertlib_api_token = `gcloud --project khan-academy secrets versions access latest --secret Slack__API_token_for_alertlib`
"""

import csv
import random
import re
import urllib.request

import alertlib

_DEFAULT_CHANNEL = "#1s-and-0s"
_CULTURE_MESSAGES_CSV_URL = "https://docs.google.com/spreadsheets/d/1EtgPvCh0a0AFDOW2vu_ugWQTZVQbsPXKEebbOoqof90/pub?gid=0&single=true&output=csv"


def main():
    url = _CULTURE_MESSAGES_CSV_URL
    lines = urllib.request.urlopen(url).read().decode('utf-8').splitlines()
    msgs = list(csv.reader(lines))
    message = random.choice(msgs)[0]
    moo = 'M' + 'o' * random.randrange(2, 10) + '.'
    slack_text = "%s  %s" % (message, moo)

    alertlib.Alert(slack_text).send_to_slack(
        _DEFAULT_CHANNEL, sender="Culture Cow", icon_emoji=":cow:")


if __name__ == "__main__":
    main()
