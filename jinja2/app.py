from flask import Flask
from routes.index_route import index_route

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Cần thiết cho session

# Đăng ký blueprint
app.register_blueprint(index_route)

if __name__ == '__main__':
    app.run(host="localhost", port=5003, debug=True)
