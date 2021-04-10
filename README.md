# ElasticSearch PoC

This is a basic PoC for setting up ElasticSearch from Scratch in a machine and APIs to Insert and Retrieve data from the ES instance

## Inspiration

Elasticsearch is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. -- The ElasticSearch Team
But the primary issue is that many people are unaware how this can be used in existing web applications
This is a lightweight application which will store the data on ES cluster and then retrieve using ES - Python Queries

## Technologies Used:
* Python Flask
* ElasticSearch
* Docker

*Ensure to allocate more than 4 GB of space for docker, to ensure that the elastic cluster starts without fail*

## Machine:
MacOS 11

## Some Useful Links:

* [ES Setting up](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html)
* [Docker Setup](https://docs.docker.com/docker-for-mac/install/)
* [Python Flask](https://flask.palletsprojects.com/en/1.1.x/)


## Setup

*This is done using ES 7+ and Python 3.7.5*

## Getting started

* Steps for setting up on your machine
1. Pull the latest code from *main* branch
2. Create a python virtualenv
3. Install packages mentioned in requirements.txt
4. Use docker-compose up to create the ES container
5. Run flask_app.py to get started
6. api contains the python APIs for accessing ES using python

