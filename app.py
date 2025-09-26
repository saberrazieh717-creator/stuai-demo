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
    {"title": "Crash Course – YouTube", "link": "https://www.youtube.com/user/crashcourse"},
    {"title": "National Science Digital Library", "link": "https://nsdl.oercommons.org/"},
    {"title": "HippoCampus", "link": "https://www.hippocampus.org/"},
    {"title": "CK-12 – Engineering", "link": "https://www.ck12.org/student/engineering/"},
    {"title": "NASA STEM", "link": "https://www.nasa.gov/stem"},
    {"title": "Smithsonian Learning Lab", "link": "https://learninglab.si.edu/"},
    {"title": "BBC Bitesize – Geography", "link": "https://www.bbc.co.uk/bitesize/subjects/zyrw2hv"},
    {"title": "National Geographic Education", "link": "https://www.nationalgeographic.org/education/"},
    {"title": "American Chemical Society – Education", "link": "https://www.acs.org/content/acs/en/education.html"},
    {"title": "MathPlanet", "link": "https://www.mathplanet.com/"},
    {"title": "CK-12 – Physics", "link": "https://www.ck12.org/student/physics/"},
    {"title": "OpenStax – Biology", "link": "https://openstax.org/subjects/biology"},
    {"title": "OpenStax – Chemistry", "link": "https://openstax.org/subjects/chemistry"},
    {"title": "Khan Academy – Programming", "link": "https://www.khanacademy.org/computing/computer-programming"},
    {"title": "Udacity – Free Courses", "link": "https://www.udacity.com/courses/all"},
    {"title": "Coursera – Free Courses", "link": "https://www.coursera.org/courses?query=free"},
    {"title": "edX – Free Courses", "link": "https://www.edx.org/course"},
    {"title": "MIT OpenCourseWare – Computer Science", "link": "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/"},
    {"title": "Stanford Online – Free Courses", "link": "https://online.stanford.edu/courses"},
    {"title": "Harvard CS50", "link": "https://cs50.harvard.edu/x/"},
    {"title": "Yale Open Courses", "link": "https://oyc.yale.edu/"},
    {"title": "Princeton Online Courses", "link": "https://online.princeton.edu/"},
    {"title": "Oxford Online Courses", "link": "https://www.conted.ox.ac.uk/about/online-courses"},
    {"title": "Cambridge OpenCourseWare", "link": "https://www.cambridge.org/"},
    {"title": "FutureLearn – Free Courses", "link": "https://www.futurelearn.com/courses"},
    {"title": "Alison – Free Courses", "link": "https://alison.com/courses"},
    {"title": "Saylor Academy – Free Courses", "link": "https://www.saylor.org/courses/"},
    {"title": "Khan Academy – Arts & Humanities", "link": "https://www.khanacademy.org/humanities"},
    {"title": "OpenStax – Economics", "link": "https://openstax.org/subjects/economics"},
    {"title": "edX – Humanities", "link": "https://www.edx.org/learn/humanities"},
    {"title": "Coursera – Arts", "link": "https://www.coursera.org/browse/arts-and-humanities"},
    {"title": "Khan Academy – Economics", "link": "https://www.khanacademy.org/economics-finance-domain"},
    {"title": "OpenStax – Psychology", "link": "https://openstax.org/subjects/psychology"},
    {"title": "CK-12 – Psychology", "link": "https://www.ck12.org/student/psychology/"},
    {"title": "Crash Course – Psychology", "link": "https://www.youtube.com/user/crashcourse/search?query=psychology"},
    {"title": "National Institute of Mental Health", "link": "https://www.nimh.nih.gov/"},
    {"title": "American Psychological Association – Education", "link": "https://www.apa.org/education"},
    {"title": "BBC Bitesize – Psychology", "link": "https://www.bbc.co.uk/bitesize/subjects/zf4d7ty"},
    {"title": "CK-12 – Economics", "link": "https://www.ck12.org/student/economics/"},
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
