from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"ok": True, "service": "BlockBot OAuth/health"}

@app.get("/discord/callback")
async def discord_callback(code: str | None = None, state: str | None = None):
    # For now we just acknowledge; you can add code-exchange later.
    return PlainTextResponse("Discord OAuth callback received. You can close this window.")

@app.get("/twitch/callback")
async def twitch_callback(code: str | None = None, state: str | None = None):
    return PlainTextResponse("Twitch OAuth callback received. You can close this window.")
