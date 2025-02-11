# Hacker News Data Visualization

This project retrieves top stories from the Hacker News API, processes the submission data, and visualizes the top 10 most active discussions based on the number of comments. The data visualization is created using Plotly and displays the titles of the top stories as clickable links along with their respective comment counts making it interactive.

## Project Overview

- **Hacker News API**: Fetches the top stories and submission details using Hacker News' API.
- **Data Processing**: Processes the submission data to filter out non-commentable (promotional) posts and sorts the submissions by comment count.
- **Data Visualization**: Uses Plotly Express to create a bar chart that visualizes the top 10 most commented stories on Hacker News.
- **Testing**: Includes tests using Pytest to check if the Hacker News API responds correctly and if the data is in the expected format.

## Installation

To run this project, ensure you have Python 3.9.6 installed, and install the required dependencies using the following steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/MrWang21/Hacker-News-Data-Visualizer.git
    ```

2. Install the dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. To install **Plotly** and **requests** manually, use:
    ```bash
    pip3 install plotly requests
    ```

## Usage

1. **Run the main script**:
    ```bash
    python3 hn_data_visualizer.py
    ```

    This will:
    - Fetch the top stories from Hacker News.
    - Process the data and filter out non-commentable posts.
    - Visualize the top 10 stories with the most comments.

2. **Run tests**:
    To test the API responses and data format, use `pytest`:

    ```bash
    python3 -m pytest
    ```

## Tests

The project includes Pytest tests to ensure the API works as expected and the data is valid:

- **test_status_code**: Ensures the API returns a status code of 200.
- **test_data_format**: Checks if the top stories API returns a list of story IDs.
- **test_submission_status**: Validates the details for the top 5 submissions (checks if they contain the necessary fields like `title` and `descendants`).

## Example Output

When you run the script, a bar chart will appear, showing the **top 10 most active discussions** on Hacker News based on the number of comments. Each bar represents a story, and clicking on the title will redirect you to the specific Hacker News post.

## Dependencies

- `requests`: To make HTTP requests to the Hacker News API.
- `plotly`: For creating the interactive bar chart.
- `pytest`: For running tests and validating API responses.

## License

This project is open-source and available under the MIT License.
