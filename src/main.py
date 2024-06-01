from dependencies import check_dependencies
from fastapi import FastAPI
from routes import router
from uvicorn import run


app = FastAPI()
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
