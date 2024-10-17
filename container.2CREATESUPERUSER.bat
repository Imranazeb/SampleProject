echo off

REM Check if Docker Engine is running
docker info >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker Engine is not running. Please start Docker Desktop and try again.
    pause
    exit /b 1
)

REM Create superuser for the Django application

docker-compose -f local.yml run --rm django python manage.py createsuperuser

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to create superuser.
    exit /b 1
    pause
)

echo Sucess...
pause
