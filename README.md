# iReporter
[![Build Status](https://travis-ci.org/IssaIan/iReporter.svg?branch=Develop)](https://travis-ci.org/IssaIan/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/IssaIan/iReporter/badge.svg?branch=Develop)](https://coveralls.io/github/IssaIan/iReporter?branch=Develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/e966a76f77ada3c9688f/maintainability)](https://codeclimate.com/github/IssaIan/iReporter/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e966a76f77ada3c9688f/test_coverage)](https://codeclimate.com/github/IssaIan/iReporter/test_coverage)

## About iReporter
This is an application that enables its users to report issues such as corruption and others public concern issues to the government and other involved organisations.

## Installation
### 1. Clone the repository:
https://github.com/IssaIan/iReporter.git
### 2. Create a virtual environment and activate it:
python3 -m virtualenv env 
source evn/bin/activate
### 3. Install environment variables:
pip install -r requirements.txt
### 4. Install app:
export FLASK_APP=run.py
### 5. Run the application:
flask run

## API Endpoints:
1. Create an incident: /api/v1/incidents
2. Edit a specific incident comment/description: /api/v1/incident_id/descrition
3. Edit a specific incident location: /api/v1/incident_id/location
4. Create a user: /api/v1/users
5. Get or update a specific user: /api/v1/users/user_id




