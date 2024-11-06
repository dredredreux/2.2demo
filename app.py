import datetime
import fastapi
import pydantic

class Order(pydantic.BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str
    admin: str = "Не назначен"

basedata = [
    Order(number=1, startDate="2021-01-02", device="Чайник", problemType="технический", description="не кипятит", client="Чайников Чай Чаевич", status="в работе")
]

app = fastapi.FastAPI()

@app.get('/orders')
def orders():
    return basedata

@app.post('/order/create')
def create_order(order: Order):
    basedata.append(order)
    return basedata

@app.put('/order/{order_id}')
def status_order(order_id: int, order: Order = fastapi.Body()):
    for index, n in enumerate(basedata):
        if n.number == order_id:
            basedata[index] = order
            return order