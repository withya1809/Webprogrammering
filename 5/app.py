"""
Flask: Using templates
"""

from read import *
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#load all students from students.tsv.
# returns a dictionary (student_no) -> name
def load_students():
    students = {}
    """Loads data from input tsv files."""
    # Load students
    print("Loading students.tsv ...")
    with open("students.tsv", "r") as f:
        for line in f:
            student_no, name = line.strip().split("\t")
            students[student_no] = name
    return students

@app.route("/")
def index():
    return render_template("index.html", students=load_students())

# Add additional routes here.


if __name__ == "__main__":
    app.run(debug=True)