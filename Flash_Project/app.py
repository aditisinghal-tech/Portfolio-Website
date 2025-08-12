from flask import Flask, render_template, request, flash, redirect, url_for

# Create the Flask Application instance
app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """This route handles the 'Contact' page.
    - GET: Shows the contact form.
    - POST: Processes submitted form data.
    """
    # Check if form was submitted
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(f"Message from {name} ({email}): {message}")

        # Flash a success message to show to the user
        flash("Thank you for your message! I'll get back to you soon.", "success")

        # Redirect to the contact page(Prevents from resubmission)
        return redirect(url_for("contact"))

    # if Get request, just render the contact form
    return render_template("contact.html")

# APP ENTRY POINT
if __name__ == "__main__":
    # Run the app in debug mode (auto-reload & detailed errors)
    app.run(debug=True)