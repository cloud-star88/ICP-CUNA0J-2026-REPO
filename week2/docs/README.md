# Week 2: Core Concepts
**Project:** Simple Application
**Description:** Implement core logic and data structures.
**Tech Stack:** Core Language - python
**Hints:** Focus on clean syntax

## Overview
In Week 2, I built a simple **backend application** using Python to strengthen my understanding of **core programming concepts**.  
The focus of this project was on backend logic, data structures, and clean syntax rather than UI, databases, or deployment.

---

## Project Goal
The main goal of this project was to:
- Practice core programming fundamentals
- Understand how backend logic works
- Learn how data is stored and manipulated in memory
- Write clean, readable, and structured code

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

## Application Description
The backend application manages tasks through a command-line interface.  
It allows users to:
- Add tasks
- View tasks
- Remove tasks
- Exit the application

All operations are handled in memory using a simple data structure.

---

## Technology Used
- **Language:** Python  
- **Interface:** Command Line (CLI)

---

## Data Structure Used
- A **list** is used to store tasks
- Tasks exist only while the application is running
- No database or external storage is used

This approach keeps the project focused on understanding fundamentals.

---

## How the Application Works (Step-by-Step)
1. The application starts and displays a menu.
2. The user selects an option.
3. Backend logic processes the request.
4. Data in memory is updated accordingly.
5. The menu repeats until the user chooses to exit.

---

## Core Concepts Demonstrated
- Variables
- Lists (data structures)
- Functions
- Loops
- Conditional statements
- Basic error handling
- Clean and readable syntax

---

## Challenges Faced
- Managing program flow between menu options
- Handling invalid user input without crashing
- Understanding in-memory data behavior
- Debugging file path and execution issues

---

## Limitations
- No persistent data storage
- No database integration
- No web interface

These limitations were intentional and aligned with the learning objectives of Week 2.

---

## Key Takeaway
This project reinforced the importance of **strong foundations** in backend development.  
Understanding core logic and data handling is essential before moving on to advanced backend, DevOps, or cloud-based systems.

---

## How to Run the Application
```bash
python todo.py