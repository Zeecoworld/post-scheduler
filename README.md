# Django Post Scheduler

A robust Django-based post scheduling service that allows users to schedule and manage content across multiple platforms. This project aims to provide functionality similar to popular task scheduling services.

## Features

- Schedule posts for multiple social media platforms
- Recurring post scheduling with customizable intervals
- Draft management and post preview
- Queue management and scheduling conflicts resolution


## Prerequisites

- Python 3.8+
- Django 4.2+
- PostgreSQL 13+
- Redis (for task queue)
- Celery (for background tasks)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-post-scheduler.git
cd django-post-scheduler
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Start Celery worker:
```bash
celery -A post_scheduler worker -l info
```

## Project Structure

```
postschedulingproject/
├── manage.py
├── requirements.txt
├── post_scheduler/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── postapp
│   ├── models/
│   ├── views/
│   ├── tasks/
│   ├── templates/
│   └── tests/
└── static/
    ├── css/
    ├── js/
    └── img/
```

## Configuration

### Database Setup

The project uses PostgreSQL. Update your database configuration in settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Redis Configuration

Configure Redis for Celery task queue:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```


## Testing

Run the test suite:

```bash
python manage.py test
```

For coverage report:

```bash
coverage run manage.py test
coverage report
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django documentation
- Celery project
- PostgreSQL
- Redis

## Support

For support, please create an issue in the GitHub repository or contact the maintenance team at support@example.com.
