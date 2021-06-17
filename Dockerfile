# Download base image ubuntu:latest
FROM ubuntu:latest

# install packages via script
COPY install-packages.sh .
RUN chmod +x install-packages.sh
RUN ./install-packages.sh

# copy files to container
COPY . /hdp
WORKDIR /hdp

# install pythonrequirements
RUN chmod +x install-deps.sh
RUN ./install-deps.sh

# expose the port 8080
EXPOSE 8000

CMD ["gunicorn", "-b 0.0.0.0:8000", "app:app"]