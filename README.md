# secistsploit-framework
A pentesting framework written in python
# Development
## Building development environment
The development environment we recommanded linux, If you are using Windows, you can use docker, the development environment's `Dockerfile` is stored in `docker` directory, building environment is easy, just type: `docker build -t ssfdev docker`. Then connect docker container with yours editor or IDE.
## Deploy
If you want deploy SecistSploit framework, just type: `docker build -t secistsploit-framework .`, and run with command: `docker run -it secistsploit-framework`