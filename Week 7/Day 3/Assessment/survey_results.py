# Survey results listing respondents with multiple question answers

# Survey data in a nested dictionary format
survey_results = [
    {'respondent_id': 1, 'age': 25, 'responses': {'Q1': 'Yes', 'Q2': 'No', 'Q3': 'Maybe'}},
    {'respondent_id': 2, 'age': 30, 'responses': {'Q1': 'No', 'Q2': 'Yes', 'Q3': 'Yes'}},
    {'respondent_id': 3, 'age': 22, 'responses': {'Q1': 'Maybe', 'Q2': 'Maybe', 'Q3': 'No'}}
]

# Function to display all survey results
def display_survey_results(results):
    for respondent in results:
        print(f"Respondent ID: {respondent['respondent_id']}, Age: {respondent['age']}")
        for question, answer in respondent['responses'].items():
            print(f"  {question}: {answer}")
        print()

# Function to add a new respondent
def add_respondent(results, respondent_id, age, responses):
    results.append({'respondent_id': respondent_id, 'age': age, 'responses': responses})
    print(f"Added respondent ID: {respondent_id}")

# Function to remove a respondent by ID
def remove_respondent(results, respondent_id):
    for i, respondent in enumerate(results):
        if respondent['respondent_id'] == respondent_id:
            results.pop(i)
            print(f"Removed respondent ID: {respondent_id}")
            return
    print(f"Respondent ID {respondent_id} not found.")

# Function to update a respondent's answer to a question
def update_response(results, respondent_id, question, new_answer):
    for respondent in results:
        if respondent['respondent_id'] == respondent_id:
            respondent['responses'][question] = new_answer
            print(f"Updated respondent ID {respondent_id}'s answer to {question} to {new_answer}")
            return
    print(f"Respondent ID {respondent_id} not found.")

# Function to display a single respondent's details
def display_respondent(results, respondent_id):
    for respondent in results:
        if respondent['respondent_id'] == respondent_id:
            print(f"Respondent ID: {respondent['respondent_id']}, Age: {respondent['age']}")
            for question, answer in respondent['responses'].items():
                print(f"  {question}: {answer}")
            return
    print(f"Respondent ID {respondent_id} not found.")

# Function to display results for a specific question across all respondents
def display_question_results(results, question):
    print(f"Results for {question}:")
    for respondent in results:
        answer = respondent['responses'].get(question, 'No response')
        print(f"  Respondent ID {respondent['respondent_id']}: {answer}")
    print()

# Example usage
display_survey_results(survey_results)
remove_respondent(survey_results, 2)
print("\nAfter removal:")
display_survey_results(survey_results)
add_respondent(survey_results, 4, 28, {'Q1': 'Yes', 'Q2': 'No', 'Q3': 'Yes'})
print("\nAfter adding respondent ID 4:")
display_survey_results(survey_results)
update_response(survey_results, 1, 'Q2', 'Yes')
print("\nAfter updating respondent ID 1's response to Q2:")
display_survey_results(survey_results)
print("\nDisplaying respondent ID 3's details:")
display_respondent(survey_results, 3)
print("\nDisplaying results for Q1:")
display_question_results(survey_results, 'Q1')
print("\nDisplaying results for Q2:")
display_question_results(survey_results, 'Q2')