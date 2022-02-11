def solution(s):
    dict_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    if len(s) >= 1 and len(s) <= 50 and s[0] != '0' and s[0:4] != 'zero':
        # num_list = list(dict_num.keys())
        # for num in num_list:
        #     if num in s:
        #         s = s.replace(num, dict_num[num])
        
        for key, val in dict_num.items():
            s = s.replace(key, val)
        answer = int(s)
        
        if answer < 1 or answer > 2000000000:
            answer = None
        
        return answer
    
print(solution("one4seveneight"))