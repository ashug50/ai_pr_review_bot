from git import Repo
from config import BASE_BRANCH, MAX_FILES, MAX_FILE_SIZE

def get_changed_files(repo_path):
    repo = Repo(repo_path)
    repo.git.fetch()
    diff = repo.git.diff(f"origin/{BASE_BRANCH}...HEAD", name_only=True)
    return diff.splitlines()[:MAX_FILES]

def get_file_diff(repo_path, file_path):
    repo = Repo(repo_path)
    diff = repo.git.diff(f"origin/{BASE_BRANCH}...HEAD", "--", file_path)
    if len(diff) > MAX_FILE_SIZE:
        diff = diff[:MAX_FILE_SIZE]
    return diff
