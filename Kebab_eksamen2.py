from flask import Flask, render_template

app = Flask(__name__)

kebab_menu = [
    {
        "name": "Original Kebab",
        "description": "Saftig kebabkjøtt, salat, tomat, løk og kebabsaus.",
        "price": "129 kr",
        "image": "https://images.unsplash.com/photo-1598514984597-5e39ad3ac404?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Chicken Kebab",
        "description": "Grillet kylling, frisk salat, paprika, og mild yoghurt-saus.",
        "price": "139 kr",
        "image": "https://images.unsplash.com/photo-1555992336-03a23c8f9a0d?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Vegetar Kebab",
        "description": "Grillet halloumi, salat, agurk, tomat og pesto.",
        "price": "119 kr",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Extra Hot Kebab",
        "description": "Sterk kebab med chili, jalapeños, salat og ekstra saus.",
        "price": "149 kr",
        "image": "https://images.unsplash.com/photo-1512058564366-c9e6f9fbd167?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Cheese Kebab",
        "description": "Kebab med smeltet ost, salat, tomat og hvitløksdressing.",
        "price": "139 kr",
        "image": "https://images.unsplash.com/photo-1532634896-26909d0d4b9b?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "BBQ Kebab",
        "description": "Kebab med barbecuesaus, mais, salat og rødløk.",
        "price": "149 kr",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Mexico Kebab",
        "description": "Kebab med salsa, avokado, mais og frisk koriander.",
        "price": "149 kr",
        "image": "https://images.unsplash.com/photo-1484723091739-30a097e8f929?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Family Kebab",
        "description": "Dobbel porsjon kebabkjøtt, salat, tomat, løk og rikelig saus.",
        "price": "179 kr",
        "image": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80"
    }
]

@app.route("/")
def index():
    return render_template("index.html", kebab_menu=kebab_menu)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/help")
def help_page():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6111)