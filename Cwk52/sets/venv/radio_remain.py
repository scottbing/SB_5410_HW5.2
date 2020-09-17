import math


def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    # elements = set(e for s in subsets for e in s)
    elements = set([e for st in subsets.items() for e in st[1][0]])
    # Check the subsets cover the universe
    if universe.issubset(elements) is not True:
        return None
    covered = set()
    cover = []

    # Greedily add the subsets with the most uncovered points
    while universe.issubset(covered) is not True:
        # for every suset in subsets find ethe length of the amount of new items it covers
        # choose the subset that covers most new items

        best_station = None  # which is the best station at eachh step?
        best_new_cover = math.inf  # how much new area does that station cover?

        for station in subsets.keys():  # for each station name
            st_cov = subsets[station][0]  # find out what that station covers
            st_cost = subsets[station][1]  # find what station costs

            remaining_needs = universe - covered  # how much of universe uncovered
            new_stations_covered = st_cov - covered #how many new stations will this cover
            actual_new_coverage = remaining_needs & new_stations_covered    #are those needed stations?
            diff_cov = len(actual_new_coverage)  # how much actual new coverage would be purchased?

            if diff_cov != 0:  # if the chosen station covers the most of all subsets
                cost_per_cover = st_cost / diff_cov
                if cost_per_cover < best_new_cover:  # if the chosen station covers the most of all subsets
                    best_new_cover = cost_per_cover  # store its amount of coverage
                    best_station = station  # store the station name
        # end for

        cover.append(best_station)  # append station name to the list to tell the user
        covered |= subsets[best_station][0]  # append station coverage to the set of all covered states

    return cover


# end def set_cover(universe, subsets):

def main():
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    #states_needed = {"mt"}

    stations = {"kone": [{"id", "nv", "ut"}, 12],
                "ktwo": [{"wa", "id", "mt"}, 3],
                "kthree": [{"or", "nv", "ca"}, 19],
                "kfour": [{"nv", "ut"}, 7],
                "kfive": [{"ca", "az"}, 1]
                }

    cover = set_cover(states_needed, stations)
    print(cover)


# end def main():

if __name__ == '__main__':
    main()
