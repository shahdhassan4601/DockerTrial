# Word Frequency Analysis using Docker

This project utilizes Docker to perform word frequency analysis on a given text file. It includes a Python script for analyzing the frequency of words in the text, and a Dockerfile for containerization.

## Table of Contents

- [Project Structure](#project-structure)
- [Instructions](#instructions)
  - [Setup](#setup)
  - [Usage](#usage)
- [Additional Notes](#additional-notes)
- [Files in Repository](#files-in-repository)
- [License](#license)

## Project Structure

- **main.py**: Python script for word frequency analysis.
- **requirements.txt**: File listing the required Python packages.
- **Dockerfile**: Configuration file for building the Docker image.
- **random_paragraphs.txt**: Sample text file for analysis.
- **word_frequency.txt**: Output file containing word frequency counts.
- **.dockerignore**: Specifies files to be ignored during Docker builds.
- **.gitignore**: Specifies files to be ignored by Git.
- **LICENSE**: License information for the project.
- **README.md**: Documentation file (you're reading it!).

## Instructions

### Setup

1. Clone the repository: `git clone https://github.com/your_username/Word-Frequency-Analysis-using-Docker.git`
2. Navigate to the project directory: `cd Word-Frequency-Analysis-using-Docker`

### Usage

1. Place the text file you want to analyze in the project directory and name it `random_paragraphs.txt`.
2. Build the Docker image:
```bash
docker build -t word-frequency-analysis 
```
3. Run the Docker container:
To run the Docker container, you have two options:

1. **Simple Run**: If you have set up your Dockerfile to include all the necessary files and dependencies, you can use the following command:
   
```bash
docker run word-frequency-analysis
```
This command will run the container without any additional options. It assumes that all required files are already present inside the container.

2. **Advanced Options**: If you need to customize the container execution, you can use additional options. For example:

```bash
docker run --rm -v $(pwd):/app word-frequency-analysis
```
- `--rm`: Removes the container after it exits. Useful for temporary containers.
- `-v $(pwd):/app`: Mounts the current directory to /app inside the container. Useful for accessing files from the host machine or persisting data.

Choose the option that best fits your requirements and use case.

The word frequency analysis will be performed on the text file, and the results will be stored in `word_frequency.txt`.

## Additional Notes

- The Python script tokenizes the text, removes stopwords, punctuation, single-character tokens, and tokens containing digits.
- It then counts the frequency of each word and exports the results to `word_frequency.txt`.
- You can customize the list of stopwords and additional tokens to be filtered out in the script (`main.py`).
- This project serves as a simple demonstration of using Docker for text analysis tasks.

## Files in Repository

- **.dockerignore**: Specifies files to be ignored during Docker builds.
- **.gitignore**: Specifies files to be ignored by Git.
- **LICENSE**: License information for the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
