# pyweek-32

The official cat dev repository for PyWeek32

---

## Dev Installation

1. Clone the repository:

- `git clone https://github.com/cat-dev-group/pyweek-32.git` or `git clone git@github.com:cat-dev-group/pyweek-32.git`

- Github CLI: `gh repo clone cat-dev-group/pyweek-32`

2. `cd pyweek-32/` and create a new branch: `git checkout -b <name of your new local branch> main` or `git switch -c <name of your new local branch> main`

3. Using poetry:

Install poetry: `pip install -U poetry`

```sh
# Install the project and development dependencies
poetry install

# Install the pre-commit hooks
poetry run task pre-commit

poetry run task lint

# Run the source code
poetry run task start
```

4. Using Docker (Recommended):

Install Docker: Follow the [official documentation](https://docs.docker.com/get-docker/)

Install docker-compose: `pip install -U docker-compose`

```sh
# Make sure docker service is running before executing the following command.
docker-compose up --build

# Use -d flag for detached mode
docker-compose up

# Use ctrl+C if not in detached mode
docker-compose stop

# Use -v (shorthand for --volumes) flag to remove volumes
docker-compose down
```

5. Lint and format your code using `poetry run task lint` and push the changes `git push -u origin <name of your remote branch>`
