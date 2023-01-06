from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    second = 0

    while True:
        print(truck_weights, second, bridge)
        if len(truck_weights) == 0 and sum(bridge) == 0:
            return second

        top = 0
        if truck_weights:
            top = truck_weights[0]

        second += 1
        bridge.pop()
        bridge.appendleft(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                cur_truck = truck_weights.pop(0)
                bridge[0] = cur_truck
            else:
                bridge[0] = 0

    return second


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
