

"""
Run script for Virtual Tutor application
Start the Flask development server
"""
from virtualtutor import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
