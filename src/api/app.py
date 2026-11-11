
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Apex Exchange API",
    description="Simulated financial API for AI quality engineering",
    version="1.0.0"
)

# Simulated customer database
customers = {
    101: {
        "customer_id": 101,
        "name": "Rahul",
        "account_type": "premium",
        "currency": "INR",
        "balance": 150000
    },
    102: {
        "customer_id": 102,
        "name": "Priya",
        "account_type": "standard",
        "currency": "INR",
        "balance": 75000
    }
}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Apex Exchange API"
    }


@app.get("/account/{customer_id}")
def get_account(customer_id: int):

    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customers[customer_id]


@app.get("/balance/{customer_id}")
def get_balance(customer_id: int):

    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    customer = customers[customer_id]

    return {
        "customer_id": customer_id,
        "currency": customer["currency"],
        "balance": customer["balance"]
    }