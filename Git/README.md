# `git_clone.sh`

## Summary

This script will take a git repository and clone it to your local machine but
under your own repository in GitHub.

## Steps

1. Download `git_clone.sh` file and save to the directory to clone repository on your computer
2. Create a repo on your GitHub where the repo will live [github.com/new](https://github.com/new)
and have your repository's URL (ends with `.git`)
3. Have the original repository's URL (ends with `.git`)
4. Run the script on your computer with `sh git_clone.sh`
5. Follow directions that will proceed to clone, update repo with your GitHub URL,
and push to GitHub

## Doing It Manually

You can proceed to do the same thing by doing this in the terminal:

```
git clone https://github.com/OTHER_USER/ORIG_REPO.git
cd ORIG_REPO
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin
```


----------
