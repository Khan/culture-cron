
Culture Cow
===========

The periodic culture sending portion of the former
[Khan/culture-cow](/Khan/culture-cow).

What it means to be Culture Cow
--------------------

1) Culture Cow provides a steady drip of Khan Academy culture, straight into
Slack's veins.

2) If at any point Culture Cow acts like an annoying robot by decreasing the
signal:noise ratio in our Slack channels, it will be turned into delicious
hamburgers.

Can I add more culture magic?
-----------------------------

Absolutely. Simply modify [the Google spreadsheet] with all the phrases.
Just abide by the two rules of Culture Cow above.

[the Google spreadsheet]: https://docs.google.com/a/khanacademy.org/spreadsheets/d/1EtgPvCh0a0AFDOW2vu_ugWQTZVQbsPXKEebbOoqof90/edit?usp=sharing

Where does Khan Academy's Culture Cow live?
-------------------------------------------

It is run on the toby-internal-webserver GCE machine.

The cronjob that runs it, along with the code that sets up the secret it
needs, lives in Khan/aws-config:toby/.

