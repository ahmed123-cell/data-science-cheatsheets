# Dev Commands Cheat Sheet

Git, GitHub CLI, Docker, Ruff, and uv: the commands you'll use most.

---

## Git

### Setup & config
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list                      # show all settings
git init                               # new repo in current folder
git clone <url>                        # clone a repo
git clone --depth 1 <url>              # shallow clone (latest commit only)
```

### Everyday workflow
```bash
git status                             # what changed
git diff                               # unstaged changes
git diff --staged                      # staged changes
git add <file>                         # stage a file
git add -p                             # stage interactively, hunk by hunk
git add .                              # stage everything
git commit -m "message"                # commit staged changes
git commit -am "message"               # stage tracked files + commit
git commit --amend                     # edit the last commit
git push                               # push current branch
git pull                               # fetch + merge
git pull --rebase                      # fetch + rebase
git fetch --all --prune                # update remotes, drop deleted branches
```

### Branching
```bash
git branch                             # list local branches
git branch -a                          # list all (incl. remote)
git switch <branch>                    # switch branch
git switch -c <new-branch>             # create + switch
git branch -d <branch>                 # delete (merged)
git branch -D <branch>                 # force delete
git branch -m <new-name>               # rename current branch
git push -u origin <branch>            # push + set upstream
git push origin --delete <branch>      # delete remote branch
```

### Merging & rebasing
```bash
git merge <branch>                     # merge into current branch
git merge --abort                      # cancel a conflicted merge
git rebase <branch>                    # replay commits on top of branch
git rebase -i HEAD~3                   # interactive: squash/reword last 3
git rebase --continue                  # after resolving conflicts
git rebase --abort
git cherry-pick <commit>               # apply a single commit
```

### History & inspection
```bash
git log --oneline --graph --decorate --all
git log -p <file>                      # history of a file with diffs
git log --author="name" --since="2 weeks ago"
git show <commit>                      # details of a commit
git blame <file>                       # who changed each line
git reflog                             # history of HEAD (recovery lifeline)
git grep "text"                        # search tracked files
git bisect start / good / bad          # binary-search for a bug
```

### Undoing things
```bash
git restore <file>                     # discard unstaged changes
git restore --staged <file>            # unstage a file
git reset --soft HEAD~1                # undo commit, keep changes staged
git reset --mixed HEAD~1               # undo commit, keep changes unstaged
git reset --hard HEAD~1                # undo commit, DISCARD changes
git revert <commit>                    # new commit that undoes a commit
git clean -fd                          # delete untracked files/dirs
git clean -nd                          # dry run first!
```

### Stash
```bash
git stash                              # shelve changes
git stash -u                           # include untracked files
git stash list
git stash pop                          # apply + remove latest
git stash apply stash@{1}              # apply without removing
git stash drop stash@{0}
```

### Remotes & tags
```bash
git remote -v
git remote add origin <url>
git remote set-url origin <url>
git tag v1.0.0                         # lightweight tag
git tag -a v1.0.0 -m "Release 1.0.0"   # annotated tag
git push --tags
```

### .gitignore tips
```bash
git rm --cached <file>                 # stop tracking a file, keep it on disk
git check-ignore -v <file>             # why is this file ignored?
```

---

## GitHub CLI (`gh`)

### Auth & repos
```bash
gh auth login
gh auth status
gh repo create my-repo --public --source=. --push
gh repo clone owner/repo
gh repo fork --clone
gh repo view --web                     # open repo in browser
```

### Pull requests
```bash
gh pr create --fill                    # create PR from commits
gh pr create --title "T" --body "B" --draft
gh pr list
gh pr view 123 --web
gh pr checkout 123                     # check out a PR locally
gh pr diff 123
gh pr review 123 --approve
gh pr review 123 --request-changes -b "comment"
gh pr merge 123 --squash --delete-branch
gh pr status
```

### Issues
```bash
gh issue create --title "Bug" --body "Details" --label bug
gh issue list --assignee @me
gh issue view 45
gh issue close 45
gh issue comment 45 -b "Working on it"
```

### Actions, releases, misc
```bash
gh run list                            # recent workflow runs
gh run view <run-id> --log
gh run watch                           # live-follow a run
gh run rerun <run-id> --failed
gh workflow run <workflow.yml>
gh release create v1.0.0 --generate-notes
gh release download v1.0.0
gh gist create file.txt --public
gh api repos/owner/repo/issues         # raw API call
gh alias set co 'pr checkout'          # custom shortcuts
```

---

## Docker

### Images
```bash
docker build -t myapp:latest .
docker build -f Dockerfile.dev -t myapp:dev .
docker build --no-cache -t myapp .
docker images                          # list images
docker pull nginx:latest
docker tag myapp:latest user/myapp:1.0
docker push user/myapp:1.0
docker rmi <image>                     # remove image
docker image prune -a                  # remove all unused images
docker history <image>                 # inspect layers
```

### Running containers
```bash
docker run -d --name web -p 8080:80 nginx          # detached, port map
docker run -it --rm ubuntu bash                    # interactive, auto-remove
docker run -v $(pwd):/app -w /app node:22 npm test # bind mount + workdir
docker run -e KEY=value --env-file .env myapp      # environment vars
docker run --network mynet myapp
docker run --restart unless-stopped myapp
docker run --cpus 2 --memory 512m myapp           # resource limits
```

### Managing containers
```bash
docker ps                              # running containers
docker ps -a                           # all containers
docker stop <name>
docker start <name>
docker restart <name>
docker rm <name>                       # remove stopped container
docker rm -f <name>                    # force remove
docker logs -f --tail 100 <name>       # follow logs
docker exec -it <name> bash            # shell into running container
docker cp <name>:/path/file ./file     # copy out of container
docker inspect <name>
docker stats                           # live resource usage
docker top <name>                      # processes in container
```

### Volumes & networks
```bash
docker volume create mydata
docker volume ls
docker volume rm mydata
docker network create mynet
docker network ls
docker network inspect mynet
```

### Docker Compose
```bash
docker compose up -d                   # start services in background
docker compose up --build              # rebuild images first
docker compose down                    # stop + remove containers
docker compose down -v                 # also remove volumes
docker compose ps
docker compose logs -f <service>
docker compose exec <service> bash
docker compose run --rm <service> <cmd>
docker compose pull
docker compose config                  # validate + view merged config
```

### Cleanup
```bash
docker system df                       # disk usage
docker system prune                    # remove unused data
docker system prune -a --volumes       # aggressive cleanup
docker container prune
```

### Dockerfile snippet (Python + uv)
```dockerfile
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
CMD ["uv", "run", "python", "main.py"]
```

---

## Ruff

### Linting
```bash
ruff check                             # lint current directory
ruff check path/to/file.py
ruff check --fix                       # auto-fix safe issues
ruff check --fix --unsafe-fixes        # include unsafe fixes
ruff check --watch                     # re-run on file changes
ruff check --select E,F,I              # only these rule sets
ruff check --ignore E501               # ignore a rule
ruff check --diff                      # show fixes without applying
ruff check --output-format=github      # CI-friendly annotations
ruff check --statistics                # count violations per rule
ruff check --add-noqa                  # add `# noqa` to existing violations
```

### Formatting
```bash
ruff format                            # format current directory
ruff format path/to/file.py
ruff format --check                    # exit non-zero if changes needed
ruff format --diff                     # preview changes
```

### Info & discovery
```bash
ruff rule F401                         # explain a rule
ruff linter                            # list available linters
ruff config                            # list config options
ruff config lint.select                # explain one option
ruff clean                             # clear the cache
ruff --version
```

### Typical `pyproject.toml` config
```toml
[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]   # pycodestyle, pyflakes, isort, pyupgrade, bugbear, simplify
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["S101"]

