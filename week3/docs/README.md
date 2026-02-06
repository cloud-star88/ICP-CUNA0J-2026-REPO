# Week 3 Project – Data & APIs Integration

## Overview
This Week 3 project focuses on learning how to connect a Python application to an external system using APIs.  
The aim was not to build anything complex, but to understand **how applications communicate with data sources outside themselves** and how to handle errors properly.

For this project, I chose to integrate with a public external API.

---

## Project Objective
The main objectives of this project were to:
- Connect a Python application to an external API
- Retrieve and process data returned from the API
- Handle possible errors gracefully
- Document the entire process clearly

---

## Tools and Technologies Used
- **Python** – programming language
- **Requests** – HTTP client library
- **Random User API** – public REST API providing sample user data

---

```
ICP-CUNA0J-2026-REPO/

├── week3/
|   ├── docs/
│       ├── documentation.md
|       ├── sample-text.txt
|       └── README.md
|
│   ├── screenshots/
│       ├── 01-http-client-install.png
|       ├── 02-verify-http-client-install.png
|       ├── 03-app-connected-to-api.png
|       └── 04-backend-code-display.png
|
│   ├── src/
│       └── app.py
|
├── LICENSE
└── README.md
```


## Why I Chose an External API
I chose to work with an external API instead of a database to keep the project simple and focused on integration.

The Random User API was selected because:
- It is free and public
- No authentication or API key is required
- It returns structured JSON data
- It is reliable and beginner-friendly

---

## Project Structure
The project contains the following files:

- `app.py` – main Python application
- `README.md` – project explanation
- `documentation.md` – detailed step-by-step documentation
- `sample-output.txt` – example output from the program
- `screenshot.png` – proof of successful execution

---

## How the Application Works
1. The application sends an HTTP GET request to the Random User API.
2. The API responds with user data in JSON format.
3. The application converts the JSON response into Python data.
4. Specific user details such as name, email, and country are extracted.
5. The extracted information is displayed in a readable format.
6. Errors such as network issues or invalid responses are handled gracefully.

---

## Error Handling
The application includes basic error handling to ensure it does not crash when something goes wrong.

It handles:
- Network connection errors
- Request timeouts
- Invalid API responses
- Unexpected runtime errors

This makes the application more reliable and closer to real-world usage.

---

## How to Run the Project
1. Install the required dependency:
```bash 
python -m pip install requests
```

## 2 Run the application:
python app.py

When successful, the program prints user details retrieved from the API.

## What I Learned

- Through this project, I learned:
- How APIs work and how applications communicate using HTTP
- The importance of handling errors gracefully
- How API integration relates to backend and cloud systems

## Conclusion
This project helped me build a strong foundation in data and API integration.
It represents an important step toward understanding backend development, cloud engineering, and how real-world systems communicate with external services.