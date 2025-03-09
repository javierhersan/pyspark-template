# PySpark Cluster

This project sets up a Spark cluster using Docker containers. It allows you to run python distributed data processing tasks using Apache Spark and pyspark library.

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

3. **Build Docker Image**

   ```bash
   $ docker build -t spark-image .
   ```

4. **Build the Docker Image**
   Navigate to the `spark/docker` directory and build the Docker image:

   ```bash
   $ cd spark/docker
   $ docker-compose build
   ```

5. **Start the Spark Cluster**
   Use Docker Compose to start the cluster:

   ```bash
   docker-compose up
   ```

6. **Access the Spark UI**
   The Spark UI can be accessed at `http://localhost:8080`.

   ![alt text](./docs/images/spark-ui.png)

## Usage

To run your PySpark application, modify the `src/main.py` file with your data processing logic. You can use the utility functions defined in `src/utils/helper.py` to assist with data loading and transformation.

## Configuration

The `docker/docker-compose.yml` file defines the services for the Spark cluster. You can adjust the number of replicas and other configurations as needed.

## Requirements

Make sure to install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.
