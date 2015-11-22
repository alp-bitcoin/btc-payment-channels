from payment_channels import app

@app.route('/')
def index():
    return "Hello World"
