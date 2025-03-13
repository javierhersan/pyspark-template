# python313jupyter

This project sets up python v3.13 using Docker container.

## Spark Cluster set-up

1. **Navigate to the python313jupyter directory**

   ```bash
   cd src/docker/images/python/python313jupyter
   ```

2. **Run Docker Daemon**
   Run Docker Desktop to start Docker Daemon

3. **Build Docker Image**

   ```bash
   docker build -t python313jupyter .
   ```

4. **Start Docker Image**

   ```bash
   docker run -p 8888:8888 python313jupyter
   ```
