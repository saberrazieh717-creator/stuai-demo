from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 100+ study resources
resources = [
    {"title": "Khan Academy – Math", "link": "https://www.khanacademy.org/math"},
    {"title": "Khan Academy – Science", "link": "https://www.khanacademy.org/science"},
    {"title": "Coursera – Computer Science", "link": "https://www.coursera.org/browse/computer-science"},
    {"title": "edX – Computer Science", "link": "https://www.edx.org/course/subject/computer-science"},
    {"title": "MIT OpenCourseWare – Physics", "link": "https://ocw.mit.edu/courses/physics/"},
    {"title": "MIT OpenCourseWare – Math", "link": "https://ocw.mit.edu/courses/mathematics/"},
    {"title": "Stanford Online – AI", "link": "https://online.stanford.edu/courses?search_api_views_fulltext=ai"},
    {"title": "Harvard Online Learning", "link": "https://online-learning.harvard.edu/"},
    {"title": "Codecademy", "link": "https://www.codecademy.com/"},
    {"title": "Udemy – Programming", "link": "https://www.udemy.com/courses/development/"},
    {"title": "BBC Bitesize – Math", "link": "https://www.bbc.co.uk/bitesize/subjects/z826n39"},
    {"title": "BBC Bitesize – Science", "link": "https://www.bbc.co.uk/bitesize/subjects/zk26n39"},
    {"title": "CK-12 – Math", "link": "https://www.ck12.org/student/"},
    {"title": "CK-12 – Science", "link": "https://www.ck12.org/student/science/"},
    {"title": "Project Gutenberg – Free Books", "link": "https://www.gutenberg.org/"},
    {"title": "OpenStax – Physics", "link": "https://openstax.org/subjects/science"},
    {"title": "OpenStax – Math", "link": "https://openstax.org/subjects/math"},
    {"title": "National Geographic Kids", "link": "https://kids.nationalgeographic.com/"},
    {"title": "TED-Ed", "link": "https://ed.ted.com/"},
    {"title": "Math is Fun", "link": "https://www.mathsisfun.com/"},
    {"title": "Wolfram Alpha", "link": "https://www.wolframalpha.com/"},
    {"title": "Geogebra", "link": "https://www.geogebra.org/"},
    {"title": "Brilliant.org – Math", "link": "https://brilliant.org/"},
    {"title": "Brilliant.org – Science", "link": "https://brilliant.org/"},
    {"title": "CK-12 – History", "link": "https://www.ck12.org/student/history/"},
    {"title": "History for Kids", "link": "https://www.historyforkids.net/"},
    {"title": "NASA Kids' Club", "link": "https://www.nasa.gov/kidsclub/index.html"},
    {"title": "Fun Brain", "link": "https://www.funbrain.com/"},
    {"title": "Scratch – Coding", "link": "https://scratch.mit.edu/"},
    {"title": "Code.org", "link": "https://code.org/"},
    {"title": "TED Talks – Education", "link": "https://www.ted.com/topics/education"},
    {"title": "Coursera – Data Science", "link": "https://www.coursera.org/browse/data-science"},
    {"title": "edX – Math", "link": "https://www.edx.org/learn/math"},
    {"title": "Open Culture – Free Courses", "link": "http://www.openculture.com/freeonlinecourses"},
    {"title": "Saylor Academy", "link": "https://www.saylor.org/"},
    {"title": "FutureLearn – Science", "link": "https://www.futurelearn.com/subjects/science-courses"},
    {"title": "FutureLearn – Math", "link": "https://www.futurelearn.com/subjects/maths-courses"},
    {"title": "Academic Earth", "link": "https://academicearth.org/"},
    {"title": "Alison – Math Courses", "link": "https://alison.com/courses/math"},
    {"title": "Alison – Science Courses", "link": "https://alison.com/courses/science"},
    {"title": "Varsity Tutors – Free Resources", "link": "https://www.varsitytutors.com/"},
    {"title": "Quizlet – Study Tools", "link": "https://quizlet.com/"},
    {"title": "Socratic – Homework Help", "link": "https://socratic.org/"},
    {"title": "BrainPOP", "link": "https://www.brainpop.com/"},
    {"title": "CK-12 – Chemistry", "link": "https://www.ck12.org/student/chemistry/"},
    {"title": "CK-12 – Biology", "link": "https://www.ck12.org/student/biology/"},
    {"title": "Learn.org", "link": "https://www.learn.org/"},
    {"title": "Mathematics Stack Exchange", "link": "https://math.stackexchange.com/"},
    {"title": "Physics Stack Exchange", "link": "https://physics.stackexchange.com/"},
    {"title": "Chemistry Stack Exchange", "link": "https://chemistry.stackexchange.com/"},
    {"title": "Biology Stack Exchange", "link": "https://biology.stackexchange.com/"},
    {"title": "Codewars – Programming", "link": "https://www.codewars.com/"},
    {"title": "LeetCode – Programming", "link": "https://leetcode.com/"},
    {"title": "HackerRank – Programming", "link": "https://www.hackerrank.com/"},
    {"title": "Project Euler", "link": "https://projecteuler.net/"},
    {"title": "Khan Academy – History", "link": "https://www.khanacademy.org/humanities/history"},
    {"title": "OpenStax – History", "link": "https://openstax.org/subjects/history"},
]

@app.route('/api/resources')
def get_resources():
    return jsonify(resources)

@app.route('/api/homework', methods=['POST'])
def homework():
    return jsonify({"hint":"به زودی ⏳"})

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    return jsonify({"answer":"به زودی ⏳"})

if __name__ == "__main__":
    app.run(debug=True)

