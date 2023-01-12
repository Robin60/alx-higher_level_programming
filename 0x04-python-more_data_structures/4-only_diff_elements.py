#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    st = set([])
    for ele in set_1:
        if ele not in set_2:
            st.add(ele)
    for val in set_2:
        if val not in set_1 and val not in st:
            st.add(val)
    return st
