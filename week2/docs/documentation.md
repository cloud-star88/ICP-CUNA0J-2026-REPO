# Week 2 Project Documentation
# Backend Application

## Overview
This project is a simple backend application designed to demonstrate core programming concepts using Python.
It manages tasks in memory and allows users to add, view, and remove tasks through a command-line interface.

The focus of this project is logic, data structures, and clean code, not deployment or databases.

## Purpose of the Project

The goal of this project is to:
Understand how backend logic works
Practice using basic data structures
Write clean and readable code
Build confidence with core programming fundamentals

## Application Responsibilities
The backend application handles the following:

Task Creation – Accepts user input and stores tasks in memory

Task Retrieval – Displays all stored tasks in an ordered list

Task Deletion – Removes a selected task from the list

Program Control – Keeps the application running until the user exits

## Technology Used
Programming Language: Python
Interface: Command Line (CLI)

## Data Handling
Tasks are stored using a list data structure

Each task exists only while the application is running

No database or external storage is used

This approach keeps the project focused on core concepts.

## Core Concepts Demonstrated

Variables

Lists (data structures)

Functions

Loops

Conditional statements

Error handling (basic)

Clean and readable syntax

## How the Application Works

The application displays a menu of options.

The user selects an action.

The backend logic processes the request.

Data is updated in memory.

The menu repeats until the user chooses to exit.

## How to Run the Application

Open a terminal in the project directory.

Run the Python file:

python todo.py
Follow the on-screen instructions.
Limitations
No persistent storage (data resets on exit)
No user authentication
No graphical or web interface
These limitations are intentional to maintain focus on core backend logic.

## Conclusion

This project demonstrates the fundamentals of building a backend application, focusing on data structures, logic flow, and clean code practices.
It serves as a strong foundation for future backend, DevOps, and cloud-based projects.

In Week 2, I built a simple backend application using Python to strengthen my understanding of core programming concepts. The project focused on implementing backend logic and managing data using basic data structures.

## Challenges faced:
- Understanding how to structure backend logic using functions and loops.
- App refused to run until i used `#!/usr/bin/env python` at the top of the script 
- Managing in-memory data and realizing data resets when the app exits.
- Handling user input errors (invalid choices or task numbers).
- after re-structuring my week 1 folder and updating my week 2 i pushed to git but realized every update i made didn't reflect except the python file in week2.
- when i entered `git add .` this message poped up `warning: in the working copy of 'README.md', CRLF will be replaced by LF the next time Git touches it` so, i resolved this by running this: git config --global core.autocrlf true




Debugging file path and execution issues in the terminal.

Controlling program flow so menus and actions behave correctly.
Structuring my folder and files. I used ctrl + , then typeed "file explorer" and chose from the options listed.

## What I Learned

- Organizing data using lists
- Writing clean, reusable functions
- Using loops and conditionals for logic control
- Building a simple interactive backend application

## Week 2 Technical Summary

In Week 2, I built a simple backend application using Python to strengthen my understanding of core programming concepts. The project focused on implementing backend logic and managing data using basic data structures.

The application handles task management through a command-line interface, allowing users to add, view, and remove tasks. Data is stored in memory using a list, emphasizing how backend systems organize and manipulate data without relying on databases or external services.

Key concepts practiced include variables, lists, functions, loops, and conditional statements, with an emphasis on clean syntax and readable code. The project reinforced logical thinking, control flow, and the importance of simplicity when building foundational backend systems.

This week established a strong foundation for more advanced topics such as persistent storage, APIs, automation, and cloud-based deployments in later stages.