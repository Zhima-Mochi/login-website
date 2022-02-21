import login_website
import uvicorn
uvicorn.run("login_website.main:app", host="127.0.0.1", port=8080)
