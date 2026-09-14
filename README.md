# 🔗 SmartLink: Simple URL Shortener Using Flask, MySQL & Docker

**SmartLink** is a simple and lightweight URL shortening web application that converts long URLs into short and easy-to-share links.

The project is developed using the **Flask framework in Python** for the backend, **HTML and CSS** for the frontend, **MySQL** for storing URL data, and **Docker** for containerization.

SmartLink is developed as an **MVP (Minimum Viable Product)** to understand how a URL shortener works and how frontend, backend, database, and Docker technologies work together in a web application.

- **Simple URL Shortening:** Convert long URLs into short and easy-to-share links.
- **Automatic Redirection:** Open a generated short URL and automatically redirect to the original URL.
- **Database Storage:** Store original URLs and their generated short codes in MySQL.
- **Docker Support:** Run the application and MySQL database using Docker and Docker Compose.
- **Simple User Interface:** A clean and lightweight HTML and CSS interface for creating short URLs.

---

# 👨🏻‍💻 Built With

This SmartLink project is built with the following technologies:

1. **Front-End:** HTML and CSS
2. **Back-End:** Python and Flask
3. **Database:** MySQL
4. **Database Connector:** MySQL Connector for Python
5. **Containerization:** Docker and Docker Compose
6. **Web Server:** Gunicorn
7. **Configuration:** Python-dotenv
8. **Deployment:** Render
9. **Version Control:** Git and GitHub

---

# 🤩 Features of the Project

## A. Users Can

1. Enter a long URL.
2. Generate a short URL.
3. View the generated short URL.
4. Open the generated short URL.
5. Automatically redirect to the original URL.

---

## B. URL Shortening

SmartLink generates a short code for the provided URL and stores the URL information in the MySQL database.

For example:

**Original URL:**

```text
https://www.google.com
```

**Short URL:**

```text
http://localhost:5000/abc123
```

When the user opens the generated short URL, SmartLink finds the corresponding original URL from the database and automatically redirects the user to the original website.

---

# 📁 Project Structure

```text
smart-link/
│
├── mysql/
│   └── init.sql
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .env
├── Dockerfile
├── app.py
├── config.py
├── database.py
├── docker-compose.yml
├── models.py
├── render.yaml
└── requirements.txt
```

### Main Files and Folders

| File/Folder | Purpose |
|---|---|
| `app.py` | Main Flask application and URL-shortening and redirection routes |
| `config.py` | Application configuration |
| `database.py` | Database connection and database-related operations |
| `models.py` | Data models used by the application |
| `templates/index.html` | Frontend HTML page |
| `static/style.css` | Frontend styling |
| `mysql/init.sql` | MySQL database initialization |
| `Dockerfile` | Docker configuration for the application |
| `docker-compose.yml` | Configuration for running the application and MySQL services |
| `render.yaml` | Deployment configuration |
| `requirements.txt` | Python dependencies |
| `.env` | Environment variables and configuration |

---

# ⚙️ How to Install and Run this Project?

## Pre-Requisites

Before running the SmartLink project, make sure the following are installed:

1. Install **Git**
2. Install **Python**
3. Install **pip**
4. Install **MySQL** if running the database locally
5. Install **Docker Desktop** if running the project using Docker

---

# 📥 Installation

## 1. Clone This Project

Clone the SmartLink repository:

```bash
git clone https://github.com/sreenidhi123221/smart-link.git
```

Then enter the project directory:

```bash
cd smart-link
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment.

### For Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### For macOS/Linux

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

---

## 3. Install Requirements

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

# 🔐 4. Configure Environment Variables

SmartLink uses environment variables for application and database configuration.

Create a `.env` file in the project root directory if it does not already exist.

Example:

```env
DB_HOST=localhost
DB_PORT=3307
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=smartlink
```

> **Note:** Use the database username, password, database name, and port that match your local or Docker MySQL configuration.

> **Security:** Do not upload real database passwords, API keys, or other sensitive information to GitHub.

---

# 🗄️ 5. Database Setup

SmartLink uses **MySQL** to store URL information.

The project contains the following database initialization file:

```text
mysql/init.sql
```

This file contains the SQL required to initialize the database.

If you are running MySQL locally, make sure the MySQL server is running and the required database is available.

If you are using Docker Compose, the MySQL service can be started along with the application.

---

# ▶️ 6. Run the Project Locally

After activating the virtual environment and configuring the database, run:

```bash
python app.py
```

The Flask application will start.

Open the application in your browser:

```text
http://localhost:5000
```

---

# 🐳 7. Run Using Docker

SmartLink also supports Docker.

Make sure **Docker Desktop** is installed and running.

From the project root directory, run:

```bash
docker compose up --build
```

This builds the application image and starts the services configured in `docker-compose.yml`.

After the containers are running, open:

```text
http://localhost:5000
```

To stop the containers:

```bash
docker compose down
```

---

# 🔗 How SmartLink Works?

The basic working flow of SmartLink is:

```text
User enters a long URL
        ↓
Flask receives the URL
        ↓
A short code is generated
        ↓
URL and short code are stored in MySQL
        ↓
Short URL is displayed to the user
        ↓
User opens the short URL
        ↓
Flask searches for the short code
        ↓
Original URL is retrieved
        ↓
User is redirected to the original URL
```

---

# 🐳 Docker Support

SmartLink uses Docker to provide a consistent environment for running the application.

The project includes:

- `Dockerfile` – Builds the application container.
- `docker-compose.yml` – Configures and manages the application and MySQL services.
- `mysql/init.sql` – Initializes the MySQL database.

Docker Compose allows the application and database to be started together using:

```bash
docker compose up --build
```

---

# 🚀 Future Improvements

The current version of SmartLink is an MVP. The project can be extended in the future with features such as:

1. **User Authentication** – Allow users to create accounts and manage their shortened URLs.
2. **Custom Short URLs** – Allow users to choose their own short codes.
3. **URL Expiration** – Automatically expire links after a specified period.
4. **Click Analytics** – Track the number of times a shortened URL is accessed.
5. **QR Code Generation** – Generate QR codes for shortened URLs.
6. **User Dashboard** – Allow users to view and manage their shortened URLs.
7. **URL Management** – Add options to edit or delete shortened URLs.
8. **Improved URL Validation** – Validate URLs before generating short links.

---

# 👩🏻‍💻 Author

**Yaso Sreenidhi Yadala**

- GitHub: [sreenidhi123221](https://github.com/sreenidhi123221)
- LinkedIn: [Yaso Sreenidhi Yadala](https://www.linkedin.com/in/yasosreenidhi-yadala-02b111320/)

---

⭐ If you find this project useful for learning **Flask, MySQL, Docker, and URL-shortening concepts**, consider giving the repository a star.
