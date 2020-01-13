FROM python:3-slim

LABEL "com.github.actions.name"="VulnAlerts"
LABEL "com.github.actions.description"="Daily customized CVE Alerts straight to your Slack Inbox for Free."
LABEL "version"="1.0"
LABEL "com.github.actions.icon"="shield"
LABEL "com.github.actions.color"="blue"
LABEL "repository"="https://github.com/y-mehta/vulnalerts"
LABEL "homepage"="https://github.com/y-mehta/vulnalerts"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
