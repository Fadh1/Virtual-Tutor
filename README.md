# Virtual Tutor

An intelligent adaptive learning platform that uses **Bayesian Knowledge Tracing** to personalize educational content and track student mastery across multiple subjects.

## Project Overview

Virtual Tutor was developed as a final year project for the **Bachelor of Computer Science** program at **Nanyang Technological University** (completed April 2020). The platform demonstrates the application of probabilistic machine learning to education, creating a personalized tutoring experience that adapts to each student's knowledge level.

**Author**: Fad Rahim
**Institution**: Nanyang Technological University
**Year**: 2020

## Key Features

### Bayesian Knowledge Tracing
- **Adaptive Difficulty**: Questions automatically adjust based on estimated student mastery
- **Real-time Assessment**: Continuous evaluation of knowledge level using Bayesian inference
- **Personalized Learning Paths**: Content difficulty scales with demonstrated competency
- **Statistical Modeling**: Uses PyMC3 for probabilistic programming and knowledge estimation

### Multi-Subject Support
Comprehensive content coverage across:
- **Mathematics** 
- **Physics**
- **Chemistry**
- **Biology**

### Learning Modes
- **Study Notes**: Review core concepts and theory
- **Practice Sessions**: Reinforce learning with adaptive exercises
- **Assessments**: Test knowledge with intelligent quizzes
- **Progress Tracking**: Monitor improvement over time

## How Bayesian Knowledge Tracing Works

The platform uses a sophisticated probabilistic model to estimate student knowledge:

1. **Prior Belief**: Starts with a uniform Beta distribution representing initial uncertainty
2. **Evidence Collection**: Observes student performance on quiz questions
3. **Bayesian Updating**: Uses Bernoulli likelihood to update knowledge estimates
4. **Logistic Transformation**: Maps latent knowledge to observable success probability
5. **MAP Estimation**: Calculates Maximum A Posteriori estimate of mastery level

The algorithm adapts question difficulty when students demonstrate >70% mastery, ensuring optimal challenge and engagement.

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with Flask-SQLAlchemy ORM
- **Machine Learning**: PyMC3, Theano for Bayesian inference
- **Frontend**: HTML5, CSS3 (Bootstrap), JavaScript (jQuery)
- **Forms**: Flask-WTF with WTForms validation

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Virtual-Tutor.git
   cd Virtual-Tutor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the platform**
   Open your browser and navigate to:
   ```
   http://localhost:4000
   ```

## Usage

1. **Select a Subject**: Choose from Mathematics, Physics, Chemistry, or Biology
2. **Pick a Topic**: Select specific units or concepts to study
3. **Choose Learning Mode**:
   - Study notes for review
   - Practice for skill building
   - Assessment for testing
4. **Take Adaptive Quizzes**: Answer questions and receive real-time knowledge estimates
5. **Progress Through Difficulty Levels**: The system automatically advances you when ready

## Project Structure

```
Virtual-Tutor/
│
├── model/                    # Bayesian Knowledge Tracing logic
│   ├── __init__.py
│   └── calc.py              # BKT calculation engine
│
├── virtualtutor/            # Main application package
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # URL routes and views
│   ├── models.py            # Database models
│   ├── forms.py             # WTForms definitions
│   │
│   ├── static/              # CSS, JavaScript, images
│   │   ├── css/
│   │   └── js/              # Quiz logic, adaptive difficulty
│   │
│   └── templates/           # Jinja2 HTML templates
│       ├── layout.html      # Base template
│       ├── home.html
│       └── ...
│
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

## Algorithm Details

### Bayesian Model Specification

```python
with pm.Model() as model_bkt:
    # Prior: Beta(1,1) - uniform distribution
    theta = pm.Beta('Beta', alpha=1, beta=1)

    # Logistic transformation
    p = pm.Deterministic('p', 1.0 / (1 + exp(-(theta * 10 - 5))))

    # Likelihood: Bernoulli outcomes
    x = pm.Bernoulli('x', p=p, observed=student_data)

# Estimate knowledge level
map_estimate = pm.find_MAP(model=model_bkt)
knowledge_level = map_estimate['Beta'] * 100
```

## Features in Detail

### Adaptive Question Selection
- Initial questions assess baseline knowledge
- Success triggers progression to harder content
- Struggles result in review of fundamentals
- Maintains optimal challenge through Bayesian updates

### Performance Tracking
- Real-time mastery percentage display
- Historical performance data
- Subject-specific progress analytics

## Future Enhancements

Potential improvements for the platform:
- Integration with modern ML frameworks (TensorFlow Probability, PyTorch)
- Expanded question banks with community contributions
- Detailed analytics dashboards
- Mobile responsive design
- Multi-language support
- Collaborative learning features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Nanyang Technological University, School of Computer Science and Engineering
- PyMC3 development team for probabilistic programming tools
- Flask community for excellent web framework documentation

## Contact

**Fad Rahim**
For questions or collaboration opportunities, feel free to reach out!

---

*This project demonstrates the practical application of Bayesian inference to create adaptive educational technology. It showcases skills in full-stack development, machine learning, probabilistic modeling, and software engineering.*
