from flask_frozen import Freezer
from app import app

app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_RELATIVE_URLS_PRETTY"] = True

if __name__ == "__main__":
    Freezer(app).freeze()
