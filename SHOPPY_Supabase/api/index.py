from flask import Flask, jsonify
from flask_cors import CORS

# Load Config
from config import Config

# -----------------------------------------------------
# IMPORT CÁC BLUEPRINT
# -----------------------------------------------------
# Vì file này nằm trong folder api/, và các folder map/routes cũng nằm trong api/
# nên cách import giữ nguyên như cũ là được.
from routes.search_routes import search_bp
from routes.review_routes import review_bp
from routes.api_routes import api_bp
from map import map_bp 
from routes.location_routes import location_bp
from routes.cart_routes import cart_bp
from routes.product_summary_routes import product_summary_bp
from routes.suggest_routes import suggest_bp

# -----------------------------------------------------
# KHỞI TẠO APP
# -----------------------------------------------------
# [SỬA 1] Bỏ static_folder và static_url_path vì Vercel tự quản lý file tĩnh
app = Flask(__name__)

# Load cấu hình
app.config.from_object(Config)

# Cấu hình Secret Key
app.secret_key = 'shoppy_secret_key_2024_bao_mat_vkl'

# Cấu hình CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*", 
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "expose_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True, 
        }
    },
)

# -----------------------------------------------------
# ĐĂNG KÝ (REGISTER) BLUEPRINTS
# -----------------------------------------------------

app.register_blueprint(api_bp) 
app.register_blueprint(search_bp)
app.register_blueprint(review_bp)

# Blueprint Map: Lưu ý route này sẽ được xử lý bởi Python
app.register_blueprint(map_bp, url_prefix='/map')

app.register_blueprint(location_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(product_summary_bp)
app.register_blueprint(suggest_bp)

# -----------------------------------------------------
# [QUAN TRỌNG] ROUTE KIỂM TRA
# -----------------------------------------------------
# Route này để test xem Backend trên Vercel có sống không
@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "active",
        "message": "Backend Flask đang chạy ngon lành trên Vercel!"
    })

# [SỬA 2] Đã XOÁ hoàn toàn các route @app.route("/") và serve_static
# Lý do: File vercel.json bên dưới sẽ đảm nhận việc này.

# -----------------------------------------------------
# CHẠY SERVER (Chỉ dùng khi test dưới máy)
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)