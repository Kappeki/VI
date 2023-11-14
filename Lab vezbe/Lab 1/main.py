# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def unija(list1, list2):
    return list(set(list1 + list2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1 = [5, 4, '1', '8', 7]
    l2 = [1, 9, '1']

    print(unija(l1, l2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
