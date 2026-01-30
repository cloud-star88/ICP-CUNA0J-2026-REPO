# Week 2 Project Documentation – Backend Application

## Overview
This project is a simple backend application designed to demonstrate core programming concepts using Python.
It manages tasks in memory and allows users to add, view, and remove tasks through a command-line interface.

## Purpose of the Project

The goal of this project is to:
Understand how backend logic works
Practice using basic data structures
Write clean and readable code
Build confidence with core programming fundamentals

**Step 1: Project Setup**

I created a simple backend application using Python to practice core programming concepts. The application runs in the terminal and manages tasks in memory.

**Step 2: Data Structure**

I initialized an empty list to store tasks. This list holds all task entries while the application is running.

**Step 3: Menu Logic**

I implemented a menu function to display available actions: add task, view tasks, remove task, and exit.

**Step 4: Add Task Functionality**

I wrote a function that collects user input and appends new tasks to the list.

**Step 5: View Tasks Functionality**

I implemented logic to display all stored tasks, handling cases where no tasks exist.

**Step 6: Remove Task Functionality**

I added functionality to remove a task by its number, including basic error handling for invalid input.

**Step 7: Program Flow Control**

I used a continuous loop to keep the application running until the user chooses to exit.

**Step 8: Error Handling**

I handled common user input errors to prevent the application from crashing.

**Step 9: Execution**

I structured the program with a main entry point to ensure clean execution when the script runs.

## Conclusion

In Week 2, I built a simple backend application using Python. This project strengthened my understanding of core programming concepts, it demonstrates the fundamentals of building a backend application, focusing on data structures, logic flow, and clean code practices. 

## Challenges faced:
- Understanding how to structure backend logic using functions and loops.
- App refused to run until `#!/usr/bin/env python` was used at the top of the script. 
- Managing in-memory data and realizing data resets when the app exits.
- Difficulty pushing all changes to github at once. i had to cd into the verious folders and had to push each content seperately. 
- On entering `git add .` a message poped out `warning: in the working copy of 'README.md', CRLF will be replaced by LF the next time Git touches it.` i resolved this by running: git config --global core.autocrlf true

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