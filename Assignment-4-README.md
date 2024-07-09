# Welcome to CFG DRUMS! 

### What is CFG Drums? 

##### CFG Drums offers drums lessons for any level from beginner to advanced. Using this app, the client can see available classes, register for a class if they are an existing student or register as a student.


### Requirements 
<ul>
<li>Flask~=3.0.3</li>
<li>mysql-connector-python~=8.4.0</li>
<li>requests~=2.25.1</li>
</ul>


### Steps
<ol> 
<li>
Edit the 'config.py' file located in the project directory updating the variable with your own MySQL db credentials and save the file
<code>USER = 'your_username'
PASSWORD = 'your_password'
HOST = 'localhost'  # or your database host IP
DATABASE = 'CFGDrums'</code>
</li>
<li>
Install required packages (Flask and mysql.connector):
<code>pip install flask mysql-connector-python</code>
</li>
<li>Save the CFGDrums.sql script and run it on your MySQL Workbench</li>
</ol>


### Running the app 

<ul>
<li>Run the app.py file to start the flask application, which will run on port 500</li>
<li>Run the client_side.py file and follow the instructions in the console</li>
<li>Option 1 will allow you to register to a class if you are an existing student</li>
<li>Option 2 will allow you to register as a student at CFG Drums</li>
<li>When accessing endpoint /classes, you should receive a JSON response listing all available classes</li>
<li>When making a POST request to endpoint /students with valid student details, the student should be registered in the database, and you should receive a success message with the new student's details.</li>
<li>When making a POST request to endpoint /classes/class_id to register a student to a class you should receive a success message and see the number of available spots of that class reducing by 1 </li>
</ul>
