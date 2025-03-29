# How to Start and Run the Scraping Project

## Prerequisites
1. Install [Python](https://www.python.org/downloads/) (version 3.7 or higher).
2. Install `pip`, the Python package manager.
3. Ensure `git` is installed on your system.

## Steps to Start the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/yashahmad/dentons-scraper/git
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Scraper
1. Run the scraper script:
    ```bash
    python main.py
    ```
2. Check the output in the specified directory or database.

## Notes
- Refer to the project documentation for advanced configurations.
- Use `deactivate` to exit the virtual environment when done.
- For troubleshooting, check the logs or enable debug mode.
