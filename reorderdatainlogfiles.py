#O(NLogN) Time, O(N) Space
class Solution(object):
    def reorderLogFiles(self, logs):
        letter_list=[]
        digit_list=[]
        for log in logs:
            if log[-1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        letter_list = sorted(letter_list, key=lambda letter: (letter.split()[1:],letter.split()[0]))
        return letter_list+digit_list
