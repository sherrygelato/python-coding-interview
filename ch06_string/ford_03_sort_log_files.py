#!/usr/bin/python3
"""
CH06. 03_Recorder_Log_Files
"""

logs = ["dig1 8 1 5 1", "let1 art can", 
        "dig2 3 6", "let2 own kit dig", 
        "let3 art zero"]


# --------------------------------------------------
def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        # digit 과 letters를 분리
        if log.split()[1].isdigit():
            digits.append(log)
            print('digits:', digits)
        else:
            letters.append(log)
            print('letters:',letters)
    
    # letters인 경우에만 다시 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


print(reorderLogFiles(logs))
