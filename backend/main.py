import json
import os
from time import sleep
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from aur_git import RepoFixType, repo_package_check, repo_package_clone, repo_package_fix
from aur_api import aur_package_info
from local_store import local_package_list
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/api/pkgbuilds")
def get_pkgbuilds():
	return local_package_list()

@app.get("/api/pkgbuilds/{name}")
def get_pkgbuild_info(name: str):
	if os.getenv('PYTHON_DEV'):
		return json.loads('{"Depends":["libxtst","libxkbcommon","libnotify","libei","libportal","qt6-base","gdk-pixbuf2","pugixml"],"Description":"Deskflow lets you share one mouse and keyboard between multiple computers (stable version)","FirstSubmitted":1727704508,"ID":1560789,"Keywords":["deskflow","keyboard","kvm","mouse","share","synergy"],"LastModified":1728914743,"License":["GPL-2.0"],"Maintainer":"SelfRef","MakeDepends":["git","cmake","python","libxkbfile","gtest","tomlplusplus","cli11"],"Name":"deskflow","NumVotes":2,"OptDepends":["openssl","gtk3","libxkbcommon-x11","libxkbfile","libxinerama","libxrandr"],"OutOfDate":null,"PackageBase":"deskflow","PackageBaseID":210340,"Popularity":1.930048,"Submitter":"SelfRef","URL":"https://deskflow.org/","URLPath":"/cgit/aur.git/snapshot/deskflow.tar.gz","Version":"1.17.0-9"}')
	return aur_package_info(name)

@app.get("/api/pkgbuilds/{name}/status")
def get_pkgbuild_status(name: str):
	return repo_package_check(name)

@app.post("/api/pkgbuilds/{name}")
async def add_pkgbuild(name: str):
	if os.getenv('PYTHON_DEV'):
		return StreamingResponse('Test output string\n'*100, media_type="text/plain")
	if not aur_package_info(name):
		return Response('Repository not found', 404)
	clone = repo_package_clone(name)
	if clone is None:
		return Response('Repository already exists', 400)
	return StreamingResponse(clone, media_type="text/plain")

@app.patch("/api/pkgbuilds/{name}")
async def fix_pkgbuild(name: str, fix: RepoFixType):
	return repo_package_fix(name, fix)




def stream():
	for i in range(5):
		yield 'Stream' + str(i) + '\n'
		sleep(1)

@app.post("/api/stream")
async def test_stream():
	return StreamingResponse(stream(), media_type="text/plain")