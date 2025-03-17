# My Zootopia API

This project generates a web page displaying information about animals using data fetched from the API Ninjas Animals API.

## Project Structure

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `animals_template.html`: HTML template used to generate the web page.
- `animals_web_generator.py`: Main script to fetch animal data and generate the web page.
- `data_fetcher.py`: Script to fetch animal data from the API.
- `requirements.txt`: Lists the dependencies required for the project.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd My_Zootopia_API
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API key:
    ```env
    API_KEY=your_api_key_here
    ```

## Usage

1. Run the main script:
    ```sh
    python animals_web_generator.py
    ```

2. Enter the name of the animal you want to search for when prompted.

3. The script will generate an `animals.html` file with the fetched animal data.

## Files Description

### [animals_web_generator.py](http://_vscodecontentref_/4)

- [load_data(file_path)](http://_vscodecontentref_/5): Loads JSON data from a file.
- [load_template()](http://_vscodecontentref_/6): Loads the HTML template from a file.
- [serialize_animal(animal)](http://_vscodecontentref_/7): Serializes a single animal's data to HTML.
- [get_animal_data(animal_data)](http://_vscodecontentref_/8): Generates HTML for a list of animals.
- [replace_data(animals_data, page_template)](http://_vscodecontentref_/9): Replaces the placeholder in the template with the animal data.
- [main()](http://_vscodecontentref_/10): Main function to generate the animals HTML.

### [data_fetcher.py](http://_vscodecontentref_/11)

- [fetch_data(animal_name)](http://_vscodecontentref_/12): Fetches the animal data for the given animal name from the API.

## License

This project is licensed under the MIT License.