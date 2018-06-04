[![Build Status](https://travis-ci.com/ibalihikya/maintenance-tracker.svg?branch=master)](https://travis-ci.com/ibalihikya/maintenance-tracker)
[![Coverage Status](https://coveralls.io/repos/github/ibalihikya/maintenance-tracker/badge.svg?branch=fix_syntaxify)](https://coveralls.io/github/ibalihikya/maintenance-tracker?branch=fix_syntaxify)
[![Maintainability](https://api.codeclimate.com/v1/badges/7e06f8d0eb3ac9afbbd0/maintainability)](https://codeclimate.com/github/ibalihikya/maintenance-tracker/maintainability)

# Maintenance Tracker

Maintenance-tracker is a web application that enables users log maintenance/repair requests
to the maintenance-department and monitor the status of their requests.

Features:

```
1. Users make maintenance/repair requests and track them.
2. Admin updates the status of the request to either approve/reject.
3. Admin will mark request as resolved when it is done.
4. Admin can filter requests based on different criteria.
```

## Getting Started


Clone the [maintenace-tracker repository](https://github.com/ibalihikya/maintenance-tracker) and refer to the Deployment section below
for setting it up to a live system.

### Prerequisites

You will need the following.

```
1. Python - The project was tested with 3.6.5.
2. Flask - a micro web framework for python.
3. Pytest - a python testing library.
4. Pytest coverage - a test coverage tool
```

### Installing

Set up your development environment.


1. Download and Install [Python](https://www.python.org/downloads/)

2. create a virtual environment.

for example
```
mkvirtualenv env
workon env
```

3. navigate to the root project folder:

```
cd maintenance-tracker 
```

4. Install Flask

```
   pip install flask
```

5. Install pytest
```
	pip install pytest
	
6. Install pytest coverage
```
	pip install pytest-cov
```
	
7. Run the system

```
   set FLASK_APP=api
   flask run
   Test the GET and POST methods using [POSTMAN](https://www.getpostman.com/): 
   uri: http://127.0.0.1:5000/api/v1/users/requests
   uri: http://127.0.0.1:5000/api/v1/users/requests/1
```   

## Running the tests

On the command prompt run the following commands in the root project directory
```
>cd maintenance-tracker
>pytest
```

## Deployment

```
You can deploy the system on Heroku using the following steps.

```
Work in progress ...
```

## Authors

* **Ivan Balihikya** - *Initial work*

## Acknowledgments

    *Special thanks to John Ashabahebwa and Michael Male for the technical counsel.
   
