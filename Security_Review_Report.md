Security Review Report

Project 2: Secure Coding Review

Internship: CodeAlpha Cyber Security
Created by: Isha Suhas Mahangade

1. Introduction

Secure Coding Review is a cybersecurity project that identifies security mistakes in Python programs and improves them using secure coding practices.

2. Security Issues Identified

1. Hardcoded Password: Password is directly written in the source code.
2. Password Exposure: Sensitive password information is displayed on the screen.
3. No Input Validation: The program does not properly check user input.
4. Weak Password Policy: Short passwords are accepted.

3. Security Improvements

1. Avoid displaying passwords.
2. Use a minimum password length of 8 characters.
3. Check login details before allowing access.
4. Validate user input.
5. Never use real passwords in demonstration programs.

4. Comparison

Insecure Code| Improved Code
Displays password| Does not display password
Accepts short passwords| Checks minimum length
Basic login checking| Improved login checking

5. Conclusion

Through this project, I learned how to identify common security vulnerabilities in Python code and improve basic login security. This project helped me understand the importance of secure coding practices.
