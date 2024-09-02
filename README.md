
MCQ Generator with spaCy
Description
The MCQ Generator script creates multiple-choice questions (MCQs) from input text using the spaCy library for natural language processing. It extracts key information from sentences to generate questions, making it a useful tool for educators, content creators, and quiz developers.

Features
Automatic MCQ Creation: Generates questions based on noun extraction.
Distractor Options: Includes randomly selected distractors for a more challenging quiz.
Customizable Question Count: Allows specification of the number of MCQs to generate.
Randomization: Randomly selects sentences and distractors to vary the output.
Requirements
Ensure you have the following Python packages installed:

spacy: For NLP tasks.
random: For randomization functions (included in the Python Standard Library).
You can install spaCy and the required model with the following commands:

bash
Copy code
pip install spacy
python -m spacy download en_core_web_sm
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/utkarshkumar26/Career-Recommendation-Syst3https://github.com/yourusername/mcq-generator.git
cd mcq-generator
Install Dependencies:

Install any required packages using pip:

bash
Copy code
pip install -r requirements.txt
Create a requirements.txt file with the following content:

Copy code
spacy
Download spaCy Model:

Download the English language model used in the script:

bash
Copy code
python -m spacy download en_core_web_sm

Code Explanation
Import Libraries:

spacy: For natural language processing tasks.
Counter: To count noun occurrences.
random: For random sampling and shuffling.
Load spaCy Model:

nlp = spacy.load("en_core_web_sm"): Loads the English language model.
Generate MCQs Function:

Extract Sentences: Breaks the text into sentences.
Select Sentences: Randomly chooses sentences to form questions.
Process Sentences: Extracts nouns and counts their occurrences.
Create MCQs: Replaces the most common noun with a blank, generates answer choices, and shuffles them.
Testing the Function:

The sample text provided tests the generate_mcqs function, outputting questions with options.
