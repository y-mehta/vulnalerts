import wget
import os
import requests
import json


def get_nvd_feed():
    url = 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.zip' # NVD Feed URL
    wget.download(url)
    command = 'unzip -o nvdcve-1.0-recent.json.zip' # Unzip json.gz file
    os.system(command)

def get_cpes():
    with open('cpe.txt', 'r') as v:
        cpe = v.readlines()
        return cpe

def parse_nvd_feed(cpes):
    get_nvd_feed()
    with open('nvdcve-1.0-recent.json','r') as f:
        cve_feed = json.load(f)
    cve_index = 0
    cve_count = 0
    message = ""

    for x in cve_feed['CVE_Items']:
        id = cve_feed['CVE_Items'][cve_index]['cve']['CVE_data_meta']['ID']
        description = cve_feed['CVE_Items'][cve_index]['cve']['description']['description_data'][0]['value']
        try:
            cpe_string = cve_feed['CVE_Items'][cve_index]['configurations']['nodes'][0]['cpe_match']
        except:
            cpe_string = ""
        for line in cpes:
            for cpe in line.split():
                for x in cpe_string:
                    if cpe in x.get('cpe23Uri'):
                        message = message + slack_block_format(cpe, description, id)
                        cve_count = cve_count + 1
        cve_index = cve_index + 1
    return message,cve_count

def slack_block_format(product, description, id):
    block = ',{"type": "section", "text": {"type": "mrkdwn","text": "*Product:* ' + product + '\n *CVE ID:* ' + id + '\n *Description:* ' + description + '\n "}}, {"type": "divider"}'
    return block

def send_slack_alert(message,cve_count):
    url = os.getenv('SLACK_WEBHOOK')
    slack_message = '{"blocks": [{"type": "section","text": {"type": "plain_text","emoji": true,"text": "Hello :wave:,'+ str(cve_count) +' Security Vulnerabilities affecting your Tech Stack were disclosed today."}}' + message + ']}'
    x = requests.post(url, data=slack_message)

def main():
    print("VulnAlerts Using GitHub Actions\n")
    message,cve_count = parse_nvd_feed(get_cpes())
    send_slack_alert(message,cve_count)
    print("Notification Sent")

if __name__ == '__main__':
    main()
