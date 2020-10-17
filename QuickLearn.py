import pandas as pd
from sklearn.model_selection import train_test_split as tts


def user_entry_check(expected, entered, operation):
    if entered in expected:
        return 1
    elif entered.lower() == "exit":
        print("\nProgram terminated\nYou chose to exit")
        exit()
    else:
        if operation == 1:  # Use when working with columns
            print("\nALERT:-\n=====")
            print("* Please, make sure you entered the column name correctly.")
            print("* You should enter only one dependent column.")
            print("\nPlease enter a valid input:-")
        if operation == 2:  # Use when operating menu tasks
            print("Please enter a valid input:-")
        return 0


def check_input(condition_list, operation):
    while 1:
        input_value = str(input())
        if user_entry_check(condition_list, input_value, operation):
            break
    return input_value


def address_check(address):
    try:
        pd.read_csv(address)
        return 1
    except FileNotFoundError:
        print("\nYou entered a wrong address. Please, type the address again.")
        print("Type below:- ")
        return 0


def location_input():
    print("\nEnter the address of the file:\n")
    while 1:
        address = str(input())
        if address_check(address):
            break
    return address


def main_file(signal):
    location = location_input()
    file = pd.read_csv(location)

    def selector(data):
        print("\nThe dataset you entered contains this following data:-")
        print(data.head(5))
        column_list = data.columns.tolist()
        print("\nThe name of the columns in this dataset are as follows:")
        print(column_list)
        print("\nWhich of the above mentioned column is the dependent column?\n")
        label = check_input(column_list, signal)
        y_data = data[label]
        predictors = data.drop(label, axis=1)
        return predictors, y_data
    return selector(file)


def param(data_x, data_y, parameters):
    if parameters in ['', ' ']:
        return 1
    else:
        # Types of error that can occur
        # 1. NameError
        # 2. ValueError
        # 3. TypeError
        # 4. AttributeError
        # 5. SyntaxError

        try:
            eval(str("tts(data_x, data_y, " + parameters + ")"))
            return 1
        except (NameError, ValueError, TypeError, AttributeError, SyntaxError):
            print("\nYou made a mistake while typing the parameters. Please, type gain.")
            print("Enter the parameter below:-")
            return 0


def splitter(data_x, data_y):
    while 1:
        parameters = str(input())
        if param(data_x, data_y, parameters):
            break
    return parameters


def preprocessing(train_x, test_x, train_y, test_y):
    table = [train_x, test_x, train_y, test_y]
    print("\nDo you want to perform preprocessing in the data or move to Machine Learning?")
    print("1. Perform preprocessing operations.\n2. Move to learning.")


# Operation Signals
signal1, signal2 = 1, 2  # 1 for column operations, 2 for menu tasks
# Applying settings for pandas
pd.set_option('display.max_columns', None)


# Initialization
print("\nWelcome to QML / QuickLearn. Your personal program to find your best model.")
print("==========================================================================")
X, y = main_file(signal1)
print("\nThe predictors / features of this dataset are as follows:- ")
print("============================================================")
print(X.columns.to_list())
print("\nShape of predictors / features: ", X.shape)
print("Shape of label: ", y.shape)
print("\nTRAIN TEST SPLIT\n================")
print("Enter the parameters for train_test_split function.")
print("\nYou don't have to enter the X and y\n"
      "since you already selected them before.")
print("\nFor example type the parameters like this:- test_size=0.2, train_size=0.8")
print("Or simply press enter if you want go with default settings.")
print("\nGive your input here:- ")
split_param = splitter(X, y)
X_train, X_test, y_train, y_test = eval(str("tts(X, y, " + split_param + ")"))
print("\nYour data split is complete:- ")
print("==============================")
print("\nShape of training predictors: ", X_train.shape)
print("Shape of testing predictors: ", X_test.shape)
print("Shape of training labels: ", y_train.shape)
print("Shape of testing labels: ", y_test.shape)


def offer(train_x, test_x, train_y, test_y, operation):
    print("\nDo you want to preprocess the data before modeling?")
    print("Type [y] for yes and [n] for no.")
    options = ['y', 'Y', 'n', 'N']
    choice = check_input(options, operation)
    if choice.lower() == 'y':
        preprocessing(train_x, test_x, train_y, test_y)
    else:
        print('1')


offer(X_train, X_test, y_train, y_test, signal2)
