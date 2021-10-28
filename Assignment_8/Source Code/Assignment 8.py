def mean(avg):
    if (len(avg) == 0):
        return 0
    else:
        sum = 0.0
        for i in avg:
            sum += i
        return sum/len(avg)

def std(mean, avg):
    sqrt_sum = 0.0
    for i in avg:
        sqrt_sum += (i - mean)**2
    return (sqrt_sum/len(avg))**0.5


def display_scores(test, assignment):
    num_test = len(test)
    num_assignment = len(assignment)
    weight = 0.0
    print('Type               #       min       max       avg       std')
    print('============================================================')
    if (num_test == 0):
        min_test = 'n/a'
        max_test = 'n/a'
        avg_test = 'n/a'
        std_test = 'n/a'
        print('Tests              0       n/a       n/a       n/a       n/a')
    else:
        min_test = min(test)
        max_test = max(test)
        avg_test = mean(test)
        std_test = std(avg_test, test)
        weight += avg_test * 0.6
        print('Tests              %d       %.2f       %.2f       %.2f       %.2f'%(num_test, min_test, max_test, avg_test, std_test))
    if (num_assignment == 0):
        min_assignment = 'n/a'
        max_assignment = 'n/a'
        avg_assignment = 'n/a'
        std_assignment = 'n/a'
        print('Programs           0       n/a       n/a       n/a       n/a')
    else:
        min_assignment = min(assignment)
        max_assignment = max(assignment)
        avg_assignment = mean(assignment)
        std_assignment = std(avg_assignment, assignment)
        weight += avg_assignment * 0.4
        print('Programs           %d       %.2f       %.2f       %.2f       %.2f'%(num_assignment, min_assignment, max_assignment, avg_assignment, std_assignment))
    print()
    print('The weighted score is       %.2f'%(weight))
    print()

if __name__ == '__main__':
    test_scores = []
    assignment_scores = []
    running = True
    while running:
        print('           Grade Menu')
        print('1 - Add Test')
        print('2 - Remove Test')
        print('3 - Clear Tests')
        print('4 - Add Assignment')
        print('5 - Remove Assignment')
        print('6 - Clear Assignments')
        print('D - Display Scores')
        print('Q - Quit')

        print()
        choice = input('==> ')

        if choice == '1':
            print()
            score = float(input('Enter the new test score 0-100 ==> '))
            while score < 0:
                score = float(input('Enter the new test score 0-100 ==> '))
            test_scores.append(score)
            print()
        elif choice == '2':
            print()
            score = float(input('Enter the test to remove 0-100 ==> '))
            removed = False
            for i in test_scores:
                if i == score:
                    test_scores.remove(score)
                    removed = True
            if removed == False:
                print('Could not find that test score to remove')
            print()
        elif choice == '3':
            test_scores.clear()
        elif choice == '4':
            print()
            score = float(input('Enter the new assignment score 0-100 ==> '))
            while score < 0:
                score = float(input('Enter the new assignment score 0-100 ==> '))
            assignment_scores.append(score)
            print()
        elif choice == '5':
            print()
            score = float(input('Enter the assignment to remove 0-100 ==> '))
            removed = False
            for i in assignment_scores:
                if i == score:
                    assignment_scores.remove(score)
                    removed = True
            if removed == False:
                print('Could not find that test score to remove')
            print()
        elif choice == '6':
            assignment_scores.clear()
        elif (choice == 'D' or choice =='d'):
            display_scores(test_scores, assignment_scores)
        elif (choice == 'Q' or choice == 'q'):
            running = False
        else:
            print('Please choose correct option.')