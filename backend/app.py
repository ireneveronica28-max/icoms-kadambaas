from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.orders import orders_bp
    from routes.reports import reports_bp
    from routes.notifications import notifications_bp
    from routes.deliveries import deliveries_bp
    from routes.leftovers import leftovers_bp
    from routes.tracking import tracking_bp


    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(orders_bp, url_prefix="/api/orders")
    app.register_blueprint(reports_bp, url_prefix="/api/reports")
    app.register_blueprint(notifications_bp, url_prefix="/api/notifications")
    app.register_blueprint(deliveries_bp, url_prefix="/api/deliveries")
    app.register_blueprint(leftovers_bp, url_prefix="/api/leftovers")
    app.register_blueprint(tracking_bp, url_prefix="/api/tracking")
    
    @app.route("/")
    def login_page():
        return render_template("ui.html")

    @app.route("/admin")
    def admin_page():
        return render_template("admin.html")

    @app.route("/supervisor")
    def supervisor_page():
        return render_template("supervisor.html")

    @app.route("/track")
    def track_page():
        return render_template("track.html")

    @app.route("/driver")
    def driver_page():
        return render_template("driver.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
