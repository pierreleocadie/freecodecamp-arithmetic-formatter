import re, pprint

def arithmetic_arranger(problems, solve = False):
    PLUS = "+"
    MINUS = "-"
    SPACES_SEP = " "*4
    data_processing = lambda problem, operator: problem.replace(" ", "").split(operator)
    to_return = ""
    top = ""
    bottom = ""
    separators = ""
    results = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        current_operator = ""
        if re.findall("[a-zA-Z]", problem):
            return "Error: Numbers must only contain digits."
        if PLUS in problem:
            current_operator = PLUS
            problem_processing = data_processing(problem, PLUS)
            if len(problem_processing[0]) <= 4 and len(problem_processing[1]) <= 4:
                result = str(int(problem_processing[0]) + int(problem_processing[1]))
                separator = (len(problem_processing[0])+2)*MINUS if len(problem_processing[0]) > len(problem_processing[1]) else (len(problem_processing[1])+2)*MINUS
            else:
                return "Error: Numbers cannot be more than four digits."
        elif MINUS in problem:
            current_operator = MINUS
            problem_processing = data_processing(problem, MINUS)
            if len(problem_processing[0]) <= 4 and len(problem_processing[1]) <= 4:
                result = str(int(problem_processing[0]) - int(problem_processing[1]))
                separator = (len(problem_processing[0])+2)*MINUS if len(problem_processing[0]) > len(problem_processing[1]) else (len(problem_processing[1])+2)*MINUS
            else:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Operator must be '+' or '-'."
        
        if problem != problems[-1]:
            top+=f"{problem_processing[0]:>{len(separator)}}"+SPACES_SEP
            bottom+=f"{current_operator:<1}{problem_processing[1]:>{len(separator)-1}}"+SPACES_SEP
            separators+=f"{separator}"+SPACES_SEP
            results+=f"{result:>{len(separator)}}"+SPACES_SEP
        else:
            top+=f"{problem_processing[0]:>{len(separator)}}\n"
            bottom+=f"{current_operator:<1}{problem_processing[1]:>{len(separator)-1}}\n"
            separators+=f"{separator}\n" if solve else f"{separator}"
            results+=f"{result:>{len(separator)}}"
        
    to_return = top+bottom+separators+results if solve else top+bottom+separators
    return to_return

pprint.pprint(arithmetic_arranger(['3801 - 2', '123 + 49']))

assert arithmetic_arranger(['3801 - 2', '123 + 49']) == '  3801      123\n-    2    +  49\n------    -----', "ERROR"
