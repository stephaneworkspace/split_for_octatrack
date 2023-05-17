from split_wav import SplitWav
import sys

if __name__ == '__main__':
    print('Split for octatrack')
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i == 1:
            folder = arg
        if i == 2:
            file = arg
        if i == 3:
            bpm = int(arg)
        if i == 4:
            bars = int(arg)
        print(f"Argument {i:>6}: {arg}")
    #folder = '/Users/stephane/Liveact/dnb01/non_master'
    #file = 'octa-export-dnb01-01-44100.wav'
    split_wav = SplitWav(folder, file)
    #split_wav.multiple_split_bar(bpm=175, bars=8*4)
    split_wav.multiple_split_bar(bpm=bpm, bars=bars)