from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'random2',
        'ptas-unittest'
    ],
)