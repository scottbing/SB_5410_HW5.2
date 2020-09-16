def set_cover(universe, subsets):
    """Find a family of subsets that covers the universal set"""
    elements = set(e for s in subsets for e in s)
    # Check the subsets cover the universe
    if elements != universe:
        return None
    covered = set()
    cover = []
    # Greedily add the subsets with the most uncovered points
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset

    return cover


def main():
    universe = set(range(1, 11))
    subsets = [{1, 2, 3, 8, 9, 10},
               {1, 2, 3, 4, 5},
               {4, 5, 7},
               {5, 6, 7},
               {6, 7, 8, 9, 10}]

    elems = set() #create an empty set to hold the total union
    for s in subsets:
        elems |= s   #elems  = the union of items in both sets
    print(elems)
    #cover = set_cover(universe, subsets)
    #print(cover)


if __name__ == '__main__':
    main()