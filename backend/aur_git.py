import os
import shutil
from subprocess import PIPE, STDOUT, CalledProcessError, Popen, check_output, check_call
from local_store import local_package_list, packages_dir
from dotenv import load_dotenv
from enum import Enum
load_dotenv()

class RepoFixType(Enum):
	RESET = 'reset'
	PULL = 'pull'
	ATTACH = 'attach'


def repo_package_clone(name: str):
	if name in local_package_list():
		return None
	repo_path = os.path.join(packages_dir(), name)
	if os.path.isdir(repo_path):
		shutil.rmtree(repo_path)
	repo_url = f'https://aur.archlinux.org/{name}.git'
	proc = Popen(['git', 'clone', repo_url, name, '--single-branch', '--progress'], cwd=packages_dir(), text=True, stdout=PIPE, stderr=STDOUT)
	# TODO: Maybe can be done using lib
	# Repo.clone_from(repo_url, repo_path, git_progress, multi_options=['--single-branch'])
	return proc.stdout

def repo_package_check(name: str):
	if not name in local_package_list():
		return None
	repo_path = os.path.join(packages_dir(), name)
	detached = False
	branch = 'master'
	correct_branch = True
	uncommited = False
	behind = 0
	ahead = 0

	branch_output = check_output(["git", "branch", "--show-current"], cwd=repo_path, text=True).strip()
	if not branch_output:
		detached = True
		correct_branch = False
	elif branch_output != "master":
		branch = branch_output
		correct_branch = False

	status_output = check_output(["git", "status", "--porcelain"], cwd=repo_path, text=True).strip()
	if status_output:
		uncommited = True

	try:
		output = check_output(['git', 'rev-list', '--count', '--left-right', 'HEAD...@{u}'], cwd=repo_path, text=True).strip()
		behind, ahead = map(int, output.split())
	except CalledProcessError:
		pass

	return {
		'commitsBehind': behind,
		'commitsAhead': ahead,
		'detachedBranch': detached,
		'branch': branch,
		'correctBranch': correct_branch,
		'uncommitedChanges': uncommited
	}

def repo_package_fix(name: str, type: RepoFixType):
	if not name in local_package_list():
		return None
	repo_path = os.path.join(packages_dir(), name)

	try:
		match type:
			case RepoFixType.RESET:
				check_call(['git', 'reset', 'origin/master'], cwd=repo_path, text=True)
				return True
			case RepoFixType.PULL:
				check_call(['git', 'pull'], cwd=repo_path, text=True)
				return True
			case RepoFixType.ATTACH:
				check_call(['git', 'checkout', 'master'], cwd=repo_path, text=True)
				return True
			case _:
				return None
	except CalledProcessError:
		return False