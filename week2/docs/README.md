# Week 2 Project: Backend Application

## Overview
This project is a simple `backend application` built using Python to demonstrate `core programming concepts`.  
It focuses on implementing backend logic and managing data using basic data structures through a command-line interface.

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

## Tech Stack
- **Language:** Python
- **Interface:** Bash CLI

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

## How to Run
1. Open a terminal in the project directory.
2. Run the application:
   ```bash
   python todo.py

## Core Concepts Demonstrated
- Variables
- Lists (data structures)
- Functions
- Loops
- Conditional statements
- Basic error handling
- Clean syntax and logical code structure