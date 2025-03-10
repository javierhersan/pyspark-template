FROM spark-image:3.4.0

# Set working directory inside the container
WORKDIR /opt/spark

# Install dependencies required to build Python 3.12 and SQLite
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libreadline-dev \
    libffi-dev \
    wget \
    libbz2-dev \
    liblzma-dev \
    libsqlite3-dev \ 
    && rm -rf /var/lib/apt/lists/*

# Download, compile, and install Python 3.12
RUN wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz && \
    tar -xvf Python-3.12.2.tgz && \
    cd Python-3.12.2 && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && rm -rf Python-3.12.2 Python-3.12.2.tgz

ENV PYSPARK_PYTHON=/usr/local/bin/python3.12
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/python3.12

# Ensure python3 and pip3 use Python 3.12
RUN ln -sf /usr/local/bin/python3.12 /usr/bin/python3 && \
    ln -sf /usr/local/bin/pip3.12 /usr/bin/pip3

# Upgrade pip, setuptools, and wheel
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Copy the application files and requirements
COPY . /opt/spark/app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /opt/spark/app/requirements.txt

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Expose Jupyter Notebook port
EXPOSE 8888

# Command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root"]
