from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_index():
    return FileResponse('views/index.html')

if __name__ == "__main__":
    uvicorn.run(app)