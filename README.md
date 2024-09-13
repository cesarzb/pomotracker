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

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables by creating a `.env` file:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/mydb
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Navigate to the homepage and log in or create a new account.
- Create new Pomodoro sessions using the "Create new Pomodoro" button.
- View Pomodoro sessions on the calendar.
- Click on a Pomodoro in the calendar to view and edit or delete it.

## License

This project is licensed under the MIT License.
