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
The API will use simple token-based authentication without expiration.
Tokens will be easily guessable or hard-coded strings.

### Injection Flaws
The user data endpoint will be susceptible to SQL injection.

### Security Misconfiguration
Default usernames and passwords will be used.
Misconfigured headers will leak information.

## Tools and Technologies
Language: Python 3.x
Framework: Flask, due to its simplicity for demonstration purposes.
Database: SQLite, for ease of setup and use.
Docker: For containerization of the application and database.
Docker Compose: To manage the multi-container setup.

## Deployment
TODO: docker-compose setup
TODO: full deployment instructions

## Exploits
TODO: A set of scripts to automate attacks like SQL injection will be provided.
TODO: Instructions for manual exploitation will also be included.
