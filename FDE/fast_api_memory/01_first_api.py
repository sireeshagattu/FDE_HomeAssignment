from fastapi import FastAPI

app = FastAPI()

employees = [
    [101, "Sireesha", 200000],
    [102, "Rahul", 180000],
    [103, "Praveen", 260000],
    [104, "Sujatha", 220000]]

@app.get("/employees")
def get_employees():
    return employees