# 📝 Git Cheat Sheet

A quick reference guide to the most commonly used Git commands.

---

## 🔧 Setup & Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list   # view all config
```

---

## 📂 Repository Basics

```bash
git init                       # initialize a new repository
git clone <url>                 # clone an existing repository
git status                      # check repo status
git log                         # view commit history
```

---

## 📌 Staging & Committing

```bash
git add <file>                  # stage a specific file
git add .                       # stage all changes
git commit -m "message"         # commit staged changes
git commit -am "message"        # stage & commit tracked files
```

---

## 🔄 Branching & Merging

```bash
git branch                      # list all branches
git branch <name>               # create a new branch
git checkout <name>             # switch to branch
git checkout -b <name>          # create & switch to branch
git merge <branch>              # merge branch into current branch
git branch -d <name>            # delete a branch
```

---

## 📤 Remote Repositories

```bash
git remote -v                   # list remotes
git remote add origin <url>     # add a remote repository
git push -u origin <branch>     # push branch and set upstream
git pull origin <branch>        # pull branch from remote
git fetch                       # fetch latest updates from remote
```

---

## 🛠 Undoing Changes

```bash
git restore <file>              # discard changes in working directory
git reset <file>                # unstage a file

# Undo last commit (without commit ID)
git reset --soft HEAD~1         # undo last commit, keep changes staged
git reset --mixed HEAD~1        # undo last commit, keep changes unstaged
git reset --hard HEAD~1         # undo last commit, discard changes

git revert <commit>             # create new commit that undoes a specific commit
```

**Notes on `git reset HEAD~1`**:

* **Soft** → keeps all changes staged (ready to commit again).
* **Mixed** → keeps changes in working directory but unstaged.
* **Hard** → discards all changes completely.

---

## 📜 Stashing

```bash
git stash                       # stash changes
git stash list                  # list stashes
git stash apply                 # apply most recent stash
git stash drop                  # remove most recent stash
```

---

## 🌐 Gitignore

* Create `.gitignore` file
* Add files/folders to ignore

Example:

```
node_modules/
*.log
.env
```

---

## 🔍 Inspection

```bash
git diff                        # show unstaged changes
git diff --staged               # show staged changes
git show <commit>               # show details of a commit
```

---

## 📦 Tags

```bash
git tag                         # list all tags
git tag <name>                  # create a tag
git push origin <tagname>       # push tag to remote