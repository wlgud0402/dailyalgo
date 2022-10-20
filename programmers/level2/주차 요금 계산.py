from datetime import datetime
from math import ceil

# 시간, 상태 (IN, OUT), 분


def solution(fees, records):
    parking_lot = {}
    for record in records:
        time, car_number, status = record.split()
        if car_number not in parking_lot:
            parking_lot[car_number] = {
                "total_minute": 0,
                "status": "IN",
                "time": time
            }
            continue

        if status == "IN":
            parking_lot[car_number]["status"] = "IN"
            parking_lot[car_number]["time"] = time
            continue

        elif status == "OUT":
            car_in_time = datetime.strptime(
                parking_lot[car_number]["time"], "%H:%M")
            car_out_time = datetime.strptime(time, "%H:%M")

            minute_diff = calculate_time_diff(car_in_time, car_out_time)
            parking_lot[car_number]["total_minute"] += minute_diff
            parking_lot[car_number]["status"] = "OUT"

    # fees = [180, 5000, 10, 600]
    # 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
    #     180	    5000	      10	       600
    result = []
    parking_lot = sorted(parking_lot.items(), key=lambda x: x[0])
    for car_number, car in parking_lot:
        car = calculate_extra_time(car)
        total_fee = calculate_fee(car["total_minute"], fees)
        result.append(total_fee)
    return result


def calculate_fee(car_total_minute, fees):
    basic_minute = fees[0]
    basic_charge = fees[1]
    per_time = fees[2]
    per_charge = fees[3]
    total_fee = 0
    if car_total_minute <= basic_minute:
        total_fee = basic_charge
    else:
        total_fee = basic_charge + \
            ceil((car_total_minute - basic_minute) / per_time) * per_charge
    return total_fee


def calculate_time_diff(car_in_time, car_out_time):
    minute_diff = (car_out_time.timestamp() - car_in_time.timestamp()) / 60
    return minute_diff


def calculate_extra_time(car):
    if car["status"] == "IN":
        car_out_time = datetime.strptime("23:59", "%H:%M")
        car_in_time = datetime.strptime(car["time"], "%H:%M")
        minute_diff = calculate_time_diff(car_in_time, car_out_time)
        car["total_minute"] += minute_diff
    return car


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                                      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
