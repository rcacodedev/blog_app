# Blog App

This is a project of a blog application developed with Django.

## Description

The blog application allows users to view posts, add comments and replies to comments, and search for posts by title.

## Features

- Listing of posts on the home page.
- Detail of each post with the option to add comments and replies.
- Categorization of posts.
- Search for posts by title.
- Dedicated pages for different categories of posts.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`.
5. Perform database migrations: `python manage.py migrate`.
6. Load initial data (optional): `python manage.py loaddata initial_data`.
7. Run the server: `python manage.py runserver`.

## Usage

Once the server is running, you can access the application through your web browser at [http://localhost:8000/](http://localhost:8000/).

## Contribution

Contributions are welcome. If you would like to contribute to this project, follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/new-feature`).
5. Create a new pull request.

## License

This project is licensed under the [MIT License](LICENSE).

