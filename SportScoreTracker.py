import sports

def main():
    print('Introducing the Sport Tracker Application!\n')
    print('I can provide you with scores from soccer, basketball, football, and baseball that occured today!\n')
    print('What sport scores would you like to read? (enter a digit)\n')
    print('1. Soccer\n2. Basketball\n3. Football\n4. Baseball')
    sport = input('Please enter a digit from 1-4: ')
    
    while True:
        if sport.isdigit():
            sport = int(sport)
        if sport == "X":
            print('Thank you for using the Sport Tracker Application.')
            break
        else:
            get_scores(sport)
            sport = str(input('Please enter a new digit or X to quit this application: ')) 

def get_scores(sport):
    if sport == 1:
        scores = sports.get_sport(sports.SOCCER)
    elif sport == 2:
        scores = sports.get_sport(sports.BASKETBALL)
    elif sport == 3:
        scores = sports.get_sport(sports.FOOTBALL)
    elif sport == 4:
        scores = sports.get_sport(sports.BASEBALL)
    

    if sport < 5:     
        for score in scores:
            print(score)       

if __name__ == '__main__':
    main()

