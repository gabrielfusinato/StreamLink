# StreamLink - URL Shortener

A simple and efficient URL shortener built with **Python**, **Streamlit**, and **Supabase**.  
This project was developed to practice **database integration (PostgreSQL)**, API communication, and web interface management.

---

## 🛠️ Setup

Install the necessary dependencies to connect to the database and run the UI:

```bash
pip install streamlit supabase
```

## 🚀 Execution

To start the application, run:

```bash
streamlit run app.py
```

---

## 🧠 Project Logic & Study Goals

The core of this project is the communication between a Python backend and a cloud database. The logic covers:

* **Database Schema:** Setting up a PostgreSQL table in Supabase with Primary Key constraints.
* **CRUD Operations:** Implementing methods to **Create** (store new URLs) and **Read** (fetch long URLs) from the database.
* **Cloud Integration:** Using the `supabase-py` client to handle authentication and data flow.
* **Dynamic Redirection:** Managing Streamlit's state to redirect users from a `tinyAlias` to the destination `longUrl`.

---

## 💾 Database Setup (SQL)

Run this command in your **Supabase SQL Editor** to initialize the project:

```sql
CREATE TABLE url (
  tinyAlias VARCHAR(10) PRIMARY KEY,
  longUrl TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---
> **Developed for study purposes:** Python Integration + Database Management + Web UI.