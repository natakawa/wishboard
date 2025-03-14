from flask import Flask
from config import DevelopmentConfig
from .extensions import db, login_manager, migrate

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Инициализация расширений
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    
    # Регистрация blueprints
    from .routes import auth, wishlist, item
    app.register_blueprint(auth.bp)
    app.register_blueprint(wishlist.bp)
    app.register_blueprint(item.bp)
    
    # Рендеринг главной страницы
    @app.route('/')
    def index():
        return __import__('flask').render_template('index.html')
    
    return app
