# Image Comparison API

This is a FastAPI-based microservice that allows you to compare two images and determine if they belong to the same person.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/image-comparison-api.git
```

2. Create a virtual environment and activate it:

- Windows:

```
python -m venv venv
venv\Scripts\activate
```

- macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the server:

```
python main.py
```

2.  The server will start running at `http://localhost:8000`.

## API Endpoints

- `POST /api/compare_images`:

- Compares two images and returns a boolean indicating whether they belong to the same person.

- Request body: `{"image1_url": "...", "image2_url": "..."}`

- Response: `true` or `false`

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
