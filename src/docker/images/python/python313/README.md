# python313

This project sets up python v3.13 using Docker container.

## Spark Cluster set-up

1. **Navigate to the python313 directory**

   ```bash
   cd src/docker/images/python/python313
   ```

2. **Run Docker Daemon**
   Run Docker Desktop to start Docker Daemon

3. **Build Docker Image**

   ```bash
   docker build -t python313 .
   ```

4. **Start Docker Image**

   ```bash
   docker run python313
   ```
