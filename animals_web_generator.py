import data_fetcher
import json


def load_data(file_path):
    """
    Load JSON data from file.

    Args:
        file_path (str): Takes path to JSON file.

    Returns:
        dict: The loaded JSON data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)
    

def load_template():
    """
    Load the HTML template from a file.

    Returns:
        str: The content of the HTML template.
    """
    with open('animals_template.html', 'r') as file:
        page_data = file.read()
        return page_data


def serialize_animal(animal):
    """
    Serialize a single animal's data as per instructions to HTML list.

    Args:
        animal (dict): The animal data.

    Returns:
        str: The HTML of animal data.
    """
    animal_name = animal.get('name', 'Unknown')
    animal_diet = animal.get('characteristics', {}).get('diet', 'Unknown')
    animal_location = animal.get('locations', ['Unknown'])[0]
    animal_type = animal.get('characteristics', {}).get('type', 'Unknown')
    
    output = f"""
    <li class="cards__item">
        <div class="card__title"><strong>Name: {animal_name}</strong></div>
        <div class="card__text"><strong>Diet:</strong> {animal_diet}</div>
        <div class="card__text"><strong>Location:</strong> {animal_location}</div>
        <div class="card__text"><strong>Type:</strong> {animal_type}</div>
    </li>"""
    return output


def get_animal_data(animal_data):
    """
    Gen HTML for a list of animals.

    Args:
        animal_data (list): The list of animal data.

    Returns:
        str: The HTML representation of the animal data.
    """
    output = ''
    for animal in animal_data:
        output += serialize_animal(animal)
    return output


def replace_data(animals_data, page_template):
    """
    Replace the placeholder in the template with the animal data.

    Args:
        animals_data (list): The list of animal data.
        page_template (str): The HTML template content.

    Returns:
        str: The updated HTML with the animal data.
    """
    new_data = get_animal_data(animals_data)
    page_template = page_template.replace('__REPLACE_ANIMALS_INFO__', new_data)
    return page_template


def main():
    """
    Main function to gen animals HTML.
    """
    animal_name = input("Please enter an animal to search for: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    page_template = load_template()
    updated_page = replace_data(animals_data, page_template)
    with open('animals.html', 'w') as file:
        file.write(updated_page)

if __name__ == '__main__':
    main()