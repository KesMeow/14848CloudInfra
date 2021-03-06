import os

'''
    Big Data Processing Terminal is a terminal that
    takes user input and provide corresponding user interface
    for user selected tools. 
'''


### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t****************************************************")
    print("\t***  Welcome to the Big Data Processing Toolbox  ***")
    print("\t****************************************************")
    

### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()
while choice != 'q':    
    
    # Let users know what they can do.
    print("\n[1] Apache Hadoop.")
    print("[2] Apache Spark.")
    print("[3] Jupyter Notebook.")
    print("[4] SonarQube and SonarScanner.")
    print("[q] Quit.")
    
    choice = input("What would you like to do? ")
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        print("\nGotcha, I will open Apache Hadoop for you. \n \
        Please use: 35.199.187.51:9870 to access the Apacne Hadoop\n")
    elif choice == '2':
        print("\nSure thing, Apache Spark will be ready momentarily. \n \
        Please use: 34.127.15.221:8080 to access the Apache Spark\n")
    elif choice == '3':
        print("\nJupyter Notebook selected. I will get it ready for you.\n \
        Please use: 35.199.178.167:8888 to access the Jupyter Notebook\n")
    elif choice == '4':
        print("\nI will spin up Sonarqube for you.\n \
        Please use: 34.105.115.19:9000 to access the SonarQube\n")
    elif choice == 'q':
        print("\nThanks for using this toolbox. Bye.")
    else:
        print("\nI didn't understand that choice.\n")