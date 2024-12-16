import subprocess
import mlflow
import mlflow.projects

# Step 1: Commit changes to Git
def git_commit_and_push(commit_message="Committing changes before running MLflow project"):
    try:
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", commit_message])
        subprocess.check_call(["git", "push"])
        print(f"Changes committed and pushed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git commit/push: {e}")

# Step 2: Get Git commit hash
def get_git_commit_hash():
    try:
        commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode("utf-8")
        return commit_hash
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve commit hash.")
        return None

git_commit_and_push()
commit_hash = get_git_commit_hash()
print(f"Current Git Commit: {commit_hash}")

# Step 3: Log Git commit hash in MLflow
def log_git_commit_hash(commit_hash):
    if commit_hash:
        mlflow.set_tag("git_commit", commit_hash)

log_git_commit_hash(commit_hash)

# Step 4: Run MLflow project
project_uri = "https://github.com/enjay27/mlops-example.git"
params = {"learning_rate": 0.05, "n_estimators": 150}

run = mlflow.projects.run(
    uri=project_uri,
    parameters=params,
    backend="local",
    use_conda=True
)

# Step 5: Commit model outputs (if necessary)
def commit_model_output(output_dir, commit_message="Committing model outputs"):
    try:
        subprocess.check_call(["git", "add", output_dir])
        subprocess.check_call(["git", "commit", "-m", commit_message])
        subprocess.check_call(["git", "push"])
        print(f"Model outputs committed: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error committing model outputs: {e}")

commit_model_output("model_outputs/", "Committing model outputs after MLflow run")
