# Use the official Ubuntu 25.04 base image
FROM ubuntu:25.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install PPA manage
RUN apt-get update

# Install software-properties-common software
# It allows you to easily manage your software vendor software sources.
RUN apt-get install -y software-properties-common

# Add the deadsnakes PPA to install Python 3.13
RUN add-apt-repository ppa:deadsnakes/ppa

# Install Python 3.13 and pip
RUN apt install -y python3.13 
RUN apt install -y python3-pip
RUN apt install -y python3.13-venv

# Verify the installation
RUN python3.13 --version 
RUN pip3 --version

# Install Java (required for PySpark)
RUN apt-get install -y openjdk-11-jdk

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# # Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /src

# Copy the current directory contents into the container at /srcs
COPY /src /src

# Create a virtual environment
RUN python3.13 -m venv venv

# Activate the virtual environment and install any needed packages specified in requirements.txt
RUN . venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt

# Expose the Jupyter port
EXPOSE 8888

# Start Jupyter server when the container launches
CMD ["sh", "-c", ". venv/bin/activate && jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]