
📚 NPTEL/Swayam Assignment Auto-Filler
This Python script automates the login process, course navigation, and assignment filling on the Swayam NPTEL portal. It uses Selenium to simulate a browser session, automatically logs in via Microsoft credentials, navigates to a selected course and week, and fills assignment answers provided by the user.

⚙️ Features
✅ Logs in with Microsoft account via Swayam

✅ Automatically navigates to your "My Courses" page

✅ Enters the first enrolled course

✅ Expands selected week's content

✅ Detects available assignments

✅ Takes user input for assignment answers

✅ Autofills and optionally submits the assignment

🧠 Requirements
Python 3.6+

Google Chrome

ChromeDriver (compatible with your Chrome version)

Python Packages
Install dependencies using pip:

bash
Copy
Edit
pip install selenium python-dotenv
🔐 Environment Variables
Create a .env file in the same directory with your Microsoft-linked Swayam credentials:

dotenv
Copy
Edit
SWAYAM_EMAIL=your_email@example.com
SWAYAM_PASSWORD=your_password
⚠️ Do not share your .env file or commit it to version control!

🚀 How to Run
Clone the repository or save the script as nptel_scraper.py.

Ensure ChromeDriver is installed and available in your system PATH.

Add your credentials to the .env file.

Run the script:

bash
Copy
Edit
python nptel_scraper.py
Follow the prompts:

Choose the week you want to work on.

Enter your answers as comma-separated values (e.g., 1,2,3,1,4).

🧪 Example Walkthrough
User sees:

yaml
Copy
Edit
Detected Weeks:
Week 0: Week 1 - Introduction
Week 1: Week 2 - Advanced Topics

Enter the Week number you want to open (e.g., 0 for Week 0):
User inputs: 1
Then prompted for answers: 1,2,3,4,1

The script auto-selects those options and attempts submission.

🔐 Login Notes
The script logs in using the Microsoft login button on Swayam.

If your login flow is different (e.g., Google or Swayam direct), the script would need to be adjusted.

🛠 Troubleshooting
Chrome opens and closes instantly: Make sure your ChromeDriver version matches your Chrome browser.

Stuck on login page: Double-check credentials in your .env file.

No assignments detected: Ensure you have assignments published in the selected week.

📎 Limitations
This script currently supports multiple-choice questions only.

Answers must be manually provided as option numbers (1-based indexing).

Only works for the first course listed under "My Courses".

Assumes a static page structure—if Swayam updates their UI, this might break.

📌 TODOs / Improvements
 Add support for selecting different courses

 Add headless mode

 Add support for saving answers locally

 Add error reporting/logging to file

🤝 Contributing
Pull requests and feature ideas are welcome! Make sure to keep credentials out of any commits.

⚠️ Disclaimer
This script is intended for educational and personal use only. Automating assignment submissions may violate the platform's terms of service. Use responsibly.

🧑‍💻 Author
Made with ❤️ by GopiKrishna
