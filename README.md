![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# Description

This application works with enterprise data provided
by [scrap_UA-Kyiv](https://github.com/ValeriyFromUA/scrap_UA-Kyiv.git) in a PostgreSQL database. The following data is
included in the database:

- Company name
- Company type (Internet shop, LLC, veterinary clinic, etc.)
- Areas of activity
- Address
- Phone numbers
- Email addresses
- Website
- Short description

## Usage

To use the application, follow these steps:

1. Clone the code using `git clone ...` or download it as a zip archive.
2. Create a virtual environment and install dependencies (use Poetry).
3. Create a `.env` file based on the `env_example` file and enter your own data.
4. Run the server.

**Important**:
The application uses the database from [scrap_UA-Kyiv](https://github.com/ValeriyFromUA/scrap_UA-Kyiv.git) and does not
generate its own. Make sure that the same database is used in the settings of both applications. The reason for this is
that the scraper can run for a very long time (depending on the amount of information), so it needs to be run before the
Django application starts.
