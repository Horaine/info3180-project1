"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
"""

from forms import ContactForm
import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

###
# Routing the application.
###

@app.route('/profile/')
def profile():
    """Render form to add a new profile."""
    return render_template('profile.html')


@app.route('/profiles/')
def profiles():
    """Render a list of all user profiles in the database."""
    return render_template('profiles.html', name="Mary Jane")
    
    
@app.route('/profile/<userid>')
def userid(userid):
     """Render an individual user profile by the specific user's id."""
     return "User{0}.format(userid)"

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/basic-form', methods=['GET', 'POST'])
def basic_form():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        gender = request.form['gender']
        email = request.form['email']
        location = request.form['location']
        biography = request.form['biography']

        return render_template('form.html',
                               firstname=firstname,
                               lastname=lastname,
                               gender=gender,
                               email=email,
                               location=location,
                               biography=biography,
                               )

    return render_template('form.html')


@app.route('/wtform', methods=['GET', 'POST'])
def wtform():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            firstname = form.firstname.data
            lastname = form.lastname.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data

            flash('You have successfully filled out the form', 'success')
            return render_template('result.html', firstname=firstname, lastname=lastname, email=email)

        flash_errors(form)
    return render_template('wtform.html', form=form)


@app.route('/photo-upload', methods=['GET', 'POST'])

def photo_upload():
    photo = photo()

    if request.method == 'POST' and photo.validate_on_submit():

        photo = photo.photo.data # we could also use request.files['photo']
        description = photo.description.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        return render_template('display_photo.html', filename=filename, description=description)

    flash_errors(photo)
    return render_template('form.html', form=photo)



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404