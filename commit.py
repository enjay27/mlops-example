import subprocess

# Capture the current Git commit hash
def get_git_commit_hash():
    try:
        commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")
        return commit_hash
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve commit hash.")
        return None

commit_hash = get_git_commit_hash()
print(f"Current Git Commit: {commit_hash}")