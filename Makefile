deploy: secrets.py
	[ -f "secrets.py" ] || ( echo 'Please create a secrets.py file with slack_alertlib_webhook_url = the value from `gcloud --project khan-academy secrets versions access latest --secret Slack__API_token_for_alertlib`' ; exit 1 )
	gcloud app deploy app.yaml cron.yaml --set-default

secrets.py:
	echo "slack_alertlib_api_token = `gcloud --project khan-academy secrets versions access latest --secret Slack__API_token_for_alertlib`" > secrets.py

.PHONY: deploy
