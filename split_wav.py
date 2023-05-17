from pydub import AudioSegment
import math


class SplitWav():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def single_split_ms(self, from_ms, to_ms, split_filename):
        t1 = from_ms * 1000
        t2 = to_ms * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')

    def multiple_split_bar(self, bpm, bars):
        total_mins = self.get_duration()
        print(total_mins)
        one_beat_ms = (60 / bpm) * 1000
        bars_s = (one_beat_ms * bars * 4) / 1000
        elements = math.ceil(total_mins / bars_s)
        print(bars_s)
        print(elements)
        i = 1
        while i <= elements:
            split_fn = str(i) + '_' + self.filename
            self.single_split_ms((i - 1) * bars_s, i * bars_s, split_fn)
            print(str(i) + ' Done')
            if i == elements:
                print('All splited successfully')
            i += 1
