# Sample Project

---

### Prerequisites:

This project requires [git](https://git-scm.com/downloads) and [docker](https://www.docker.com/). Follow the instructions in the links provided to download and install. These first set of instructions are for Windows only. If you are using Linux, please skip to Linux section.

### Installation:

---

#### Windows:

Open a terminal in the folder where you want to place this project, then enter the command:

    git clone https://github.com/Imranazeb/SampleProject

Once completed, change to the project directory using the command:

    cd SampleProject

Then either double-click on **container.1DEPLOY.bat** or use the command line to execute the file. This will initiate the container build process. Please note that, depending on the speed of your computer, it may take up to 3-5 minutes for the first-time build.

Once built successfully, a web page will open up. The webpage can be accessed any time at [http://localhost:8080](http://localhost:8080).

To create a superuser and access the admin interface, double-click on **container.2CREATESUPERUSER.bat**. This need to be done once only after creation of the container. Then, you may log in as admin using the URL [http://localhost:8080/admin](http://localhost:8080/admin).

To stop the container, double-click **container.3STOP.bat**. To restart the container, use **container.4RESTART.bat**. To completely remove the container, dependencies, volumes, and temporary files, use **container.5CLEAN.bat**.

---

#### Linux:

Git is preinstalled on most Linux distros. If you are using Linux, basic knowledge of the command line interface (CLI) is assumed. Linux can be installed on Windows by opening a terminal as an administrator and typing:

    wsl --install

You will need to install Docker **and** Docker Compose. To install the full version, follow the instructions on [www.docker.com](https://www.docker.com/). **Alternatively**, you may install a lightweight version using the command:

    sudo apt update && \
    sudo apt install docker.io docker-compose -y

To run Docker without `sudo` privileges, add your user to the Docker group using:

    sudo usermod -aG docker $USER

Once installed, you can enable Docker on startup (this is optional):

    sudo systemctl start docker && \
    sudo systemctl enable docker

Confirm the installation by running:

    docker --version

Confirm Docker Compose installation:

    docker-compose --version

A Makefile is included to allow easy shortcuts to Docker commands. Make can be installed on Ubuntu-based distros using the command:

    sudo apt update && sudo apt install make -y

Once installed, you can execute these commands:

**Build Container:**

    make build

**Stop Container:**

    make down

**Restart Container:**

    make up

**Stop container, clean everything:**

    make down-v && \
    docker-compose -f local.yml down --rmi all && \
    docker system prune -f
