from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_exam = math_quiz.math_quiz:math_quiz_exam',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        
    ],
)
