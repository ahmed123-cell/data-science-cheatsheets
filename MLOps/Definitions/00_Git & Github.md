# Git & GitHub Popular Commands

## Setup & Configuration

- `git init` — Initialize a new Git repository in the current folder
- `git config --global user.name "Your Name"` — Set your username globally
- `git config --global user.email "your@email.com"` — Set your email globally
- `git config --list` — Show all Git configuration

## Basic Workflow

- `git status` — Show the current status of your working directory (modified/added files)
- `git add .` — Stage all changes (new, modified, deleted files)
- `git add <file>` — Stage a specific file
- `git commit -m "Your commit message"` — Commit the staged changes
- `git commit -am "Message"` — Add and commit tracked files in one step

## Viewing History

- `git log` — Show commit history
- `git log --oneline` — Compact one-line commit history
- `git log -p` or `git log --patch` — Show changes (diff) for each commit
- `git diff` — Show unstaged changes
- `git diff --staged` — Show staged changes

## Branching

- `git branch` — List all local branches
- `git branch <branch-name>` — Create a new branch
- `git checkout -b <branch-name>` — Create and switch to a new branch
- `git checkout <branch-name>` — Switch to an existing branch
- `git checkout <commit-hash>` — Checkout a specific commit (detached HEAD)
- `git branch -d <branch-name>` — Delete a merged branch
- `git branch -D <branch-name>` — Force delete a branch

## Merging & Rebasing

- `git merge <branch-name>` — Merge a branch into current branch
- `git rebase <branch-name>` — Rebase current branch onto another branch
- `git rebase -i HEAD~n` — Interactive rebase (edit last *n* commits)

## Remote & GitHub

- `git clone <url>` — Clone a repository
- `git remote add origin <url>` — Add remote repository
- `git remote -v` — Show configured remotes
- `git fetch` — Fetch latest changes from remote (without merging)
- `git pull` — Fetch and merge changes from remote
- `git pull --rebase` — Fetch and rebase instead of merge
- `git push origin <branch-name>` — Push branch to GitHub
- `git push -u origin <branch-name>` — Push and set upstream tracking
- `git push --all origin` — Push all branches

## Undo & Recovery

- `git stash` — Temporarily save uncommitted changes
- `git stash pop` — Restore latest stash and remove it from stash list
- `git stash apply` — Apply stash without removing it
- `git reset --soft HEAD~1` — Undo last commit (keep changes staged)
- `git reset --mixed HEAD~1` — Undo last commit (unstage changes)
- `git reset --hard HEAD~1` — **DANGER**: Discard last commit and all changes
- `git revert <commit-hash>` — Create a new commit that undoes a previous commit
- `git checkout -- <file>` — Discard changes to a specific file
- `git restore <file>` — (Git 2.23+) Restore a file to last commit state

## Other Useful Commands

- `git rm <file>` — Remove a file from Git
- `git mv <old-name> <new-name>` — Rename/move a file
- `git tag v1.0.0` — Create a tag
- `git tag -l` — List tags
- `git cherry-pick <commit-hash>` — Apply a specific commit to current branch
- `.gitignore` — Create a file to ignore files/folders (e.g., `node_modules/`, `.env`)