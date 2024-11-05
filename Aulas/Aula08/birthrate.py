import random

""""
Monte Carlo methods

1. Establish domain
2. Generate random samples
3. Processing
4. Compute the derived value (counter / number_of_trials)
"""

def prob_two_girls(trials):
    girl_count = 0

    # domain
    for _ in range(trials):
        first_child = random.choices(['boy', 'girl'], weights=[51, 49])[0]
        second_child = random.choices(['boy', 'girl'], weights=[51, 49])[0]

        if first_child == 'girl' and second_child == 'girl':
            girl_count += 1

    return girl_count / trials

def main():
    #print(f"The approximate probability of having two girls is: {prob_two_girls(1000000)*100:.2f}%")
    
    number_of_trials = 1000000
    mean = 5
    
    sum = 0
    for i in range(mean):
        print("\r" + i * ".", end="")
        prob = prob_two_girls(number_of_trials)
        sum += prob
    
    print(f"\rThe mean of the probability is: {sum/5*100:.2f}%")

if __name__ == "__main__":
    main()