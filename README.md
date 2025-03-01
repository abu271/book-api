# Django Book API
![Django Book API](https://github.com/abu271/book-api/workflows/Python%20application/badge.svg)

Simple API using Django for creating books and authors

## **Requirements**
- Docker [version `>=19.03.13`]
- Docker Compose [version `>=1.27.4`]
- git [version `>=2.9`]

## **Installation**
1. Clone the repo
2. Run `docker compose build`
3. Next run `docker compose up`
4. Access API on `http://localhost:8000/`

## **Setting up Python virtual enviroment**
1. Create a virtual environment
python -m venv venv

2. Activate the virtual environment (Linux/macOS)
source venv/bin/activate

3. Activate the virtual environment (Windows)
.\venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Deactivate the virtual environment
deactivate

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

For this project we like to follow **conventional commits**

### Summary of Conventional Commits

Conventional Commits is a specification for adding human and machine-readable meaning to commit messages. The key elements include:

- **feat**: A new feature for the user.
- **fix**: A bug fix for the user.
- **docs**: Documentation only changes.
- **lint**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **perf**: A code change that improves performance.
- **test**: Adding missing or correcting existing tests.
- **build**: Changes that affect the build system or external dependencies.
- **ci**: Changes to our CI configuration files and scripts.
- **chore**: Other changes that don't modify src or test files.
- **revert**: Reverts a previous commit.

For more details, visit the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) website.

### API Endpoints
For detailed information on the available API endpoints, please refer to the [Endpoints documentation](Endpoints.md).