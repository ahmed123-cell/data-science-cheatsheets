# Docker

## What is Docker?

**Docker** is an open-source platform that enables developers to **build, ship, and run** applications inside lightweight, portable **containers**.

It solves one of the biggest problems in software development:  
**"It works on my machine"** — by packaging the application with all its dependencies, libraries, and configurations into a single unit that runs consistently everywhere (laptop, server, cloud, etc.).

Docker uses **containerization** technology, which is much more efficient than traditional virtual machines.

---

## Docker vs Virtual Machine

| Feature                  | **Docker (Containers)**                  | **Virtual Machine (VM)**                |
|--------------------------|------------------------------------------|-----------------------------------------|
| **Size**                 | Small (MBs)                             | Large (GBs)                            |
| **Startup Time**         | Very fast (seconds)                     | Slow (minutes)                         |
| **Performance**          | Near native speed                       | Slower due to overhead                 |
| **Resource Usage**       | Low (shares host OS)                    | High (each VM has its own OS)          |
| **Isolation**            | Process and user level                  | Full hardware-level                    |
| **Portability**          | Extremely portable                      | Portable but heavier                   |
| **Number of instances**  | Can run dozens on one server            | Limited by resources                   |

**Main Difference**:  
Containers **share the host operating system**, while Virtual Machines run a **complete guest operating system**. This makes Docker much lighter, faster, and more efficient.

---

## Docker Images, Containers, and Volumes

- **Docker Image**  
  A **read-only template** or blueprint used to create containers.  
  It contains the application code, runtime (e.g., Python, Node.js), libraries, and system tools.  
  Images are built using a `Dockerfile` and can be stored locally or in a registry like **Docker Hub**.

- **Docker Container**  
  A **runnable instance** of an image.  
  When you run an image, Docker creates a container — an isolated environment where the application actually runs.  
  You can start, stop, restart, or delete containers.

- **Docker Volumes**  
  A way to **persist data** outside of a container.  
  Containers are ephemeral (data is lost when the container is removed). Volumes allow you to store data on the host machine so it survives even if the container is deleted or recreated.  
  Very useful for databases, logs, and configuration files.

**Simple Analogy**:
- **Image** = Cake recipe
- **Container** = Actual cake baked from the recipe
- **Volume** = The plate where you keep the cake (persists after eating)

---

## Popular Docker Commands

### Basic Commands

```bash
# Check Docker version
docker --version

# Pull an image from Docker Hub
docker pull nginx

# List all images
docker images

# Run a container
docker run nginx

# Run in detached mode (background)
docker run -d nginx

# Run with port mapping
docker run -d -p 8080:80 nginx

# List running containers
docker ps

# List all containers (running + stopped)
docker ps -a
```

### Managing Containers

```bash
# Stop a running container
docker stop <container_id_or_name>

# Start a stopped container
docker start <container_id_or_name>

# Restart a container
docker restart <container_id_or_name>

# Remove a container
docker rm <container_id_or_name>

# Remove all stopped containers
docker rm $(docker ps -a -q)
```

### Images & Cleanup

```bash
# Build an image from Dockerfile
docker build -t myapp:latest .

# Tag an image
docker tag myapp:latest myusername/myapp:latest

# Push image to Docker Hub
docker push myusername/myapp:latest

# Remove an image
docker rmi nginx
```

### Volumes & Logs

```bash
# Create and use a volume
docker run -d -v mydata:/app/data nginx

# View container logs
docker logs <container_id>

# Follow logs in real-time
docker logs -f <container_id>

# Enter inside a running container
docker exec -it <container_id> bash
```

### Docker Compose (Multi-container)

```bash
# Start services defined in docker-compose.yml
docker compose up -d

# Stop services
docker compose down
```

---