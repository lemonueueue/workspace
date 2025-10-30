from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration
app.config['DEBUG'] = True

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically process the form data
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', title='Contact')

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """500 error handler"""
    return render_template('500.html', title='Server Error'), 500

