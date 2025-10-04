from main_2 import logger


path = 'list_of_list.log'

@logger(path)
def flat_generator(list_of_list):
    for value in list_of_list:
        if isinstance(value, list):
            yield from flat_generator(value)
        else:
            yield value

if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print(list(flat_generator(list_of_lists_2)))
