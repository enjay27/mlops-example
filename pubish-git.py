import mlflow

from commit import get_git_commit_hash

# Log the Git commit hash as a tag
def log_git_commit_hash(commit_hash):
    if commit_hash:
        mlflow.set_tag("git_commit", commit_hash)
    else:
        print("No Git commit hash available to log.")

log_git_commit_hash(get_git_commit_hash())