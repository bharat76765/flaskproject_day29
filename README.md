# flaskproject_day29
# Flask Technical Roles Roadmap Project

This repository contains a Flask project that serves as both a client and an API provider for showcasing roadmaps of various technical roles.

## Project Structure

- **Client Application (`app.py`)**
  - Displays a homepage where users can select a technical role from a dropdown menu.
  - Upon selection, it fetches the corresponding roadmap image from the API and displays it.
  
- **API Service (`app(1).py`)**
  - Provides an API endpoint to serve roadmap images based on the selected technical role.

## Technical Roles

The following technical roles are included in the project, each with its own roadmap:

- Data Science
- Database Administrator
- Analyst
- Information Technology Management
- Web Developer
- Application Developer
- Software Architect
- Computer Network Architects
- DevOps Engineer
- Data Engineer
- Java Developer
- Artificial Intelligence
- Network Administrator
- Software Engineer
- User Experience Design
- Full Stack Developer
- Information Security Analysts
- IT Security Specialist
- Product Management
- Cloud Engineer
- Support Specialist
- Blockchain Engineer
- Computer Programmer

## Installation and Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/bharat76765/flaskproject_day29.git
    cd flaskproject_day29
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/Scripts/activate  # On Windows
    # source .venv/bin/activate    # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. Start the API service:
    ```sh
    python app(1).py
    ```

2. Start the client application in a separate terminal:
    ```sh
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000` to access the client application.

## Usage

1. On the homepage, select a technical role from the dropdown menu.
2. Click the "Get Roadmap" button to fetch and display the roadmap for the selected role.
3. Use the "Back to Home" link to return to the homepage and select another role.

## API Details

- **Endpoint:** `/api/roadmap`
- **Method:** `GET`
- **Parameters:**
  - `role` (string): The technical role for which the roadmap is requested.
- **Response:**
  - Returns the URL of the roadmap image for the specified role.

## .gitignore

The `.gitignore` file is configured to exclude unnecessary files such as:
- Virtual environment directories
- Python cache files
- IDE configuration files

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
