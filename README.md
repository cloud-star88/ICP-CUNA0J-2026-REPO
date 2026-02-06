# ICP-CUNA0J-2026-REPO
Repository for tasks and projects completed during the DevOps Internship Program at InternCareerPath

**Week 1:** Foundation & Setup
**Project:** Environment & Hello World
**Description:**
   **Install tools.** Build a basic proof of concept.
   **Tech Stack:** Domain Standard Tools

## Scope
Week 1 focuses on environment setup, tool installation, and a Hello World proof of concept.

## Contents
- Environment setup details
- Tools and verification steps
- Hello World proof explanation
- Onboarding summary
- Official references

# Repository Structure

```
ICP-CUNA0J-2026-REPO/

├── week1/
|   ├── docs/
│       ├── documentation.md
|       └── README.md
|
│   ├── screenshots/
│       ├── azure-CLI.png
|       ├── docker.png
|       ├── git-version.png
|       ├── github-connection.png
|       ├── hello-world-screenshot.png
|       ├── os-and-bash.png
|       └── vs-code.png
│    
│   ├── src/
│       └── hello_world.sh 
|
├── LICENSE
└── README.md
```

**Environment setup details**
system and tools used for Week 1 

**Operating System**
- OS: Windows 11

**Terminal & Shell**
- Bash 
I used bash to run commands, executing scripts, and managing files.

**Development Tools**
- Editor: Visual Studio Code

**Validation**
The setup was verified by checking tool versions and successfully running a Hello World Bash script, confirming the environment is ready for further DevOps tasks.

# Tools and verification steps

## Git & GitHub
- Purpose: Version control
- Verification: `git --version`

## Linux Terminal
- Purpose: Command-line operations
- Verification: `uname -a`

## VS Code
- Purpose: Code editor
- Verification: `code --version`

## Docker
- Purpose: Containerization
- Verification: `docker --version`

## Azure CLI
- Purpose: Cloud interaction
- Verification: `az version`
Verification was done using version checks and basic commands.

# Hello World proof explanation

## Objective
To confirm that the environment and tools are working correctly.

## Implementation
A Bash script was created to print a simple message.

## Script
- File: `hello_world.sh`

## Execution
The script was executed successfully using Bash.

## Output
- Output file: `hello-world-output.txt`
- Screenshot provided as visual confirmation

## Evidence
- Tool versions recorded
- Script execution output captured
- Screenshots saved 

# Onboarding summary
- Weekly task submissions
- Proper documentation
- Use of GitHub for tracking progress
- LinkedIn profile update to highlight progress and key learnings

## References and official documentation

- Git Documentation – https://git-scm.com/docs
- Docker Documentation – https://docs.docker.com
- Azure CLI Documentation – https://learn.microsoft.com/cli/azure
- Bash Scripting Guide – https://www.gnu.org/software/bash/manual/

---------------------------------------------------------------------------------------

# Week 2: Core Concepts
**Project:** Simple Application
**Description:** Implement core logic and data structures.
**Tech Stack:** Core Language - python
**Hints:** Focus on clean syntax

## Overview
This project is a simple backend application designed to demonstrate core programming concepts using Python.
It manages tasks in memory and allows users to add, view, and remove tasks through a command-line interface.

The focus of this project is logic, data structures, and clean code, not deployment or databases.

---

## Project Objective
The objective of this project is to strengthen understanding of:
- Core programming fundamentals
- Backend logic flow
- Data handling without databases
- Writing clean and readable code

---

# Repository Structure

```
ICP-CUNA0J-2026-REPO/

├── week2/
|   ├── docs/
│       ├── documentation.md
|       └── README.md
|
│   ├── screenshots/
│       ├── menu.png
|       ├── add-task.png
|       ├── view-task.png
|       ├── remove-task.png
|       └── exit-app.png
│    
│   ├── src/
│       └── todo.py 
|
├── LICENSE
└── README.md
```


## Application Functionality
The backend application handles the following operations:
- Add tasks
- View all tasks
- Remove tasks
- Exit the application

All operations are performed in memory using a simple data structure.

---

## Technology Used
Programming Language: Python
Interface: Command Line (CLI)

---

## Data Handling
- Tasks are stored using a **list data structure**
- Data exists only while the application is running
- No database or external storage is used

This approach keeps the focus on **core concepts**, not infrastructure.

---

## How the Application Works
1. The program displays a menu of options.
2. The user selects an action.
3. Backend logic processes the request.
4. The in-memory data is updated.
5. The menu repeats until the user exits.

---

## Core Concepts Demonstrated
- Variables
- Lists (data structures)
- Functions
- Loops
- Conditional statements
- Basic error handling
- Clean syntax and logical code structure

## How to Run
1. Open a terminal in the project directory.
2. Run the application:
   ```bash
   python todo.py

--------------------------------------------------------------------------------------

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
│    
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
- How to fetch and process JSON data in Python
- The importance of handling errors gracefully
- How API integration relates to backend and cloud systems

## Conclusion
This project helped me build a strong foundation in data and API integration.
It represents an important step toward understanding backend development, cloud engineering, and how real-world systems communicate with external services.