# passGen 🔑🎲🚀

My take on the ever popular Password Generator!

This is a simple Django web application that generates random passwords using Python's built-in string and secrets modules. The generated passwords can include lowercase and uppercase letters, digits, and punctuation characters.

### [Live Demo](https://pass-gen-gray.vercel.app/)

## Usage

To use the password generator, simply enter the desired password length and select the types of characters you want to include (digits and/or punctuation) using the checkboxes. Then, click the "Generate Password" button to generate a new password.

The app also provides a basic password strength check based on the length and complexity of the generated password. Passwords that are at least 20 characters long and contain at least one punctuation character are considered "strong," while passwords that are at least 10 characters long are considered "medium." Passwords that are shorter than 10 characters are considered "weak."

## Installation

To install and run the app locally, follow these steps:

Clone the repository to your local machine:


```git clone https://github.com/siwhelan/pass_gen.git```

Install the required Python packages:

```pip install -r requirements.txt```

Run the Django development server:

```python manage.py runserver```

Open your web browser and navigate to http://localhost:8000/.

## Screenshot

https://github.com/siwhelan/pass_gen/blob/main/screenshot.PNG