[tool.ruff.format]
quote-style = "double"
```

### Inline suppression
```python
import os  # noqa: F401
# ruff: noqa: E501        <- whole file
```

---

## uv

### Projects
```bash
uv init my-project                     # new project
uv init --lib my-lib                   # new library layout
uv add requests                        # add dependency
uv add "fastapi>=0.110" --dev          # dev dependency
uv add --group lint ruff               # named dependency group
uv remove requests
uv sync                                # install from lockfile into .venv
uv sync --frozen                       # don't update the lockfile
uv lock                                # update uv.lock
uv lock --upgrade-package requests     # upgrade one package
uv tree                                # dependency tree
uv run python main.py                  # run in the project env
uv run pytest
uv run --with rich python script.py    # one-off extra dependency
uv build                               # build sdist + wheel
uv publish
```

### Python versions
```bash
uv python list                         # available + installed versions
uv python install 3.12
uv python install 3.11 3.13
uv python pin 3.12                     # write .python-version
uv python find
uv venv --python 3.12                  # venv with a specific version
```

### Virtual environments & pip interface
```bash
uv venv                                # create .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
uv pip install requests
uv pip install -r requirements.txt
uv pip install -e .                    # editable install
uv pip uninstall requests
uv pip list
uv pip freeze > requirements.txt
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt
```

### Tools (like pipx)
```bash
uvx ruff check                         # run a tool without installing
uv tool run black .                    # same as uvx
uv tool install ruff                   # install globally
uv tool list
uv tool upgrade --all
uv tool uninstall ruff
```

### Scripts (PEP 723)
```bash
uv init --script script.py --python 3.12
uv add --script script.py requests     # records deps inline
uv run script.py
```

### Maintenance
```bash
uv self update
uv cache clean
uv cache dir
uv export --format requirements-txt > requirements.txt
```

---

## Handy combos

```bash
# Pre-commit routine for a Python project
uv run ruff check --fix && uv run ruff format && uv run pytest

# Start a new project end to end
uv init app && cd app && git init && uv add --dev ruff pytest
gh repo create app --private --source=. --push

# Clean up merged local branches
git branch --merged main | grep -v "main" | xargs git branch -d

# Stop & remove every container
docker rm -f $(docker ps -aq)
```