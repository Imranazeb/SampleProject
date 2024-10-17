@echo off

REM Check if Docker and docker-compose are installed
docker --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker is not installed. Please install Docker and try again.
    exit /b 1
    pause
)
docker-compose --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker Compose is not installed. Please install Docker Compose and try again.
    exit /b 1
    pause
)

REM Check if Docker Engine is running
docker info >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker Engine is not running. Please start Docker Desktop and try again.
    pause
    exit /b 1
)


REM Start the Docker containers
docker-compose -f local.yml up --build -d --remove-orphans
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to start Docker containers. Please check the logs for more information.
    exit /b 1
    pause
)

REM Check if the app is running on localhost:8080 by making an HTTP request
echo Waiting for the application to become available at http://localhost:8080...

REM Set initial variables
set /a attempts=0
set /a max_attempts=60

:check_app
timeout /t 1 >nul
curl -s http://localhost:8080 >nul
IF %ERRORLEVEL% EQU 0 (
    GOTO start_app
)

REM Increment attempt counter
set /a attempts+=1

REM Check if the maximum number of attempts has been reached
IF %attempts% GEQ %max_attempts% (
    echo Application failed to start within 1 minute.
    exit /b 1
    pause
)

echo Application is not up yet, retrying... (%attempts%/%max_attempts%)
GOTO check_app

REM If the app is up, print success message and open in browser
:start_app
echo.
echo Application is now running! You can access it here: http://localhost:8080
echo You may close this window. The application will continue to run in the background.

start http://localhost:8080

pause

