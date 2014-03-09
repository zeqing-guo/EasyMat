#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyPj.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selab1.settings")
>>>>>>> 572ea2b005db99e2deeae8ad0ecb7bd12235e50c

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
