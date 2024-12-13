#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mamar_bank.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mamar_bank.settings")
    
    # Get the PORT from the environment variables, default to 8000 for local development
    port = os.environ.get("PORT", "8000")
    
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])
