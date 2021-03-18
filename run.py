from jsjobs_app import app, db
from jsjobs_app.models import Company

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Company': Company}