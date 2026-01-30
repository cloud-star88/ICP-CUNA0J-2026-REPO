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
