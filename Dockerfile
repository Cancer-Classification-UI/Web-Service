# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim
WORKDIR /usr/src/app


# Copy local code to the container image.
COPY . ./

# Install dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposed for SSL through aws
EXPOSE 443

# Run the the service on startup
CMD ["python","main.py"]