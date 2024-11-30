from typing import Dict

def solution(today, terms, privacies):
    terms_dict = terms2dict(terms)
    
    answer = []
    for i, privacy in enumerate(privacies):
        in_date, p_type = privacy.split(" ")
        p_period = terms_dict[p_type]
        expdate = date2int(in_date) + 28*p_period

        if date2int(today) >= expdate:
            answer.append(i+1)
    
    return answer

def terms2dict(terms) -> Dict[str, int]:
    terms_dict = {}
    for term in terms:
        t_type, t_period = term.split(" ")
        t_period = int(t_period)
        terms_dict[t_type] = t_period
    return terms_dict
        

def date2int(date) -> int:
    year, month, day = date.split(".")
    year = int(year); month = int(month); day = int(day);
    date_int = 28*(12*year + month) + day
    return date_int



