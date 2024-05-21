#!/usr/bin/env python3

# TODO(csilvers): make this a cloud-function that lives in
# khan-internal-services, and use cloud-scheduler to run it.

import csv
import random
import re
import urllib.request

import flask

import alertlib

_DEFAULT_CHANNEL = "#1s-and-0s"
_CULTURE_MESSAGES_CSV_URL = "https://docs.google.com/spreadsheets/d/1EtgPvCh0a0AFDOW2vu_ugWQTZVQbsPXKEebbOoqof90/pub?gid=0&single=true&output=csv"

_RESPOND_REGEXP = re.compile(r'culture us$')

app = flask.Flask(__name__)


def _get_culture():
    url = _CULTURE_MESSAGES_CSV_URL
    lines = urllib.request.urlopen(url).read().decode('utf-8').splitlines()
    msgs = list(csv.reader(lines))
    message = random.choice(msgs)[0]
    moo = 'M' + 'o' * random.randrange(2, 10) + '.'
    return "%s  %s" % (message, moo)


@app.route("/culture", methods=["GET"])
def culture_get():
    """Invoked by cron."""
    alertlib.Alert(_get_culture()).send_to_slack(
        _DEFAULT_CHANNEL, sender="Culture Cow", icon_emoji=":cow:")


@app.route("/culture", methods=["POST"])
def culture_post():
    """Hit by the culture cow outgoing webhook in Slack.

    In this case, we can just return our reply in HTTP and be done.
    """
    if _RESPOND_REGEXP.search(flask.request.args.get("text")) is not None:
        return {'text': _get_culture()}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
