@echo off
echo Setting up LMS environment...
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
echo Setup complete! Run: python manage.py runserver
pause