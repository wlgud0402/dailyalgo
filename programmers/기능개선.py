import math
def solution1(progresses, speeds):
    progresses_zips = []
    times = []
    answer = []
    progresses_zips = list(zip(progresses,speeds))
    for progresses_zip in progresses_zips:
        day_count = math.ceil((100-progresses_zip[0]) / progresses_zip[1])
        times.append(day_count)
    
    print("progresses_zips:", progresses_zips, "times:", times)

    answer = []

    while times:
        deployedIdxes = [0]
        first = times[0]
        for i in range(1, len(times)):
            if times[i] <= first:
                deployedIdxes.append(i)

        print(deployedIdxes)

        answer.append(len(deployedIdxes))

        times = times[len(deployedIdxes):]

    return answer


def solution2(progresses, speeds):
    done = []
    while progresses:
        # work
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # done check
        doneJobCount = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break
            doneJobCount += 1

        if doneJobCount > 0:
            progresses = progresses[doneJobCount:]
            speeds = speeds[doneJobCount:]
            done.append(doneJobCount)

            # for i in range(doneJobCount):
            #     progresses.pop(0)
            #     speeds.pop(0)
    return done

    
print(solution1([93,30,55],[1,30,5]))
print()
print()
print(solution2([93,30,55],[1,30,5]))




