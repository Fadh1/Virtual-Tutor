"""
Bayesian Knowledge Tracing Calculator
Uses PyMC3 to estimate student knowledge level based on quiz performance
"""
import pymc3 as pm
import numpy as np
import random
import theano


def calculate_knowledge_level(num_correct, total_questions=10):
    """
    Calculate estimated knowledge level using Bayesian inference

    Args:
        num_correct: Number of questions answered correctly
        total_questions: Total number of questions (default: 10)

    Returns:
        float: Estimated knowledge level as a percentage (0-100)

    The algorithm:
    1. Generates synthetic performance data based on success rate
    2. Uses Beta distribution as prior for knowledge level (theta)
    3. Applies logistic transformation to model probability of success
    4. Uses Bernoulli likelihood for binary success/failure
    5. Finds Maximum A Posteriori (MAP) estimate of knowledge level
    """
    # Generate synthetic data based on performance
    data_array = np.empty(0)
    success_threshold = (total_questions - num_correct) / total_questions

    # Create 500 virtual attempts to model performance distribution
    for _ in range(500):
        x = random.random()
        if x > success_threshold:
            data_array = np.append(data_array, 1)  # Success
        else:
            data_array = np.append(data_array, 0)  # Failure

    data = theano.shared(data_array)

    # Bayesian Knowledge Tracing Model
    with pm.Model() as model_bkt:
        # Prior: Beta distribution with uniform parameters
        # Represents initial belief about knowledge level
        theta = pm.Beta('Beta', alpha=1, beta=1)

        # Logistic transformation to map knowledge to success probability
        # p(success) = 1 / (1 + exp(-(theta * 10 - 5)))
        p = pm.Deterministic('p', 1.0 / (1 + pm.math.exp(-1 * (theta * 10 - 5))))

        # Likelihood: Bernoulli distribution for binary outcomes
        x = pm.Bernoulli('x', p=p, observed=data)

    # Find Maximum A Posteriori estimate
    map_estimate = pm.find_MAP(model=model_bkt)

    # Convert to percentage
    knowledge_level = map_estimate.get('Beta') * 100

    return knowledge_level
