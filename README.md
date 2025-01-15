# XSS Vulnerability Lab (Flask)

This repository contains a simple Flask-based web application designed to demonstrate a **Stored Cross-Site Scripting (XSS)** vulnerability. The application allows users to post comments, and the comments are stored without proper sanitization, which can result in the execution of malicious JavaScript code.

## Overview

The application simulates a food blog where users can post comments. The vulnerability lies in the way comments are displayed on the page without sanitizing the input. As a result, it allows attackers to inject arbitrary JavaScript into the page, which is then executed by the browser of any user visiting the page.

### Vulnerability Demonstrated:

- **Stored XSS**: The vulnerability allows an attacker to inject malicious JavaScript code that gets stored on the server and executed when another user views the page.
  
### Example:
If an attacker submits the following script in the comment section:
```html
<script>alert(1)</script>

The script will be stored and executed when the page is loaded, resulting in an alert pop-up. This is the essence of Stored XSS.

### Features:
-**Comment Section**: Allows users to post comments including their name, email, website, and a comment message.

-**Vulnerable to XSS**: The comments are rendered without proper sanitization, making them vulnerable to storing and executing malicious scripts.
