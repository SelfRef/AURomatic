from genericpath import isdir
import os
import shutil
from time import sleep
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from subprocess import Popen, PIPE, STDOUT

pkgbuilds_dir = '../pkgbuilds'

app = FastAPI()

@app.get("/api/pkgbuilds")
def get_pkgbuilds():
	return pkgbuild_repo_list()

@app.post("/api/pkgbuilds")
async def add_pkgbuild(name: str):
	return StreamingResponse(pkgbuild_repo_clone(name), media_type="text/plain")

def pkgbuild_repo_list():
	return [entry.name for entry in os.scandir(pkgbuilds_dir) if entry.is_dir()]

def pkgbuild_repo_clone(name: str):
	if name in pkgbuild_repo_list():
		return 'Repo already exists'
	repo_path = os.path.join(pkgbuilds_dir, name)
	if os.path.isdir(repo_path):
		shutil.rmtree(repo_path)
	repo_url = f'https://aur.archlinux.org/{name}.git'
	proc = Popen(['git', 'clone', repo_url, repo_path, '--single-branch', '--progress'], text=True, stdout=PIPE, stderr=STDOUT)
	return proc.stdout



@app.get("/stream")
async def get_stream():
	def stream():
		yield 'start\n'
		for i in range(5):
			sleep(1)
			yield 'stream' + str(i) + '\n'
		yield 'end\n'
	return StreamingResponse(stream(), media_type="text/plain")