# Week 3: Intermediate Integration
**Project:** Data & APIs
**Description:** Connect to database or external APIs.
**Tech Stack:** DB / HTTP Client
**Hints:** Handle errors gracefully

## Project Goal
The goal of this project was to learn how to connect a Python application to an external system (an API), retrieve data, and handle possible errors without crashing the application.

This project focuses on understanding integration, not complexity.

---

## Step 1: Understanding the Task
I first clarified that I only needed to connect my application to:
- either a database, or
- an external API

To reduce complexity and focus on learning integration, I chose to work with an external public API.

---

## Step 2: Choosing the Right Tools
I selected tools that were simple and beginner-friendly:
- **Python** as the programming language
- **Requests** as the HTTP client library
- **Random User API** as the external API

Reasons for choosing this API:
- Free and public
- No authentication required
- Stable and easy to use
- Returns clean JSON data

---

## Step 3: Setting Up the Project
I created a project folder and added the following files:

- `app.py` – main application file
- `README.md` – project overview
- `documentation.md` – step-by-step documentation
- `sample-output.txt` – example program output
- `screenshot.png` – proof of successful execution

---

## Step 4: Installing Dependencies
Since the project required making HTTP requests, I installed the `requests` library using:
```bash 
python -m pip install requests
```
I verified the installation using `curl --version`to ensure it was available for use in the project.

## Step 5: Writing the Application Logic

- In app.py, I followed these steps:
- Imported the requests library
- Defined the API endpoint URL
- Created a function to handle the API request
- Sent a GET request to the API
- Converted the response from JSON into Python data
- Extracted specific user details such as name, email, and country
- Displayed the extracted information in a readable format

## Step 6: Implementing Error Handling

To meet the project requirement of handling errors gracefully, I added error handling using try and except.

**The application handles:**
- Network connection errors
- Request timeouts
- Invalid HTTP responses
- Unexpected runtime errors

This ensures the program does not crash and provides clear feedback when something goes wrong.

## Step 7: Running and Testing the Application

I ran the application from the terminal using: python app.py

When successful, the program displayed user information fetched from the API.
I repeated the test to confirm consistency and reliability.

## Step 8: Capturing Output
- After confirming the application worked correctly, I:
- Saved a sample output to sample-output.txt
- Took a screenshot of the successful execution
- These serve as proof that the integration works.

## Step 9: Final Review
- Before completing the project, I verified that:
- The application connects successfully to an external API
- Data is retrieved and displayed correctly
- Errors are handled gracefully
- The project is properly documented

## Conclusion

This project helped me understand how applications communicate with external systems using APIs. It also reinforced the importance of error handling and clear documentation, which are essential skills for backend development, cloud engineering, and system integration.