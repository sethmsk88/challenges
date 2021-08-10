# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    # go as far as you can on a full tank of gas, then fill up
    num_refills = 0
    current_stop = 0
    dist_travelled = tank

    while dist_travelled < distance:
        # if reaching the destination or next stop is impossible
        if (current_stop >= len(stops)) or (stops[current_stop] > dist_travelled):
            return -1

        # calculate the furthest gas station we can reach on 1 tank
        while (current_stop < len(stops) - 1) and (stops[current_stop + 1] <= dist_travelled):
            current_stop += 1

        # refill gas tank
        num_refills += 1
        dist_travelled = stops[current_stop] + tank
        current_stop += 1

    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
