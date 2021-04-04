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

Flow Architecture:

**Service #2**

A text generator with 2 different implementations available:

One that creates 4 char Strings of lowercase letters
One that creates 2 char String of uppercase letters

**Service #3**

A number generator with 2 different implementations available:

One that creates a 4-digit number.
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

Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
The goal behind NGINX was to create a fast web server for handling a large amount of concurrent connections.An NGINX reverse proxy server sits in front of web servers and forwards client requests (e.g. web browsers) to those web servers.Reverse proxies are typically implemented to help increase security, performance, and reliability.

🎁 Programming Language - Python (Flask micro-framework)

🎁 CI Server - Jenkins

🎁 Markup Languages for Front-end -  Flask(HTML)

🎁 Webhooks

Webhooks were used so that whenever there is a change it automatically triggers a build automatically from SCM(this Github) Therefore instead of constantly checking for new changes, 
the job can be triggered by a web hook which is really just a HTTP POST request to the jenkins server.

🎁 Containerisation Tool - Docker/Compose 

Docker compose was used to sreamline the process of having to use several Docker CLI commands to declare what docker resources we want 
which takes longer and creates room for human error. A Docker Compose file achieved this by allowing you to define and run multiple Docker containers with a single command 
through a single configuration file that specifies the deployment.

Benefits include:

**.** Build multiple images/containers with one command

**.** Easy to read and edit

**.** Automatically puts your containers into a network

**.** Containers are deployed as services


🎁 Orchestration Tool - Docker Swarm

A container orchestration tool which is used to run a network of containers across multiple host machines, also known as nodes.
Nodes are grouped together in clusters of managers and workers. Manager nodes manage the Swarm while the worker nodes merely host containers. The
containers in a Swarm are run as services, and are therefore all replicas of each other, which thereby provides redundancy and high availability to the applications. It also allows for the deployment of the
 containers at scale. 

Benefits include:

**.** Easily scale up/down containers 

**.** Replicate containers for increased redundancy and improved resiliency

**.** Deploy containers across multiple machines (nodes) 

**.** Load balancing between containers 

**.** Dynamically re-allocate containers across nodes 

**.** Rolling updates can be done without stopping or restarting any containers 

🎁 Configuration management - Ansible Playbook

🎁 Open source repository management - Nexus 

Used to proxy, collect, and manage your dependencies, so that you are not constantly juggling a collection of Docker images. Cached artefacts, so that, after the first build, the project will consult the cache before downloading anything. Installed Nexus on a local server, so that the builds have access to any artefacts that have previously been downloaded, even if the servers go offline.

Benefits include:

**.** A secure, private, and trusted location to host images

**.** Offline access to stored images

**.** Using local copies of commonly used images is more efficient and speeds up deployment.

🎁 VS Code

🎁 Operating System - Linux

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

