# db-lab-autmation-hax

This program allows you to create a summary of your codezinger programs and
generate a SQL file so you can use it however you want.

Don't ask why we felt the need to create this. 🙂

## Installation

- clone or download this repository \
  clone: \
  `git clone https://github.com/Ya-s-h/db-lab-autmation-hax.git`
- install requirements \
  `pip install -r requirements.txt`\
  or \
  `python -m pip install -r requirements.txt`
- Download the WebDriver for Chrome to use with selenium \
   Direct link for chrome:
  [link](https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.107/)
  \
   Direct link to Selenium docs (in case you want to use it with any other
  browser apart from Chrome):
  [Selenium Docs](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/#quick-reference)
- Unzip the downloaded file and keep the `.exe` file in the same folder as this program.
## Usage

- Run the program with `python main.py`
- Codezinger login page would be opened. Enter your credentials and login
- Wait for the chrome browser to close
- a file (`dataFile_0.sql`) will be saved where you have cloned the repository

Now you have the huuuge data that woudl've been boring to collect manually, all
thanks to computer automation ✌ Feel free to modify the generated `.sql` file

**If you face any issue feel free to [open an issue](https://github.com/Ya-s-h/db-lab-autmation-hax/issues/new) in the repository**
## License

This project is licensed under GNU GPLv3
