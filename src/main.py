from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run

from dependencies import check_dependencies
from directories import BASE_DIR
from routes import router


app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(router)


def main():
    print("Checking dependencies...")
    check_dependencies()

    print("Starting exemplary api...")
    run(app, host="0.0.0.0", port=7200)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
