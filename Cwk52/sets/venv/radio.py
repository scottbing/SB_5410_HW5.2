def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    #elements = set(e for s in subsets for e in s)
    elements = set([e for st in subsets.items() for e in st[1]])
    # Check the subsets cover the universe
    if elements != universe:
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        # subset = max(subsets, key=lambda s: len(s - covered))
        # cover.append(subset)
        # covered |= subset

        best_station = None #which is the best station at eachh step?
        best_new_cover = 0  #how much new area does that station cover?
        for station in subsets.keys():  #for each station name
            st_cov = subsets[station]   #find out what that station covers
            diff_cov = len(st_cov - covered)    #ho much f  what that station covers is already covered?
            if diff_cov > best_new_cover: # if the chosen station covers the most of all subsets
                best_new_cover = diff_cov   #store its amoutn of coverage
                best_station = station  #store the station name
        #end for

        cover.append(best_station)  #append station name to the list to tell the user
        covered |= subsets[best_station]    #append station coverage to the set of all covered states

    return cover
#end def set_cover(universe, subsets):

def main():

    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = {"kone": {"id", "nv", "ut"},
                "ktwo": {"wa", "id", "mt"},
                "kthree": {"or", "nv", "ca"},
                "kfour": {"nv", "ut"},
                "kfive": {"ca", "az"}
                }
    # print(stations)
    # print([e for st in stations.items() for e in st[1]])

    cover = set_cover(states_needed, stations)
    print(cover)
#end def main():

if __name__ == '__main__':
    main()