# pulseid-ui-automation
QA Automation assessment for PulseId

### Prerequisites

- [Python v3.8.0](https://www.python.org/downloads/) up to the latest version
- [Pip, Pip3 and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) Community IDE
- Selenium drivers: [Chromedriver](https://chromedriver.chromium.org/downloads)

### Setup instructions:

1. Create a folder named "pulseid-automation". 
2. Inside pulseid-automation folder, clone this repository.
3. Inside the same folder, create a virtual environment.
4. Go to the pulseid-ui-automation folder and activate virtual environment using the command
`source ../<venv_name>/bin/activate`.
5. Install python libraries by entering the command `pip install -r requirements.txt`.
6. Create a folder named "driver" inside the pulseid-ui-automation folder and move downloaded chrome drivers. `Note: Make sure you download the same version on your current chrome browser`

You may also set the project's virtual environment and install python libraries in PyCharm > Preferences... > Project > Project Interpreter.

### Running the feature files:
1. Make sure your virtual environment is activated.
2. Entering the command behave to run all the feature files.
	a. On [behave] section in behave.ini file you may set specific feature file and run the command on your terminal:
	```
	behave
	```
	b. To generate an allure report run and execute the following command on your terminal
	
	- To run your test set in in behave.ini, execute:
		```
		behave -f allure -o allure-results -f pretty 
		```
	- To generate allure reports after executing the test, execute:
		```
		allure generate allure-results -o allure-reports
		```
	- To view the reports execute:
		```
		allure open allure-reports
		```
		
	
	
