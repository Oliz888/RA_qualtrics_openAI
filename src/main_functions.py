from imports import *  # Import necessary modules

import time
import openai
import logging
import re
import plotly.graph_objects as go

# Function to evaluate comments using OpenAI API
def get_evaluation(comment):
    # Create the evaluation prompt
    prompt = (
        f"Evaluate the following comment: \"{comment}\" "
        "and provide an estimate for each dimension:\n"
        "Discrimination (on a scale of 1 to 10):\n"
        "Political Inclination (on a scale of 1 to 10):\n"
        "Source Credibility (on a scale of 1 to 10):\n"
        "Public Perception (on a scale of 1 to 10):\n"
        "Emotional Appeal (on a scale of 1 to 10):"
    )

    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            logging.info(f"Evaluating comment: {comment}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an assistant who evaluates comments on various dimensions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )

            evaluation_result = response['choices'][0]['message']['content'].strip()
            logging.info("Evaluation successful")

            # Debug: Print raw evaluation result to see the format
            print(f"Raw evaluation result for comment '{comment}':\n{evaluation_result}")
            return evaluation_result

        except openai.error.RateLimitError:
            retries += 1
            logging.warning(f"Rate limit reached. Retrying in 60 seconds... (Attempt {retries}/{max_retries})")
            time.sleep(60)

        except openai.error.InvalidRequestError as e:
            logging.error(f"Invalid request error: {e}")
            return "Error: Invalid request"

        except openai.error.AuthenticationError:
            logging.error("Authentication error: Invalid API key.")
            return "Error: Authentication failed"

        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return "Error in evaluation"

    logging.error("Max retries reached. Evaluation failed.")
    return "Error: Max retries reached"


# Function to extract numerical scores from the evaluation result
def extract_scores(evaluation_text):
    # Debug: Print the evaluation text to inspect the format
    print(f"Extracting scores from evaluation text:\n{evaluation_text}")

    # Regex pattern to match "Dimension: X/10" where X is a number
    # This will match both bullet point format and inline text format
    pattern = re.compile(r'(Discrimination|Political Inclination|Source Credibility|Public Perception|Emotional Appeal)[^\d]*(\d+)/10')

    scores = {match[0]: int(match[1]) for match in pattern.findall(evaluation_text)}

    # Debug: Print the extracted scores
    print(f"Extracted Scores: {scores}")
    
    return scores


# Function to plot radar chart for comparison of two comments
def plot_radar(comment1_scores, comment2_scores):
    dimensions = list(comment1_scores.keys())
    comment1_values = list(comment1_scores.values())
    comment2_values = list(comment2_scores.values())

    fig = go.Figure()

    # Add first comment to radar plot
    fig.add_trace(go.Scatterpolar(
        r=comment1_values,
        theta=dimensions,
        fill='toself',
        name='Comment 1'
    ))

    # Add second comment to radar plot
    fig.add_trace(go.Scatterpolar(
        r=comment2_values,
        theta=dimensions,
        fill='toself',
        name='Comment 2'
    ))

    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10])
        ),
        showlegend=True,
        title="Radar Chart Comparison of Two Comments"
    )

    # Show the radar chart
    fig.show()


# Function to compare two comments and plot radar chart
def compare_two_comments(comment1, comment2):
    # Evaluate both comments
    eval1 = get_evaluation(comment1)
    eval2 = get_evaluation(comment2)

    # Extract the scores
    scores1 = extract_scores(eval1)
    scores2 = extract_scores(eval2)

    # Print extracted scores for debugging
    print("Comment 1 Scores:", scores1)
    print("Comment 2 Scores:", scores2)

    # Plot the radar chart for comparison
    plot_radar(scores1, scores2)


