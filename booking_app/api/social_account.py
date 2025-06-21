from fastapi import APIRouter
from starlette.requests import Request
from booking_app.config import social
from authlib.integrations.starlette_client import OAuth


social_router = APIRouter(prefix='/oauth' , tags=['Social Auth'])

oauth = OAuth()
oauth.register(
    name = 'github',
    client_id = social.GITHUB_CLIENT_ID,
    secret_key = social.GITHUB_KEY,
    authorize_url = 'https://github.com/login/oauth/authorize',
)
oauth.register(
    name = 'google',
    client_id = social.GITHUB_CLIENT_ID,
    secret_key = social.GOOGLE_KEY,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_kwargs={"scope": "openid profile email"},
)

@social_router.get('/github')
async def login_github(request: Request):
    redirect_uri = social.GITHUB_URL
    return await oauth.github.authorize_redirect(request, redirect_uri)

@social_router.get('/google')
async def login_google(request: Request):
    redirect_uri = social.GOOGLE_URL
    return await oauth.google.authorize_redirect(request, redirect_uri)






