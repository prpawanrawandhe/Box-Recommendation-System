# Box Recommendation System

A Django-based web application that recommends the most suitable shipping box for a product based on its dimensions, weight, and box cost.

## Overview

The system helps warehouse teams select an appropriate shipping box for products. It checks whether a product fits inside a box, verifies the maximum weight capacity, and recommends the lowest-cost suitable box.

## Features

- Product dimension and weight input.
- Multiple box options stored in the database.
- Automatic dimension matching with rotation support.
- Maximum weight capacity validation.
- Recommends the lowest-cost suitable box.
- Displays a message when no suitable box is available.
- Responsive web interface.

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Testing:** Django TestCase

## Box Selection Logic

1. Retrieve available boxes from the database.
2. Sort product dimensions and box dimensions to support rotation.
3. Compare all three dimensions.
4. Check whether the product weight is within the box's maximum capacity.
5. Select the suitable box with the lowest cost.
6. Display the recommendation or a no-suitable-box message.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Box Recommendation System"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Running Tests

Run the automated test suite using:

```bash
python manage.py test boxes
```

## Project Documentation

- `AI_USAGE.md` – AI tools and usage documentation.
- `TEST_CASES.md` – Test scenarios and expected results.
- `TEST_OUTPUT.md` – Automated test execution output.
- `LEARNINGS.md` – Personal learning outcomes.

## Author

**Pawan Rawande**

GitHub: https://github.com/prpawrawandhe

