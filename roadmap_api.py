def get_roadmap(role):
    roadmaps = {
        'data_scientist': [
            'Learn Python and R',
            'Understand Data Analysis',
            'Master Machine Learning Algorithms',
            'Get Familiar with Big Data Tools',
            'Work on Real Projects'
        ],
        'web_developer': [
            'Learn HTML, CSS, and JavaScript',
            'Understand Frontend Frameworks like React or Vue',
            'Master Backend Technologies like Node.js, Django, or Flask',
            'Get Familiar with Databases',
            'Work on Real Projects'
        ],
        'machine_learning_engineer': [
            'Learn Python',
            'Understand Machine Learning Algorithms',
            'Master Deep Learning Frameworks like TensorFlow or PyTorch',
            'Get Familiar with Data Engineering',
            'Work on Real Projects'
        ]
        # Add more roles and their roadmaps
    }
    return roadmaps.get(role, [])

