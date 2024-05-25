import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env



app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r" ) as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = "About", company=data)


# Route Definition: @app.route("/about/<member_name>") defines a route in a Flask web application. When a user goes to a URL like "/about/some_member_name", Flask knows to call a function named about_member, passing "some_member_name" as a parameter.

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r" ) as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

# Exactly! When you click on a link like `/about/thorin`, Flask interprets it as a request to the `about_member` function, passing `"thorin"` as the `member_name` parameter. 

# Then, within the `about_member` function, it iterates through the JSON data to find an object where the `"url"` attribute matches `"thorin"`. If such an object is found, it assigns it to the `member` variable. 

# So, in this case, clicking on the link triggers the function with `"thorin"` as the `member_name`, and if there's a member in the JSON data with the URL attribute equal to `"thorin"`, that member's information is displayed.
    
# The `member=member` part is the syntax used in Python to pass a variable named `member` to the template `render_template("member.html", member=member)`. 

# Here's what's happening:

# - `render_template("member.html", member=member)`: This function call tells Flask to render the HTML template named "member.html" and pass the variable `member` to it. The first `member` is the name of the variable in the template (which can be accessed within the template using this name), and the second `member` is the Python variable that holds the member information retrieved from the JSON file.

# So essentially, it's saying "Render the 'member.html' template and provide it with the data stored in the `member` variable." This allows the HTML template to access and display the information about the specific member.


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title = "Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)