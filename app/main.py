import sys
import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI

# Start API
app = FastAPI()

# Load model
sys.path.append('src') # esse código faz com que o arquivo de utilidades seja procurado na pasta src
with open('models/recommender.pkl', 'rb') as file:
    recommender = pickle.load(file)
    
# create home
@app.get('/')
def home():
    return 'Welcome to the steam recommender app!'

# games list
@app.get('/list_games')
def list_games():
    return recommender.scores_.index.tolist()


# Run API
if __name__ == '__main__':
    uvicorn.run(app)