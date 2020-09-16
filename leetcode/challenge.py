from datetime import datetime



def challenge(offers):
    type_offers = []
    for offer in offers:
        offer = offer.split()
        offer[0] = datetime.strptime(offer[0], '%m/%d').date()
        offer[1] = datetime.strptime(offer[1], '%m/%d').date()
        offer[2] = int(offer[2])

        type_offers.append(offer)
    
    best_offer = type_offers[0]

    for i in range(1, len(type_offers)):
        if best_offer[1] < type_offers[i][0]:
            break

        if best_offer[2] > type_offers[i][2]:
            continue

        if best_offer[0] == type_offers[i][0] and best_offer[2] < type_offers[i][2]:
            best_offer = type_offers[i]
            continue
        
        elif best_offer[1] > type_offers[i][0] and best_offer[2] < type_offers[i][2]:
            best_offer = type_offers[i]
            continue

        elif best_offer[2] == type_offers[i][2] and best_offer[1] < type_offers[i][1]:
            best_offer = type_offers[i]
            continue

    return best_offer







print(challenge(["10/05 10/12 2400", "10/05 10/10 2500", "10/07 10/15 2300", "10/08 10/30 3000", "10/15 11/03 3000", "10/20 11/01 3500", "11/02 11/11 4000"]))

print()
print()

print(challenge(["07/01 07/30 2000", "07/01 07/15 2000", "07/01 07/30 2000", "07/01 07/30 1500", "07/05 07/30 2100", "07/20 08/01 2400", "07/20 07/31 2400", "07/31 09/01 2900", "08/01 08/15 3000", "08/14 08/19 2000","08/17 08/30 4000"]))