# Week 4 Project Documentation – Optimization

## Project Overview
In Week 4, the focus of this project was optimization. The goal was to improve the performance, security, and readability of an existing Python To-Do application without changing its core functionality.

This involved analyzing the original code, identifying weak points, and refactoring the application to make it cleaner, safer, and easier to maintain.

---

## Step 1: Review the Existing Application
I started by reviewing the original version of the To-Do application. The app allowed users to:
- Add tasks
- View tasks
- Remove tasks
- Exit the program

Although the app worked correctly, I noticed areas that could be improved in terms of structure, input handling, and code clarity.

---

## Step 2: Identify Optimization Targets
I focused on three key optimization areas:

### Performance
- The application relied on a global `tasks` list, which can become difficult to manage as an application grows.
- Some functions depended on shared state instead of clear inputs.

### Security
- User input was accepted directly without validation.
- Empty tasks could be added.
- Invalid inputs were not always handled clearly.

### Readability
- Some functions handled multiple responsibilities.
- The flow of data was not always obvious.
- The code could be clearer for another developer to understand.

---

## Step 3: Profiling and Analysis
Rather than focusing on execution speed, I profiled the application logically by observing:
- Frequently executed functions
- Areas where user input could cause errors
- Code sections that were harder to understand or extend

This helped me decide where refactoring would have the most impact.

---

## Step 4: Refactor to Remove Global State
I removed the global `tasks` list and instead passed it explicitly to functions that needed it.  
This made the application more predictable, easier to test, and safer to extend in the future.

---

## Step 5: Improve Input Validation and Security
I added validation to:
- Prevent empty tasks from being added
- Ensure menu choices were properly handled
- Prevent invalid task numbers during removal

Clear error messages were added to guide the user when incorrect input is entered.

---

## Step 6: Refactor for Readability
I refactored the code to ensure:
- Each function has a single responsibility
- Function names clearly describe what they do
- The control flow in the main loop is easy to follow

Comments were added where necessary to explain important logic.

---

## Step 7: Test the Optimized Application
After refactoring, I tested all features:
- Adding tasks
- Viewing tasks
- Removing tasks
- Handling invalid input
- Exiting the application

All features worked as expected with improved clarity and safety.

---

## Final Outcome
The optimized version of the application:
- Is easier to read and maintain
- Handles user input more safely
- Avoids unnecessary global state
- Reflects better engineering practices

This project reinforced the importance of writing clean, secure, and maintainable code.
