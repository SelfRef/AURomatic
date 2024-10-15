from time import sleep
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from aur_git import repo_package_clone
from aur_api import aur_package_info
from local_store import local_package_list


app = FastAPI()

@app.get("/api/pkgbuilds")
def get_pkgbuilds():
	return local_package_list()

@app.get("/api/pkgbuilds/{name}")
def get_pkgbuild_info(name: str):
	return aur_package_info(name)

@app.post("/api/pkgbuilds/{name}")
async def add_pkgbuild(name: str):
	if not aur_package_info(name):
		return 'Package does not exists'
	return StreamingResponse(repo_package_clone(name), media_type="text/plain")





def stream():
	for i in range(5):
		yield 'Stream' + str(i) + '\n'
		sleep(1)

@app.post("/api/stream")
async def test_stream():
	return StreamingResponse(stream(), media_type="text/plain")