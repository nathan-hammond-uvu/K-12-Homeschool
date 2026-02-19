from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load course catalog data
def load_courses():
    with open('K12_Master_Course_Catalog.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    courses = load_courses()
    
    # Extract unique filter options
    categories = sorted(list(set([c['course_category'] for c in courses])))
    levels = sorted(list(set([c['course_level'] for c in courses])))
    school_years = sorted(list(set([c['school_year'] for c in courses if c['school_year']])))
    
    return render_template('index.html', 
                         courses=courses,
                         categories=categories,
                         levels=levels,
                         school_years=school_years)

@app.route('/course/<course_code>')
def course_detail(course_code):
    courses = load_courses()
    course = next((c for c in courses if c['course_code'] == course_code), None)
    
    if course is None:
        return "Course not found", 404
    
    # Generate 15 sample modules
    modules = []
    for i in range(1, 16):
        modules.append({
            'number': i,
            'title': f'Module {i}: {course["course_name"]} Core Concepts',
            'topics': [
                f'Topic {i}.1: Fundamental Concepts',
                f'Topic {i}.2: Practical Applications',
                f'Topic {i}.3: Advanced Techniques'
            ],
            'discussions': [
                f'Discussion {i}.1: Conceptual Understanding',
                f'Discussion {i}.2: Real-World Connections',
                f'Discussion {i}.3: Peer Collaboration'
            ],
            'assignments': [
                f'Assignment {i}.1: Practice Exercises',
                f'Assignment {i}.2: Applied Project',
                f'Assignment {i}.3: Reflection Journal'
            ],
            'quizzes': [
                f'Quiz {i}.1: Comprehension Check',
                f'Quiz {i}.2: Application Assessment',
                f'Quiz {i}.3: Module Mastery'
            ]
        })
    
    return render_template('course_detail.html', course=course, modules=modules)

@app.route('/api/filter')
def filter_courses():
    courses = load_courses()
    
    # Get filter parameters
    category = request.args.get('category', '')
    level = request.args.get('level', '')
    school_year = request.args.get('school_year', '')
    required = request.args.get('required', '')
    search = request.args.get('search', '').lower()
    
    # Apply filters
    filtered = courses
    
    if category:
        filtered = [c for c in filtered if c['course_category'] == category]
    
    if level:
        filtered = [c for c in filtered if c['course_level'] == level]
    
    if school_year:
        if school_year == 'elective':
            filtered = [c for c in filtered if not c['school_year']]
        else:
            filtered = [c for c in filtered if c['school_year'] == school_year]
    
    if required:
        req_bool = required.lower() == 'true'
        filtered = [c for c in filtered if c['is_required'] == req_bool]
    
    if search:
        filtered = [c for c in filtered if 
                   search in c['course_code'].lower() or 
                   search in c['course_name'].lower() or 
                   search in c['course_description'].lower()]
    
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
