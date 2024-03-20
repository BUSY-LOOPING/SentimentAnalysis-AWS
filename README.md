# Sentiment Analysis Flask Server

This project provides a Flask-based server for sentiment analysis using AWS Comprehend service.

## Running on AWS EC2 Instance

If you want to deploy and run the Flask server on an AWS EC2 instance, follow these steps:

1. **Launch an EC2 Instance:**
   - Log in to your AWS Management Console and navigate to the EC2 dashboard.
   - Select Amazon Machine Image (AMI) as Amazon Linux.
   - Select Instance type (t2.micro recommended).
   - Select an appropriate VPC and Subnet.
   - Create a new security group to allow inbound traffic on port 80 (HTTP) and any other necessary ports.

2. **Download Key Pair and Place it within Project Root Folder:**
   - During the EC2 instance launch process, you'll be prompted to download a key pair (.pem file or.ppk file) or create a new one.
   - Download the key pair and ensure it is placed within the project root folder on your local machine.
   - This key pair will be used to authenticate your SSH connections to the EC2 instance.

3. **Launch the EC2 instance:**
    - From the EC2 dashboard, start the new instance.

4. **Connect to Your EC2 Instance:**
   - Use SSH or PuTTY Windows client to connect to your EC2 instance from your local machine.

5. **Install Dependencies:**
   - Once connected to your EC2 instance, install Git and Python 3.9 (if not already installed) using the package manager.
   - Use the following commands for Amazon Linux:

        ```bash
        sudo yum update
        sudo yum install git
        sudo yum install python3
        sudo yum install python3-pip
        ```

6. **Make project directory**
    - Use following command to create a new directory for project files:

        ```bash
        mkdir project1
        ```

7. **Clone the Repository:**
   - Clone your project repository onto the EC2 instance .
   - Use command to clone from git:

        ```bash
        git clone <repository_url> project1
        ```
   - Or use command from local machine's command prompt to upload from local machine [make sure that all the server code is within a directory called `/Server` within the root directory]:

        ```cmd
        scp -i <KEY-PAIR>.pem -r Server/* ec2-user@<PUBLIC-EC2-IP>:/home/ec2-user/project1
        ```

8. **Install Dependencies:**
   - Navigate to the project directory and install the required dependencies using pip:

        ```bash
        sudo pip3 install -r requirements.txt
        ```

9. **Run the Flask Server:**
   - Start the Flask server on the EC2 instance:

        ```bash
        cd project1
        python3 main.py
        ```
    - You should see following output in command line upon successful run of the flask server:

        ```bash
        ====SERVER LIVE====
        ```

9. **Access the Server:**
   - Access the Flask server in your web browser using the public IP address or public DNS name of your EC2 instance.
   - Navigate to `http://<your_ec2_public_ip>:80` to access the server.


## Running on Local Machine

1. **Python Installation (Version 3.9)**

    - Before proceeding with the installation of project dependencies, ensure you have Python 3.9 installed on your system. 
    - Visit the official Python website [python.org](https://www.python.org/downloads/) and download the Python 3.9 installer suitable for your operating system (Windows, macOS, or Linux).

    - Run the downloaded installer and follow the installation wizard instructions. Make sure to check the option to add Python to your system PATH during installation.

    - Once Python 3.9 is installed, you can verify the installation by opening a new command prompt or terminal window and running the following command:

        ```cmd
        python --version
        ```

    - If Python 3.9 is installed correctly, you should see an output similar to the following:

        ```cmd
        Python 3.9.x
        ```

        Note: The `x` represents the patch version number.

2. Make a project directory:

    ```cmd
    mkdir project1
    ```

3. Clone the repository:

    ```cmd
    git clone <repository_url> project1
    ```

4. Navigate to the project directory:

    ```cmd
    cd <project_directory>
    ```

5. Install the required dependencies using pip:

    ```cmd
    pip install -r requirements.txt
    ```

6. Ensure you have AWS credentials set up with access to the AWS Comprehend service. If not, follow the instructions provided by AWS for setting up IAM users and obtaining access keys.

## Usage in Local Machine

1. Run the Flask server:

    ```cmd
    python main.py
    ```

2. Access the server in your web browser at `http://localhost:80`.

3. Enter text into the provided text input field and click the "Analyze" button to perform sentiment analysis.

4. The sentiment analysis result will be displayed on the webpage.

## Example

1. **Install extra dependency**
    - Install BeautifulSoup via pip

        ```
        pip install beautifulsoup4
        ```

2. **Usage**

    - Here's an example of how you can use the server:

        ```python
        import requests
        from bs4 import BeautifulSoup

        url = 'http://127.0.0.1:80/analyze'
        data = {'text': 'This is a great day!'}
        response = requests.post(url, data=data)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            sentiment = soup.find('p')
            sentiment_scores = soup.find_all('li')
            print(f"{sentiment.text}")
            print(f'Sentiment Scores: \n {[senti_score.text for senti_score in sentiment_scores]}')
            
        else:
            print("Error occurred while making the request.")
        ```