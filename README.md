# Prize Generator

Author: Ayona Duncan

# Project Scope

A service-orientated architecture that randomly 
generates a prize depending on your account number that was generated 
and is composed of at least 4 services that work together.

**Service #1**


The core service – this will render the Jinja2 templates 
 that interact with the application, 
 it will also be responsible 
 for communicating with the other 3 services, 
 and finally for persisting some data in an SQL database.

**Service #2 + #3**

These both generate a random “Object”, that generates a: 

Random number

Random letter

API call to an external API

**Service #4**

This service creates an “Object” based upon the results of service #2 + #3 using some pre-defined rules.


# Architecture 

**Service #2**

A text generator with 2 different implementations available:

One that creates 3 char Strings of lowercase letters
One that creates 2 char String of uppercase letters

**Service #3**

A number generator with 2 different implementations available:

One that creates a 6-digit number.
One that creates an 8-digit number.

**Service #4**

A prize generator with 2 different implementations available, 
in both cases the prize is determined by the char string and number
 generated above.

One for when the service is feeling generous (bigger rewards)
One for when the service is not feeling generous (smaller rewards)'

**User Journey:**

A page is loaded and an Account Number is generated, for example 
let's say it generates “ABC123456”.

Because the first letter of the Account Number is “A” the user has a 25% 
chance to win £100 and a 75% chance to win £50, this is described in
 the logic of service 4.


# Work Progress
I used a Trello board for project management,
please find link attached https://trello.com/b/t1bVao8S/prize-account-number-generator

# Build 

Setting the jenkins job to download this github repo where my code is:


The build script in the CI Server Jenkins using Flask Gunicorn:


# Tech Stack
The tools and requirements used for this application to run are as follows:

🎁 Cloud Server and Database - GCP VM and GCP SQL Server 

🎁 Reverse Proxy - NGINX 

🎁 Programming Language - Python (Flask micro-framework)

🎁 CI Server - Jenkins

🎁 Markup Languages for Front-end -  Flask(HTML)

🎁 Webhooks

🎁 Containerisation Tool - Docker

🎁 Orchestration Tool - Docker Swarm

🎁 Configuration management - Ansible Playbook

🎁 VS Code

🎁 Linux

See requirements.txt file for a full list of all requirements

# Testing

Testing was done with Pytest and Flask Testing

Test analysis:

.All routes were tested for Read, Add, Update and Delete.

.Ensuring that pages with redirects are being redirected.

.Post requests added data and Get requests responded to get requests with a successful status code.

Test Coverage: 99%

![](Test/testcov.jpg)


# Risk Assessment 

 

# Contributors

Special thanks to Dara Oladopo, 
whose guidance was immensely helpful.

# References
https://www.w3schools.com/

https://www.youtube.com/watch?v=SV1eSbAWfWQ&list=PLBf-QcbaigsKwq3k2YEBQS17xUwfOA3O3&index=10

QA community DevOps learning

# License 
This project is licensed under the terms of the MIT license

