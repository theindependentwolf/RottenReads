## Rotten Reads - A book review website 

Running Live on www.rottenreads.com

### Environment

1. This was done on MacOSX and the instructions will be very similar for Linux environments.
2. Python version 3+
3. Python virtualenv - Create a virtual environment with python3

### Set up Instructions

1. Clone the repository
2. Requirements found in the requirement.txt file
   pip install -r requirements.txt
3. Apply the contents of .env file to your environment (Environment Variables) or use venv
4. Install Postgresql or a relational DB of your choice
5. Run the application using 
   python rottenreads.py
6. Open the application on your localhost on port 5000
   localhost:5000
7. Docker file can be found in the repository, although it has not been fully tested. 


### Testing

1. Application has undergone thorough User Acceptance Testing.
2. Unit tests to be added.


### To be Added

1. Pagination
2. Images for books
3. Proper Authentication
4. Search function
