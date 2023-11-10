# Insecure API Project
## Objective
This project aims to create an intentionally vulnerable API for educational purposes. The API will demonstrate common security flaws identified by the OWASP Top Ten list, allowing users to learn about API vulnerabilities through hands-on experience.

## Scope
The API will be simple, mimicking a real-world application, and will include the following:

- Authentication endpoint
- User data retrieval and manipulation endpoint
- Administrative functions endpoint

## Security Flaws to Implement
### Broken User Authentication
- The API will use simple token-based authentication without expiration.
- Tokens will be easily guessable or hard-coded strings.

### Injection Flaws
- The user data endpoint will be susceptible to SQL injection.

### Security Misconfiguration
- Default usernames and passwords will be used.
- Misconfigured headers will leak information.

## Tools and Technologies
- Language: Python 3.x
- Framework: Flask, due to its simplicity for demonstration purposes.
- Database: SQLite, for ease of setup and use.
- Docker: For containerization of the application and database.
- Docker Compose: To manage the multi-container setup.

## Deployment
To implement and run the insecure API from the provided GitHub repository, follow these instructions:

### Step 1: Clone the GitHub Repository

Open a terminal and run the following command to clone the repository:

```bash
git clone https://github.com/rainleander/insecure-api-project.git
```

Navigate to the cloned repository directory:

```bash
cd insecure-api-project
```

### Step 2: Build and Run with Docker Compose

Ensure that [Docker and Docker Compose](https://docs.docker.com/get-docker/) are installed and running on your system. You can check by running `docker -v` and `docker-compose -v` to confirm installation. If they are not installed, please install them before proceeding. Run `docker ps` to confirm status.

In the root directory of the cloned repository, start the application by running:

```bash
docker-compose up --build
```

This command builds the Docker image for the Flask application and starts it. The `--build` flag ensures that the image is built using the most up-to-date version of your application code.

### Step 3: Interact with the API

After running the `docker-compose up` command, your Flask application should be running and accessible at `http://localhost:5001`. Use `curl`, Postman, or any HTTP client to interact with the API.

Here are some example `curl` commands to interact with the API:

```bash
# Login (This is insecure and for demonstration purposes)
curl -H "Content-Type: application/json" -d '{"username":"admin", "password":"password"}' http://localhost:5001/login

# Fetch user details (Potentially vulnerable to SQL injection)
curl http://localhost:5001/users/1
```

TODO: Resolve [curl: (52) Empty reply from server](https://github.com/rainleander/insecure-api-project/issues/1)

### Step 4: Explore the Vulnerabilities

- TODO: A set of scripts to automate attacks like SQL injection will be provided.
- TODO: Instructions for manual exploitation will also be included.

### Step 5: Shutdown and Cleanup

When you are done exploring the API, you can stop and remove the Docker containers by running:

```bash
docker-compose down
```

This command stops the services and removes the containers. To remove the containers along with their associated volumes, run `docker-compose down -v`.

**Security Warning**: Keep in mind that this API contains intentional vulnerabilities for educational purposes. Never deploy this API in a production environment or expose it to an untrusted network.

### Step 6: Provide Feedback (Optional)

If you have any suggestions or feedback on the project, consider opening an issue or a pull request in the GitHub repository to share your thoughts with the repository maintainer.
