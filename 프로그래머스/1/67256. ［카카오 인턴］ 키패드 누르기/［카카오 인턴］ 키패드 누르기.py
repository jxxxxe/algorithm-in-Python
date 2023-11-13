def solution(numbers, hand):
    answer = ''
    
    cur_xy_l = [-1,0]
    cur_xy_r = [1,0]
    xy = [(0,0)]
    
    x = [-1,0,1]
    for i in range(9):
        xy.append((x[i%3], 3-i//3))
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            cur_xy_l = xy[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            cur_xy_r = xy[number]
        else:
            target_x, target_y = xy[number]
            distance_l = abs(target_x - cur_xy_l[0]) + abs(target_y - cur_xy_l[1])
            distance_r = abs(target_x - cur_xy_r[0]) + abs(target_y - cur_xy_r[1])
            if distance_l > distance_r:
                answer += 'R'
                cur_xy_r = xy[number]
            elif distance_l < distance_r:
                answer += 'L'
                cur_xy_l = xy[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_xy_l = xy[number]
                else:
                    answer += 'R'
                    cur_xy_r = xy[number]
            
    return answer