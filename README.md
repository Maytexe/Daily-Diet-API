![banner](https://res.cloudinary.com/dloadb2bx/image/upload/v1706241280/dailydiet_sehpbr.png)
# Daily Diet API

## Technologies
![enter image description here](https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![enter image description here](https://camo.githubusercontent.com/63d721e5f8294c62d26a43f71778ffcccf4b23b83234050aa6ead289c3f0e987/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d7973716c2d2532333030303030662e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6d7973716c266c6f676f436f6c6f723d7768697465)

## Overview

The Daily Diet API is a project developed as part of the Python Developer formation at Rocketseat. The primary objective is to provide users with a tool to manage their diet effectively. Built using Flask and MySQL, the API allows users to create accounts, log in, create meals, view meals in the database, and access personalized information about their diet progress.

## Features

### 1. Authentication

-   **Create Account:** Users can register and create their accounts securely.
-   **Login:** Secure authentication to access personalized features.

### 2. Meal Management

-   **Create Meal:** Users can add details of their meals to the database.
-   **View All Meals:** Access a list of all meals stored in the database.
-   **Edit and Delete Meals:** Users have the ability to modify or remove meals they created.

### 3. User Insights

-   **User Meals List:** Retrieve a personalized list of meals based on the user.
-   **Diet Statistics:** Track the number of meals on the diet and the success percentage.

## Application Rules

-   It should be possible to register a meal with the following information:
    
    -   Name
    -   Description
    -   Date and Time
    -   Compliance with the diet (Yes/No)
-   It should be possible to edit a meal, allowing changes to all the above data
    
    -   Name
    -   Description
    -   Date and Time
    -   Compliance with the diet (Yes/No)
-   It should be possible to delete a meal
    
    -   Delete meal functionality implemented.
-   It should be possible to list all meals for a user
    
    -   List all meals for a user functionality implemented.
-   It should be possible to view a single meal
    
    -   View single meal functionality implemented.
-   The information should be stored in a database
    
    -   Utilizes MySQL for persistent storage.
    - 
## Getting Started

1.  **Clone the Repository:**
    
    bashCopy code
    
    `git clone https://github.com/your-username/daily-diet-api.git` 
    
2.  **Install Dependencies:**
    
    bashCopy code
    
    `pip install -r requirements.txt` 
    
3.  **Configure Database:**
    
    -   Set up a MySQL database and update the configuration in `config.py`.
4.  **Run the Application:**
    
    bashCopy code
    
    `python app.py` 
    
5.  **Access API:**
    
    -   Open `http://localhost:5000` in your browser or API client.
