FROM ubuntu
MAINTAINER harika2724@gmail.com
RUN apt-get update && apt-get install -y python-pip python-dev build-essential && pip install requests
COPY . /src
RUN chmod +x /src/Assignment.py
EXPOSE 90
CMD ["python","/src/Assignment.py"]
