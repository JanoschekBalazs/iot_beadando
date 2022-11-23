from fastapi import FastAPI

weight = 50

app = FastAPI()

@app.post("/weight/{weight_control}")
def control_weight(weight_control: int):
    global weight
    if (weight_control == 1):
        weight += 10
    else:
        weight -= 10
    return True

