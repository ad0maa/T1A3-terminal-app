# Application Splash Screen 

def app_splash():
    print(' /$$$$$$$$ /$$                 /$$$$$$$$                        /$$$$$$$$                 ')
    print('|__  $$__/|__/                |__  $$__/                       |__  $$__/                 ')
    print('   | $$    /$$  /$$$$$$$         | $$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ ')
    print('   | $$   | $$ /$$_____/         | $$ |____  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$')
    print('   | $$   | $$| $$               | $$  /$$$$$$$| $$               | $$| $$  \ $$| $$$$$$$$')
    print('   | $$   | $$| $$               | $$ /$$__  $$| $$               | $$| $$  | $$| $$_____/')
    print('   | $$   | $$|  $$$$$$$         | $$|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$$')
    print('   |__/   |__/ \_______/         |__/ \_______/ \_______/         |__/ \______/  \_______/')
    print('')
    print('')
    print('Welcome to Tic Tac Toe, Created by Adam Tunchay 2022')
    print('')
    input('Press Enter to Get Started')


# Get Users to input names and store in Dictionary with scores set to zero

user_scores = {}

def player_names():
    p1_name = input('Enter Player One Name: ')
    user_scores.update({p1_name: 0})
    p2_name = input('Enter Player Two Name: ')
    user_scores.update({p2_name: 0})

