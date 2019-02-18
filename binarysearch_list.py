#!/usr/bin/python3

'''
Assuming a sorted list, search for a value in the list by repeatedly
bisecting it.
'''
def search_list(in_list, in_val):
    list_len = len(in_list)
    head = 0
    tail = list_len - 1

    while head <= tail:
        idx = int((head + tail) / 2)
        if in_list[idx] == in_val:
            return idx

        elif in_list[idx] > in_val:
            tail = idx - 1
        else:
            # in_list[idx] < in_val
            head = idx + 1

    return None

def search_list_rec(in_list, in_val):
    list_len = len(in_list)
    head = 0
    tail = list_len - 1

    if head == tail:
        if in_list[head] == in_val:
            return 0

        return None

    if head < tail:
        idx = int((head + tail) / 2)

        if in_list[idx] == in_val:
            return idx

        elif in_list[idx] > in_val:
            # slice the list at the midpoint,
            # removing all values including idx.
            # as the list has not changed from the head, the idx is still
            # within [0, idx) so return directly from the recursive call.
            return search_list_rec(in_list[:idx], in_val)

        else:
            # in_list[idx] < in_val
            # slice the list at the head, removing all values including idx,
            # and account for this offset with +1 on the output.
            offset_idx = search_list_rec(in_list[idx+1:], in_val)
            if offset_idx == None:
                return None

            return (idx + 1) + offset_idx

    return None
