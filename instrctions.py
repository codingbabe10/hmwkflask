# In this assignment, the focus is on integrating Flask-SQLAlchemy into your existing project to create database models for each resource. You will be creating two database models for each resource and updating your routes to interact with these models, ensuring proper 
# integration with Flask-Migrate for database migrations.






# Use your project's virtual environment.
# Install Flask-SQLAlchemy and Flask-Migrate by running the following commands:

# pip install flask-sqlalchemy flask-migrate




# Make a models.py file in your project.
# Create a database model class for each resource. Define attributes corresponding to the data fields for the resources.
# Ensure that you set up proper relationships between models if needed (e.g., ForeignKey).
# Configure your Flask app with the database URL. Update your app configuration to include SQLAlchemy settings.
# Use Flask-Migrate to create migration scripts and apply them to create tables in the database.
# Run the following commands to initialize and apply migrations:

# flask db init 
# flask db migrate -m "Initial migration" 
# flask db upgrade

# Modify your existing routes to interact with the database models rather than the local data.
# Update CRUD operations to create, read, update, and delete data from the database using the SQLAlchemy models.
# Upload your modified codebase, including the models.py file, to the designated repository.Ensure your Flask app successfully connects to the database and performs CRUD operations using the SQLAlchemy models.Include any additional documentation or comments that explain the integration of Flask-SQLAlchemy and the changes made to interact with the database.
# Consider handling exceptions and errors that may occur during database interactions.
# Test your routes thoroughly to ensure proper integration with the database.
# If you encounter any issues during migration, document the problems faced and the solutions applied.