# DjangoCon 2022 - The Django Admin Is Your Oyster
Let's push the Django Admin to its limit! We'll start out simple by speeding up search results for big models so you can traverse through 40 million row tables in seconds. We’ll continue on and gain a deeper understanding of the `clean()`, `save_model()` and the `__init__()` functions as these functions are where a lot of customization happens in the Admin. I’ll show you how to use multiple databases within one Admin website and even customize the basic Admin templates so you can have documentation right there on the CRUD pages.

By the end of the talk, you’ll have a new mindset and a toolkit for how to customize the Django Admin to your unique needs.

If you attend this talk, you’ll walk away with the following:

- An understanding of how key functions work behind the scenes
- The ability to go a step beyond the basic out-of-the-box setup and functionality
- Confidence that you can implement custom features for your team
- A sense of excitement about the Django Admin!
- A new mindset for how to customize the Django Admin to your needs

## Get the app up and running

1. Install Poetry
2. Use Poetry to install Django
3. Create superuser
> poetry run python manage.py createsuperuser
4. Seed database
5. Run the app
> poetry run python manage.py runserver
6. Navigate to `localhost:8000/admin` in your browser and login with your superuser account