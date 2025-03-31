![banner](https://res.cloudinary.com/dloadb2bx/image/upload/v1706241280/dailydiet_sehpbr.png)

# Daily Diet API

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300000f.svg?style=for-the-badge&logo=mysql&logoColor=white)

## Overview

The Daily Diet API is a project developed as part of the Python Developer formation at Rocketseat. The primary objective is to provide users with a tool to manage their diet effectively. Built using Flask and MySQL, the API allows users to create accounts, log in, create meals, view meals in the database, and access personalized information about their diet progress.

## Features

### 1. Authentication

- **Create Account:** Users can register and create their accounts securely.
- **Login:** Secure authentication to access personalized features.

### 2. Meal Management

- **Create Meal:** Users can add details of their meals to the database.
- **View All Meals:** Access a list of all meals stored in the database.
- **Edit and Delete Meals:** Users have the ability to modify or remove meals they created.

### 3. User Insights

- **User Meals List:** Retrieve a personalized list of meals based on the user.
- **Diet Statistics:** Track the number of meals on the diet and the success percentage.

## Application Rules

- It should be possible to register a meal with the following information:
  - Name
  - Description
  - Date and Time
  - Compliance with the diet (Yes/No)
- It should be possible to edit a meal, allowing changes to all the above data:
  - Name
  - Description
  - Date and Time
  - Compliance with the diet (Yes/No)
- It should be possible to delete a meal.
- It should be possible to list all meals for a user.
- It should be possible to view a single meal.
- The information should be stored in a database:
  - Utilizes MySQL for persistent storage.

## Getting Started

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/daily-diet-api.git
   ```
2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure Database:**
   - Set up a MySQL database and update the configuration in `config.py`.
4. **Run the Application:**
   ```sh
   python app.py
   ```
5. **Access API:**
   - Open `http://localhost:5000` in your browser or API client.

