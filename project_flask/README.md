# Flask Application Template

A modern, fully-featured Flask web application template with Bootstrap 5, complete with responsive design, multiple pages, and best practices.

## Features

- ✅ Modern Flask application structure
- ✅ Bootstrap 5 responsive design
- ✅ Multiple page templates (Home, About, Contact)
- ✅ Error handling (404, 500 pages)
- ✅ Contact form with flash messages
- ✅ Custom CSS with animations
- ✅ JavaScript utilities
- ✅ Environment configuration
- ✅ Ready for development and production

## Project Structure

```
project_flask/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page (welcome page)
│   ├── about.html        # About page
│   ├── contact.html      # Contact page with form
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom styles
    └── js/
        └── main.js       # Custom JavaScript
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd project_flask
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables (optional):**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

## Running the Application

1. **Start the development server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Available Routes

- `/` - Home page (welcome page with features)
- `/about` - About page
- `/contact` - Contact page with form
- Error pages (404, 500) are automatically displayed when needed

## Development

### Adding New Routes

Edit `app.py` to add new routes:

```python
@app.route('/your-route')
def your_function():
    return render_template('your_template.html', title='Your Page')
```

### Creating New Templates

1. Create a new HTML file in the `templates/` directory
2. Extend the base template:
   ```html
   {% extends "base.html" %}
   {% block content %}
       <!-- Your content here -->
   {% endblock %}
   ```

### Customizing Styles

- Edit `static/css/style.css` for custom styles
- The template uses Bootstrap 5 for responsive design
- Custom color variables are defined in CSS root

### Adding JavaScript

- Edit `static/js/main.js` for custom JavaScript
- Bootstrap 5 JavaScript is included via CDN

## Production Deployment

1. **Set environment variables:**
   - Set `SECRET_KEY` to a strong random value
   - Set `DEBUG=False`
   - Configure production database if needed

2. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Set up reverse proxy (nginx/Apache)**

4. **Enable HTTPS with SSL certificate**

## Security Notes

- Change the `SECRET_KEY` in production
- Never commit `.env` file to version control
- Use environment variables for sensitive data
- Enable HTTPS in production
- Set `DEBUG=False` in production

## Technologies Used

- **Backend:** Flask 3.0.0
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Template Engine:** Jinja2
- **Python:** 3.8+

## License

This is a template project. Feel free to use it for your own projects.

## Support

For issues or questions, please refer to the Flask documentation:
- Flask: https://flask.palletsprojects.com/
- Bootstrap: https://getbootstrap.com/

## Next Steps

- Add database integration (SQLAlchemy)
- Implement user authentication
- Add more pages and features
- Configure email sending
- Add form validation
- Implement API endpoints
- Add testing suite
