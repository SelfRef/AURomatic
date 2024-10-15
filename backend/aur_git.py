import os
import shutil
from subprocess import PIPE, STDOUT, Popen
from local_store import local_package_list, package_dir


def repo_package_clone(name: str):
	if name in local_package_list():
		return 'Repo already exists'
	repo_path = os.path.join(package_dir(), name)
	if os.path.isdir(repo_path):
		shutil.rmtree(repo_path)
	repo_url = f'https://aur.archlinux.org/{name}.git'
	proc = Popen(['git', 'clone', repo_url, repo_path, '--single-branch', '--progress'], text=True, stdout=PIPE, stderr=STDOUT)
	# TODO: Maybe can be done using lib
	# Repo.clone_from(repo_url, repo_path, git_progress, multi_options=['--single-branch'])
	return proc.stdout