# from readchar import readchar

from classes import Solution


def main():
    solution = Solution()
    is_won = False
    i = 0
    while i < 6:
        word = input('Guess a word: ')
        res = solution.get_clues(word)
        if res is True:
            print('You won')
            break
        elif res is False:
            print('wait, that\'s illegal')
            i -= 1
        else:
            print(res)
        i += 1
    if not is_won:
        print(solution.guessword)


if __name__ == '__main__':
    main()
