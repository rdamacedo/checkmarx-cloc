# Cloc Script Overview

Cloc counts blank lines, comment lines, and physical lines of source code in many programming languages. 
The idea of this wrapper is just use a docker image with a wrapper to send the report via email. 

##Requirements

The only requirement to run it is the docker installed. 

## Quick start

In the root of the repo change the settings to the desired ones and them docker build and docker run. 

You must change repoUrl and smtp connection details to make this work:

```
{
  "smtp_server": [
    {
      "server": "smtp_server",
      "port": "port",
      "SSL": "False",
      "sender": "sender",
      "recipient": "recipient",
      "subject": "subject",
      "username": "username",
      "password": "password"
    }
  ],
  "repository": [
    {
      "repoUrl": "repo_url",
      "repoFolder": "/tmp/"
    }
  ]
}
```


Then you must run the docker build and run to execute it. 

```
docker build -t clocwrapper .

docker run clocwrappe
```