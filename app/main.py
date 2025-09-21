from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from .utils import sum_list

app = FastAPI(title="CI/CD Practice Service")


class Numbers(BaseModel):
    numbers: List[float]


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello — CI/CD practice!"}


@app.post("/sum")
def post_sum(data: Numbers) -> Dict[str, float]:
    total = sum_list(data.numbers)
    return {"result": total}
