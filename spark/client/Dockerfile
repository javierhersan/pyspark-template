FROM spark-image:3.4.0

# Set working directory inside the container
WORKDIR /opt/spark

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Copy the application files and requirements
COPY app /opt/spark/app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /opt/spark/app/requirements.txt

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Default command to run the PySpark job
CMD ["spark-submit", "--master", "spark://spark-master:7077", "/opt/spark/app/main.py"]
