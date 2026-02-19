# K-12 Course Catalog Web Application

A Flask-based interactive web application for browsing and exploring K-12 course offerings with advanced filtering and search capabilities.

## Features

- 📇 **Interactive Course Cards** - Browse all courses in an attractive card layout
- 🔍 **Real-time Search** - Search across course codes, names, and descriptions
- 🎛️ **Advanced Filtering** - Filter by category, level, school year, and required status
- 📄 **Detailed Course Pages** - View comprehensive course information with 15 modules
- 💻 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Clean, professional interface built with Bootstrap 5

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download this repository** to your local machine

2. **Navigate to the project directory**
   ```bash
   cd path/to/your/project
   ```

3. **Install required Python packages**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Ensure all files are in place**
   - `app.py`
   - `K12_Master_Course_Catalog.json`
   - `requirements.txt`
   - `templates/` folder with HTML files
   - `static/` folder with CSS and JS files

2. **Start the Flask application**
   ```bash
   python app.py
   ```

3. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

4. **To stop the server**, press `Ctrl+C` in the terminal

## Project Structure

```
/
├── app.py                              # Flask application main file
├── requirements.txt                     # Python dependencies
├── README.md                           # This file
├── K12_Master_Course_Catalog.json      # Course data
├── course_template.md                  # Course template reference
├── templates/                          # HTML templates
│   ├── base.html                       # Base template
│   ├── index.html                      # Homepage with course cards
│   └── course_detail.html              # Individual course page
└── static/                             # Static assets
    ├── css/
    │   └── style.css                   # Custom styles
    └── js/
        └── script.js                   # JavaScript functionality
```

## Usage Guide

### Browsing Courses

- The homepage displays all available courses as interactive cards
- Each card shows the course code, name, description, category, level, and required status
- Click on any card or the "View Details" button to see full course information

### Filtering Courses

Use the left sidebar to filter courses by:

- **Category**: English Language Arts, Mathematics, STEM, Fine Arts, etc.
- **Level**: Introductory, Intermediate, Advanced, Advanced Placement
- **School Year**: Preschool, 9th, 12th, or Electives
- **Course Type**: Required courses or Electives only

Multiple filters work together to narrow your results. Click "Clear Filters" to reset all filters.

### Searching

- Use the search bar at the top of the sidebar
- Search terms match against course code, name, and description
- Search works in combination with active filters

### Viewing Course Details

Course detail pages include:

- Complete course information and metadata
- Learning objectives
- 15 detailed modules with topics, discussions, assignments, and quizzes
- Final exam and capstone project information
- Easy navigation back to the catalog

## Customization

### Changing the Port

Edit `app.py` and modify the last line:
```python
app.run(debug=True, port=5000)  # Change 5000 to your preferred port
```

### Modifying Course Data

Edit `K12_Master_Course_Catalog.json` to add, remove, or modify courses.

### Styling

Customize the appearance by editing `static/css/style.css`.

### Module Generation

The course detail page generates 15 sample modules. To customize this, edit the `course_detail` function in `app.py`.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, either:
- Stop the application using that port
- Change the port in `app.py` (see Customization section)

### Module Not Found

If you get import errors, ensure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### Template Not Found

Ensure the `templates/` folder is in the same directory as `app.py`.

### Static Files Not Loading

Ensure the `static/` folder structure is correct and in the same directory as `app.py`.

## Technical Details

- **Framework**: Flask 3.0.0
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.4.0
- **Template Engine**: Jinja2
- **JavaScript**: Vanilla JS (no additional frameworks required)
- **Python Version**: 3.7+

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please check:
1. All files are in the correct locations
2. Python dependencies are installed
3. The JSON file is valid
4. The Flask server is running without errors

---

**Enjoy exploring your K-12 Course Catalog!** 🎓
