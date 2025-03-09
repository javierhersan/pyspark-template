# PySpark Cluster

This project sets up a Spark cluster using Docker containers. It allows you to run python distributed data processing tasks using Apache Spark and pyspark library.

![alt text](./docs/images/spark-cluster.png)

## Project Structure

```
pyspark-template
├── pyspark
│   ├── src
|   |  ├── main.py
│   |  └── utils
│   |  └── helper.py
│   └── requirements.txt
├── spark
|   └── docker
│       ├── Dockerfile
│       └── docker-compose.yml
└── README.md
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   $ git clone <repository-url>
   $ cd pyspark-template
   ```

2. **Run Docker Daemon**
   Run Docker Desktop to start Docker Daemon

3. **Access spark/docker folder**

   ```bash
   $ cd spark/docker
   ```

4. **Build Docker Image**

   ```bash
   $ docker build -t spark-image:3.4.0 .
   ```

5. **Build the Docker Image**
   Navigate to the `spark/docker` directory and build the Docker image:

   ```bash
   $ docker-compose build
   ```

6. **Start the Spark Cluster**
   Use Docker Compose to start the cluster:

   ```bash
   docker-compose up
   ```

7. **Access the Spark UI**
   The Spark UI can be accessed at `http://localhost:9090`.

   ![alt text](./docs/images/spark-ui.png)

## Usage: Docker Client

```bash
cd spark/client
docker build -t spark-client:latest .
docker run --network=cluster_default --name spark-client-app
-e HOSTNAME=spark-client --rm spark-client:latest
```

## Usage: Local client

Access to pyspark folder:

```console
$ cd pyspark
```

List python versions:

```console
$ py --list
```

Use a specific python version:

```console
$ py -3.13 <command>
```

Create python virtual environment:

```console
$ py -m venv .venv
```

Activate python virtual environment:

```console
$ .venv\scripts\activate
```

Update pip package installer

```console
$ pip3 install --upgrade pip
```

Add your requirements to "requirements.txt" file.

Install the requirements:

```console
$ python -m pip install -r requirements.txt
```

Select your .venv as Python Interpreter in VSCode to enable code linting with Pylance. Click Ctrl+Shift+P and type "Python: Select Interpreter" and select you ".venv" python executable.

Install JAVA and Apache Hadoop and set JAVA_HOME environment variable.

To run your PySpark application, modify the `src/main.py` file with your data processing logic. You can use the utility functions defined in `src/utils/helper.py` to assist with data loading and transformation.

```console
$ py main.py
```

docker build -t spark-client:latest .

docker run --network=cluster_default --name spark-client-app
-e HOSTNAME=spark-client --rm spark-client:latest

## License

This project is licensed under the MIT License.
