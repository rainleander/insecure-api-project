# Insecure API Project
## Objective
This project aims to create an intentionally vulnerable API for educational purposes. The API will demonstrate common security flaws identified by the [OWASP Top Ten](https://owasp.org/www-project-top-ten/) list, allowing users to learn about API vulnerabilities through hands-on experience.

## Scope
The API will be simple, mimicking a real-world application, and will include the following:

- Authentication endpoint
- User data retrieval and manipulation endpoint
- Administrative functions endpoint

## Security Flaw to Implement
### Injection Flaws
- The user data endpoint will be susceptible to SQL injection.

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

Please ensure that [Docker and Docker Compose](https://docs.docker.com/get-docker/) are installed and running on your system. You can check by running `docker -v` and `docker-compose -v` to confirm the installation. If they are not installed, please install them before proceeding. Run `docker ps` to confirm status.

In the root directory of the cloned repository, start the application by running:

```bash
docker-compose up --build
```

This command builds the Docker image for the Flask application and starts it. The `--build` flag ensures that the image is built using the most up-to-date version of your application code.

### Step 3: Interact with the API

After running the `docker-compose up` command, your Flask application should be running and accessible at `http://0.0.0.0:8080`. Use `curl`, Postman, or any HTTP client to interact with the API.

Here are some example `curl` commands to interact with the API:

```bash
# Test if the app is accessible
curl http://127.0.0.1:8080/
```
This will return 'Hello, World!'; you can also test if the app is accessible by opening the URL http://0.0.0.0:8080/ in your browser.  

```bash
# Fetch user details (Potentially vulnerable to SQL injection)
curl http://0.0.0.0:8080/users/1
```
This command will return the following output: 
```
{
  "message": "User Data Retrieval Endpoint"
}
```

### Step 4: Explore the Vulnerabilities

Run SQLMap on the user endpoint with a risk and severity level.

`sqlmap -u "http://0.0.0.0:8080/users/admin" --data="username=admin" --method=POST --dbms=SQLite  --risk=3 --level=5`

The script does several types of tests:

```
[15:19:30] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[15:19:30] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[15:19:30] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[15:19:30] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[15:19:30] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[15:19:30] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[15:19:30] [INFO] testing 'Generic inline queries'
[15:19:30] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[15:19:30] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[15:19:30] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[15:19:30] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[15:19:30] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[15:19:30] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[15:19:30] [INFO] testing 'Oracle AND time-based blind'
```

This script returns that `all tested parameters do not appear to be injectable`. There are a few possible reasons for that. 

- **SQLMap's Testing Strategy**: SQLMap follows a set of predefined testing strategies and payloads to detect SQL injection vulnerabilities. It doesn't necessarily cover all possible variations of SQL injection and may not detect vulnerabilities if they deviate from its testing patterns.

- **Test Parameters**: SQLMap relies on the parameters provided in the URL or form data for testing. If the parameters are not easily identifiable as injection points, SQLMap may not detect them as potential vulnerabilities.

- **Custom Code**: SQLMap is a general-purpose tool that may not fully understand the specifics of the `app.py`. It might not recognize the SQL injection vulnerability in the Flask application because it's looking for more common patterns or vulnerabilities.

- **Mitigation Measures**: In the original prompt `sqlmap -u "http://0.0.0.0:8080/users/admin" -v`, I am using SQLAlchemy and parameterized queries to mitigate SQL injection vulnerabilities. These measures are effective in preventing SQL injection attacks. SQLMap may not detect these vulnerabilities if it cannot find any exploitable SQL injection points.

- **False Negatives**: False negatives (where SQLMap doesn't detect a vulnerability) can happen. SQLMap might require specific circumstances or payloads to trigger an injection, and if those conditions are not met during its automated testing, it may report no vulnerabilities.

It's important to note that even if SQLMap doesn't detect a vulnerability, it doesn't necessarily mean the code is secure. Manual code review and thorough testing are essential for identifying and addressing potential security issues in your application. While parameterized queries and ORM libraries like SQLAlchemy help prevent SQL injection, other security considerations, such as input validation, authentication, and authorization, should also be part of a security strategy.

Testing for SQL injection in an API typically involves sending malicious SQL payloads to the API endpoints and observing the responses to see if they reveal any indication of SQL injection vulnerabilities. You can use various tools and methods for this purpose. Here are some bash commands to test for SQL injection vulnerabilities in your Flask API:

**Note:** This command is for educational purposes and should only be used on systems and applications you have permission to test.

Curl with SQL Injection Payloads (Manual Testing)

Use `curl` to manually send requests with SQL injection payloads to the API endpoints. Replace `<username>` with a payload that may trigger SQL injection.

```bash
# Test SQL injection on /users/<username> endpoint
curl -X POST "http://0.0.0.0:8080/users/admin'%20OR%20'1'='1" -d
```

This payload attempts to inject a SQL condition that continuously evaluates to true (`' OR '1'='1`) and comments out the rest of the query with `--`.

Remember that testing for vulnerabilities should be done responsibly, and you should only test systems and applications for which you have explicit permission. Additionally, using these techniques for educational and security improvement purposes and not for malicious intent is essential.

### Step 5: Shutdown and Cleanup

When you are done exploring the API, you can stop and remove the Docker containers by running:

```bash
docker-compose down
```

This command stops the services and removes the containers. To remove the containers along with their associated volumes, run `docker-compose down -v`.

**Security Warning**: So that you know, this API contains intentional vulnerabilities for educational purposes. Please don't deploy this API in a production environment or expose it to an untrusted network.

### Step 6: Provide Feedback (Optional)

If you have any suggestions or feedback on the project, consider opening an issue or a pull request in the GitHub repository to share your thoughts with the repository maintainer.
