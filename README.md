# Instics is a simple Flask-based library management app

## For now the app has web-first interface and I will soon make it responsive on mobile as well.

## To use this project:

1. Clone the repo into your computer. Run the command `git clone https://github.com/kiplimock/instics.git` in terminal.

2. Create a database called `instics` in your postgres installation. Run `CREATE DATABASE instics;` in psql. I assume you already have the postgresql installation. Ensure your settings match with the ones in the DATABASE URI.

3. Create the tables by running `db.create_all()` in the python shell. Ensure you start the python shell in the project root folder and import the `db` variable first.

4. To start the application, enter `python app.py` and press return/enter in terminal. Make sure you run the command in the right directory.

5. Visit `http://127.0.0.1:5000` in your browser and check out the interface.

6. Have fun. Explore!
