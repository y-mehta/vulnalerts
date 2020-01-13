# vulnalerts - Customized CVE Alerts straight to your Slack Channel

## How to Use?
- Fork the project.
- [Create an Incoming Webhook on Slack](https://slack.com/intl/en-in/help/articles/115005265063-Incoming-WebHooks-for-Slack)
- Goto Repository Settings -> Secrets -> Add a New Secret
- Enter ```SLACK_WEBHOOK``` in the Secret Name and your slack webhook in the value.
- Add CPEs of the products that you want to monitor for vulnerabilities in the **cpe.txt** file. [NVD CPE Search](https://nvd.nist.gov/products/cpe/search)

Note: No need to enter full CPE unless you want to monitor specific version. ```apple:icloud``` or ```atlassian:sourcetree``` will do the job.

## How it Works?
- [CVE-Recent JSON Vulnerability Feed](https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.gz) is fetched from the NVD.
- The JSON feed is processed to check if any CPEs mentioned in **cpe.txt** are present in the Feed.
- After processing is done, It'll send the message to Slack Incoming Webhook.

## Security Warning
- Don't hardcode your Slack Incoming Webhook URL into the python file.

## References
- https://nvd.nist.gov/
