# 📚 LibraryOS

A lightweight, containerized Library Management System designed to handle inventory operations for books, magazines, and digital media. Built with a Python/Flask backend and a responsive Bootstrap frontend.

## 🚀 Overview

LibraryOS is a full CRUD (Create, Read, Update, Delete) web application that demonstrates clear separation of concerns, utilizing an Object-Oriented backend architecture to manage data flow between a Flask server and an SQLite database. The entire application is containerized with Docker, ensuring consistent deployment across any environment.

## ✨ Key Features

* **Object-Oriented Design:** Utilizes Python classes and a dedicated `LibraryManager` to handle database transactions and data validation safely.
* **Dynamic User Interface:** Built with Bootstrap 5. Features dynamic form rendering (JavaScript), interactive search, and modal-based safeguards for destructive actions.
* **Containerized Workflows:** Fully Dockerized using a lightweight Python-slim image for rapid, portable, and reliable deployment.
* **Data Persistence:** Integrated SQLite3 database with custom row factories for clean dictionary-like data handling.

## 🛠️ Tech Stack

* **Backend:** Python 3.13.8, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Bootstrap Icons
* **DevOps:** Docker, Git

## 📦 Run it Locally (Docker)

The easiest way to run LibraryOS is via Docker. Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YusanNim21/LibraryOS.git](https://github.com/YusanNim21/LibraryOS.git)
   cd LibraryOS