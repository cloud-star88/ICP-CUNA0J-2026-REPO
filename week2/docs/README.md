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

