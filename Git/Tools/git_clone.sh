#!/bin/bash

# Clone the repo you care about
echo "Enter original git repository url"
read -p '(From GitHub and looks like "https://github.com/some-user/repo-name.git"): ' upstreamVar
echo Ready to clone in this here directory? `pwd`
read -p '(CTRL+C) if you want to quit, otherwise just press "ENTER"'
echo

# Clone the repo
git clone $upstreamVar
echo

# Get info on what directory is named and changing to that path
basename=$(basename $upstreamVar)
dirname=${basename%.*}
echo "Setting up your git repo as $dirname"
cd $dirname
echo

# Ask the user for their repository to make commits to
echo "Now for YOUR repository url (from GitHub)"
read -p "If you haven't done so already, go to github.com and make an new (empty repo): " myUpstreamVar


# Changing remote to user's
git remote set-url origin $myUpstreamVar
echo

# Verification
echo "Please verify your remote was:"
git remote -v
echo
echo "Please verify your credentials:"
echo username: `git config user.name`
echo email: `git config user.email`

# Do a git push (sync with GitHub)
echo
read -p 'Continue to push to your GitHub repo? "ENTER" to continue'
git push -u origin
