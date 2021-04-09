#!/bin/bash 
sudo apt get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


python3 -m pytest coreservice --cov-coreservice --cov-report-term-missing
python3 -m pytest servicetwo --cov-servicetwo --cov-report-term-missing
python3 -m pytest servicethree --cov-servicethree --cov-report-term-missing
python3 -m pytest servicefour --cov-servicefour --cov-report-term-missing