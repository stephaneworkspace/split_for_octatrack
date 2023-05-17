# This is a sample Python script.
from split_wav import SplitWav


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    folder = '/Users/stephane/Liveact/dnb01/non_master'
    file = 'octa-export-dnb01-01-44100.wav'
    split_wav = SplitWav(folder, file)
    #split_wav.multiple_split(min_per_split=0.109714285714286000000000000000)
    split_wav.multiple_split_bar(175,8)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
