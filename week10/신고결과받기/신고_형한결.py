''' 
return : array, id_list에있는 id 순서대로 결과 메일 수 
id_list : array, 이용자 id
report : array, '이용자id 신고한id'
k : int ,  정지기준이 되는 신고 횟수
'''

# 1. 중복 처리하기
def distinct(report_list:list) -> list:
    set_report = report.copy()
    set_report = set(set_report)
    return set_report

# 2. 신고 당한 횟수를 카운트하는 딕셔너리 생성
def cnt_report(id_list:list, report_list:list)->tuple:
    result_dict = {} 
    for id in id_list:
        result_dict[id] = 0
        answer_dict = result_dict.copy()
    for report in report_list:
        result_dict[report.split()[1]] = result_dict[report.split()[1]] +1 
    return answer_dict, result_dict

        
# 3. K 이상일 떄  신고한 사람을 카운트하는 배열 생성
def solution(answer_dict:dict,result_dict:dict, report_list:list, k:int)->list:
    for key,result in result_dict.items():
        if result>=k:
            for report in report_list:
                if key == report.split()[1]:
                    answer_dict[report.split()[0]] = answer_dict[report.split()[0]] + 1
    answer = list(answer_dict.values())            
    return answer


# 정답 코드
def solution(id_list, report_list, k):
    report_list = set(report_list)
    result_dict = {}
    for id in id_list:
        result_dict[id] = 0
        answer_dict = result_dict.copy()
    for report in report_list:
        result_dict[report.split()[1]] = result_dict[report.split()[1]] +1 
    for key,result in result_dict.items():
        if result>=k:
            for report in report_list:
                if key == report.split()[1]:
                 answer_dict[report.split()[0]] = answer_dict[report.split()[0]] + 1
    answer = list(answer_dict.values())          
    return answer

# 정확성: 91.7
