# VulnAlerts - Customized CVE Alerts straight to your Slack Channel

## How to Use?
- [Create an Incoming Webhook on Slack](https://slack.com/intl/en-in/help/articles/115005265063-Incoming-WebHooks-for-Slack)
- Goto Repository Settings -> Secrets -> Add a New Secret
- Enter ```SLACK_WEBHOOK``` in the Secret Name and your slack webhook in the value.
- Add CPEs of the products that you want to monitor for vulnerabilities in the **cpe.txt** file. [NVD CPE Search](https://nvd.nist.gov/products/cpe/search)
- Create new workflow in .github/workflows/alerts.yml
```
name: VulnAlerts

on: 
  schedule:
    - cron:  '15 * */1 * *'

jobs:
  alert:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - uses: y-mehta/vulnalerts@master
      env:
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
    - name: done
      run: echo 'done'
```

- That's it. You'll receive daily alerts on the selected slack channel.

Note: No need to enter full CPE unless you want to monitor specific version. ```apple:icloud``` or ```atlassian:sourcetree``` will do the job.

- Action Schedule can be changed in ```.github/workflows/alerts.yml``` if needed. Follow crontab format(@daily,@monthly etc. aren't supported by Github Actions)

## How it Works?
- GitHub Actions WorkFlow is automatically triggered based on schedule.
- [CVE-Recent JSON Vulnerability Feed](https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.gz) is fetched from the NVD.
- The JSON feed is processed to check if any CPEs mentioned in **cpe.txt** are present in the Feed.
- After processing is done, It'll send the message to Slack Incoming Webhook.

## Sample Alert:

![image](https://user-images.githubusercontent.com/24428063/72280765-19bf9380-365f-11ea-84d3-395a78343f3e.png)


## Security Warning
- Don't hardcode your Slack Incoming Webhook URL into the python file.

## References
- https://nvd.nist.gov/
