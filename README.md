# Pomodoro Tracker App

A web-based Pomodoro tracking app built with Django, Bootstrap, and FullCalendar. This app allows users to create, view, edit, and delete Pomodoro sessions and displays them on a calendar.

## Features

- **User Authentication**: Sign up, log in, and manage your Pomodoro sessions.
- **Pomodoro Sessions**: Create, update, and delete Pomodoro sessions with start and end times.
- **FullCalendar Integration**: View your Pomodoro sessions on a calendar. The number of Pomodoros per day is displayed, and clicking on a specific Pomodoro shows it's detailed page.
- **Responsive UI**: Built with Bootstrap for a clean, responsive user interface.

## Technologies Used

- **Django**
- **Bootstrap**
- **FullCalendar**
- **PostgreSQL**

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd pomodoro-tracker
   ```

2. Create database volume in project directory:
    ```bash
   mkdir /data/db
   ```

2. Setup correct permissions (sometimes it doesn't work without it):
    ```bash
   sudo chmod 777 data/db
   ```

3. Set up environment variables by creating a `.env` file:

   ```env
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432

    TEST_DB_NAME=test_mydb
    TEST_DB_USER=postgres
    TEST_DB_PASSWORD=postgres
    TEST_DB_HOST=db
    TEST_DB_PORT=5432

    SECRET_KEY=super_secret-hello
   ```

4. Start docker compose:

   ```bash
   docker compose up
   ```

5. If you want to run the tests you can run:

   ```bash
   docker compose run web python manage.py test
   ```

## Usage

- Navigate to the homepage and log in or create a new account.
- Create new Pomodoro sessions using the "Create new Pomodoro" button.
- View Pomodoro sessions on the calendar.
- Click on a Pomodoro in the calendar to view and edit or delete it.

## License

This project is licensed under the MIT License.
