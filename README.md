# Instagram Login Checker

This Python script allows you to check the validity of <a href="https://logmeonce.com/resources/how-to-find-out-your-instagram-password-while-logged-in/">Instagram login checker</a> credentials (username and password) using Instagram's API. It is intended for educational and personal use only. Please ensure that you use this script responsibly and in accordance with ethical guidelines.

## Prerequisites

- Python 3.x
- `requests` library

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install requests
   ```
3. Open the `instagram_login.py` file and provide the Instagram username and password in the appropriate variables.
4. Run the script by executing the following command in your terminal or command prompt:
   ```
   python instagram_login.py
   ```
5. The script will make a POST request to the Instagram login API and display the result.
   - If the status is "ok" and the authentication is successful, it will print "User and password matching."
   - If the status is not "ok" or the authentication fails, it will print "No password or user are correct" along with the response details.

## Ethical Use

- This script should only be used for legitimate and authorized purposes, such as testing your own Instagram account credentials.
- Do not use this script for hacking, phishing, or any malicious activities.
- Respect the privacy and security of others. Do not attempt to access or use someone else's Instagram account without their explicit permission.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Make sure to read and understand the content of the README.md file and modify it further if necessary to reflect the appropriate ethical use of the code.
