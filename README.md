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
```
The script will be stored and executed when the page is loaded, resulting in an alert pop-up. This is the essence of Stored XSS.

###  Features:
- **Comment Section**: Allows users to post comments including their name, email, website, and a comment message.
- **Vulnerable to XSS**: The comments are rendered without proper sanitization, making them vulnerable to storing and executing malicious scripts.

### Running the Application
Follow these steps to run the application locally:

### Prerequisites:
- Python 3 and pip installed on your system.

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/xss-lab.git
   cd xss-lab
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install dependencies(Flask):
   ```bash
   pip install flask
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
   or
   ```bash
   flask run
   ```
The application should be running at http://127.0.0.1:5000/

### Access thee application:
Open your browser and navigate to http://127.0.0.1:5000/. You can now view the blog, post comments, and see the vulnerability in action.

## How to Demonstrate the Vulnerability:
1. Go to the "Post a Comment" page by clicking on the "Post a Comment" link.
2. Enter a name, email, and a comment like this:
```html
<script>alert(1)</script>
```
3. Click Post Comment.
4. Go back to the blog page, and you will see the alert pop-up demonstrating the stored XSS vulnerability.

## Fixing the Vulnerability (Solution)
The vulnerability can be fixed by properly sanitizing user input or by escaping HTML content before rendering. This prevents malicious scripts from being executed. A potential solution would involve modifying the code to escape user inputs or using a library to sanitize HTML.

## Example of Fix:
In the blog.html file, you can modify how comments are rendered:
```html
<p>{{ comment.comment | safe }}</p>  <!-- This is vulnerable -->
```
Change to:
```html
<p>{{ comment.comment }}</p>  <!-- Proper sanitization required -->
```
Alternatively, you can use libraries like bleach to sanitize input before storing or rendering.

## Contributing
Feel free to open issues or submit pull requests for improvements. If you want to help fix the vulnerability or add additional features, your contributions are welcome!
