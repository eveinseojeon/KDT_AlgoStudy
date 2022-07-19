
def solution(fees:list,records:list)->list:
    answer = []
    # 1.input을 딕셔너리로 저장
    rc_dict = {}
    for record in records: 
        if record.split()[1] not in rc_dict.keys():
            rc_dict[record.split()[1]] = []
        result = int(record.split()[0].split(':')[0]) * 60 + int(record.split()[0].split(':')[1])
        rc_dict[record.split()[1]].append(result)
    
 
    for c_num in rc_dict.keys(): # 차번호 조회
  
        if len(rc_dict[c_num])%2 != 0: # 차번호에 주차이력이 홀수면 23:59분 추가
            rc_dict[c_num].append(1439)
        
        # 2.누적 주차시간 구하기
        cumsum = 0 # 초기화
        for i in range(0,len(rc_dict[c_num]),2):  # 2step으로 누적 주차시간 계산
          cumsum = cumsum + rc_dict[c_num][i+1]-rc_dict[c_num][i] # i+1 : OUT , i ; IN
        #rc_dict[c_num]=cumsum
         
        # 3.주차 요금 구하기
        #fees[0] : 기본시간, fees[1] : 기본요금 , fees[2] ; 단위 시간, fees[3]; 단위 요금
        if cumsum>fees[0]: #기본시간을 초과할 경우
          rc_dict[c_num] = fees[1] + (math.ceil((cumsum-fees[0])/fees[2])*fees[3])
        else:  #기본 요금일 경우
          rc_dict[c_num] = fees[1]
    
    # 4. 정렬해서 answer 리스트에 담기
    for i in sorted(rc_dict.items()):
      answer.append(i[1])
    return answer

