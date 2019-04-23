import subprocess



def check_dir():
    '''
    Will print out the current directory using command line `pwd`
    '''
    cmd = ['pwd']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Confirmation
    o, e = proc.communicate()
    print(f'Current directory: {o}')


def clone_repo(git_repo):
    '''
    Attempts to clone repo via URL and rename the `.git` directory so git doesn't get confused
    '''
    #
    git_dir = git_repo.split('/')[-1].replace('.git', '')

    # Clone
    print(f'Attempting to clone repo from "{git_repo}" to current directory...\n')
    cmd_clone = ['git', 'clone', git_repo]
    proc_clone = subprocess.Popen(cmd_clone, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Confirmation
    o, e = proc_clone.communicate()
    print(f"Output: {o.decode('ascii')}")
    print(f"(Possible) Error: {e.decode('ascii')}")

    # Move `.git` directory within clone
    old_dirname = f'{git_dir}/.git'
    new_dirname = f'{git_dir}/._old_git'
    cmd_move = ['mv', old_dirname, new_dirname]
    proc_move = subprocess.Popen(cmd_move, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Confirmation
    o, e = proc_move.communicate()
    print(f"Output: {o.decode('ascii')}")
    print(f"(Possible) Error: '{e.decode('ascii')}")


def append_to_readme(git_repo, filename='README.md'):
    '''
    Appends the repo name to the README file (creates file if it doesn't already)
    '''
    text = f'\n- Repo added: {git_repo}'
    with open(f"{filename}", "a") as myfile:
        myfile.write(text)



# Check that we are in the right spot
check_dir()
is_correct_dir = input('Are you in the correct area? ("y" or "n")\n')

if (is_correct_dir.lower() != 'y') and (is_correct_dir.lower() != 'yes'):
    print('Ok exiting and run this again when you navigate to the correct directory')
else:
    # Repeat until user says to stop
    continue_cloning = True
    while continue_cloning:
        # Continue (correct directory)
        user_proceed = input('Do you want to continue with cloning a repo? ("yes" to continue)\n').lower()

        # Stop here
        if (user_proceed != 'y') and (user_proceed != 'yes'):
            continue_cloning = False
            break

        # Clone repo in current directory
        print('')
        git_repo = input('What repo (URL) do you want to clone? (no extra spaces or characters; should end with .git)\n')
        clone_repo(git_repo)

        # Append to README
        print('If clone was successful, we should give credit in the README')
        readme_name = input('What is the name of your README? Just enter (no text) to use "README.md". Note that this file must be in current directory & case sensitive.\n')
        if readme_name == '':
            append_to_readme(git_repo, 'README.md')
            print(f'README.md was appended with repo cloned: {git_repo}')
        else:
            append_to_readme(git_repo, readme_name)
            print(f'README.md was appended with repo cloned: {git_repo}')

# Out of loop - done
print('Exited')
