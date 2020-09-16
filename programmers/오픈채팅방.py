# def solution(records):
#     peoples_info = []
#     answer = []

#     for record in records:
#         new_record = record.split()
        
#         peoples_info.append(new_record)
#     print(peoples_info)
    
#     for i in range(len(peoples_info)):
#         # if peoples_info[i][0] == "Enter":
#         #     answer.append(peoples_info[i][1] + "/" + peoples_info[i][2] + "님이 들어왔습니다.")
        
#         if peoples_info[i][0] == "Leave":
#             answer.append(peoples_info[i][1] + "/" + peoples_info[i][2] + "님이 나갔습니다.")

#     return answer


#아이디로구별 최종아이디  
#아이디를 키값으로함 유일하니깐

def solution(records):
    answer = []
    peoples_info = {}

    for i in range(len(records)):
        new_record = records[i].split()
        
        if new_record[0] == "Enter":
            peoples_info[new_record[1]] = new_record[2]
        
        if new_record[0] == "Change":
            peoples_info[new_record[1]] = new_record[2]

    for i in range(0,len(records)):
        new_record = records[i].split()

        if new_record[0] == "Enter":
            answer.append(peoples_info[new_record[1]]+"님이 들어왔습니다.")
            
        elif new_record[0] == "Leave":
            answer.append(peoples_info[new_record[1]] + "님이 나갔습니다.")

    return answer







print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

#result : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]