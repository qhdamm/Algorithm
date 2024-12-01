def solution(cap, n, deliveries, pickups):
    # cap: 최대 택배 상자의 개수
    # n: 집의 수
    # deliveries
    # pickups
    init_list = [(i, d, p) for i, (d, p) in enumerate(zip(deliveries, pickups),1)]
    answer = 0
    delivery = 0; pickup = 0;  # 각각 남은 택배 상자 수
    
    while init_list:
        
        i, d, p = init_list.pop()
        delivery += d
        pickup += p
        
        while delivery > 0 or pickup > 0:
            
            delivery -= cap
            pickup -= cap
            
            answer += 2*i
                
    return answer

