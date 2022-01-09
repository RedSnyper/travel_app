from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {"message": "hello world"}

if __name__ == '__main__':
    main()