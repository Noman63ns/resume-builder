from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": request.form.get("address"),
            "dob": request.form.get("dob"),
            "nationality": request.form.get("nationality"),
            "profile": request.form.get("profile"),
            "skills": request.form.getlist("skills"),
            "languages": request.form.getlist("languages"),
            "education": [
                {
                    "degree": request.form.get("degree1"),
                    "institute": request.form.get("institute1"),
                    "gpa": request.form.get("gpa1"),
                    "duration": request.form.get("duration1")
                },
                {
                    "degree": request.form.get("degree2"),
                    "institute": request.form.get("institute2"),
                    "gpa": request.form.get("gpa2"),
                    "duration": request.form.get("duration2")
                }
            ],
            "internships": request.form.get("internships"),
            "activities": request.form.get("activities"),
            "research": request.form.get("research")
        }
        return render_template("resume.html", data=data)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
