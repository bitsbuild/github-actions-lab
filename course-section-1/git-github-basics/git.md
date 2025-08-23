# 📝 Git Cheat Sheet

A quick reference guide to the most commonly used Git commands.

---

## 🔧 Setup & Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list   # view config
````

---

## 📂 Repository Basics

```bash
git init                       # initialize a new repo
git clone <url>                # clone an existing repo
git status                     # check repo status
git log                        # view commit history
```

---

## 📌 Staging & Committing

```bash
git add <file>                 # stage a file
git add .                      # stage all changes
git commit -m "message"        # commit staged changes
git commit -am "message"       # stage & commit tracked files
```

---

## 🔄 Branching & Merging

```bash
git branch                     # list branches
git branch <name>              # create branch
git checkout <name>            # switch to branch
git checkout -b <name>         # create & switch to branch
git merge <branch>             # merge branch into current
git branch -d <name>           # delete branch
```

---

## 📤 Remote Repositories

```bash
git remote -v                  # list remotes
git remote add origin <url>    # add remote
git push -u origin <branch>    # push branch
git pull origin <branch>       # pull branch
git fetch                      # fetch latest updates
```

---

## 🛠 Undoing Changes

```bash
git restore <file>             # discard changes in working dir
git reset <file>               # unstage file
git reset --soft HEAD~1        # undo last commit, keep changes staged
git reset --mixed HEAD~1       # undo last commit, keep changes unstaged
git reset --hard HEAD~1        # undo last commit, discard changes
git revert <commit>            # create new commit that undoes a specific commit
```

---

## 📜 Stashing

```bash
git stash                      # stash changes
git stash list                 # list stashes
git stash apply                # apply most recent stash
git stash drop                 # remove most recent stash
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
git diff                       # show unstaged changes
git diff --staged              # show staged changes
git show <commit>              # show details of a commit
```

---

## 📦 Tags

```bash
git tag                        # list tags
git tag <name>                 # create tag
git push origin <tagname>      # push tag to remote