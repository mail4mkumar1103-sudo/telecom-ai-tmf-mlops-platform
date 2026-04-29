import random
import pandas as pd

def generate_data(n=500):
    data = []

    for i in range(n):
        data.append({
            "call_duration": random.randint(1, 1000),
            "cost": random.randint(1, 500)
        })

    return pd.DataFrame(data)
