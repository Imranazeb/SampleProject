echo off

REM Check if Docker Engine is running
docker info >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker Engine is not running. Please start Docker Desktop and try again.
    pause
    exit /b 1
)

REM Stop the Docker containers

docker-compose -f local.yml down -v

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to stop Docker containers. Please check the logs for more information.
    exit /b 1
    pause
)

docker-compose -f local.yml down --rmi all

echo Removing Docker volumes, networks, and system. This may take a few moments...

docker volume prune -f

docker network prune -f

docker system prune -f

echo Docker containers have been stopped and removed successfully.

pause