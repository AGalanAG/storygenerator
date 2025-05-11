from flask import Flask, render_template, jsonify
from fantasy_story_generator import FantasyStoryGenerator
import os

app = Flask(__name__)

# Initialize the FantasyStoryGenerator
generator = FantasyStoryGenerator()
stories_dir = "path/to/your/stories/directory"  # Update this path
training_texts = generator.load_training_texts(stories_dir)
generator.train_markov(training_texts)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-story')
def generate_story():
    story = generator.generate_story()
    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True)