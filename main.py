from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import house_router

app = FastAPI()

app.include_router(house_router)

# CORS -> Cross Origin Resource Sharing -> Response of the API from other domains 
# -> Middleware: Acts as a intermediary between different parts of the app. 
# -> allow_origins -> allows requests from any dom 
# -> allow_credentials -> allows the usage of credentials like cookies, headers, etc. 
# -> allow_methods: allow get, post, put, delete 

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)