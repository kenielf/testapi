from fastapi import FastAPI
from routes import router
from uvicorn import run


app = FastAPI()
app.include_router(router)


def main():
    print("Starting exemplary api...")
    run(app)


if __name__ == "__main__":
    main()
