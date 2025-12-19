from flask import Flask, request, redirect, url_for, Response, session

app = Flask(__name__)
app.secret_key = "supersecret"

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    users = {
        "admin" : "123",
        "sushank" :"456",
        "dikshit" : "789"

    }
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype="text/plain")

    # GET request: show login form
    return """
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="username" /><br><br>
        Password: <input type="password" name="password" /><br><br>
        <input type="submit" value="Login" />
    </form>
    """

# Welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome, {session['user']}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        """
    return redirect(url_for("login"))

# Logout page
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
