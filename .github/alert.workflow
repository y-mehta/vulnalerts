name: VulnAlerts

on: 
  schedule:
    - cron:  '* * * * *'

jobs:
  alert:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: install dependencies
      run: pip3 install -r requirements.txt
    - name: run python script
      env:
        SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
      run: python3 main.py
    - name: done
      run: echo 'done'
