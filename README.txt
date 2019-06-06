Created a Dockerfile took the base image as centos6

Build a docker image from Dockerfile
   
   docker build -t testimage .

run the cntainer using the dockerimage by passing argument moviename

  docker run -it testimage python /src/Assignment.py "Titanic"
  
Finally the output is
   
     Rotten Tomatoes:84%