from flask import Flask, render_template, request, redirect
from database import get_db_connection
import random
import string


app = Flask(__name__)


# Generate random short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Create Short URL
@app.route('/shorten', methods=['POST'])
def shorten():

    long_url = request.form.get("long_url")

    short_code = generate_short_code()

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO links (original_url, short_code)
    VALUES (%s, %s)
    """

    cursor.execute(query, (long_url, short_code))

    connection.commit()

    cursor.close()
    connection.close()


    short_url = f"{request.host_url}{short_code}"


    return render_template(
        "index.html",
        short_url=short_url
    )


# Redirect short URL
@app.route('/<short_code>')
def redirect_url(short_code):

    connection = get_db_connection()
    cursor = connection.cursor()


    query = """
    SELECT original_url 
    FROM links
    WHERE short_code = %s
    """


    cursor.execute(query, (short_code,))

    result = cursor.fetchone()


    cursor.close()
    connection.close()


    if result:
        return redirect(result[0])


    return "Short URL not found"



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )