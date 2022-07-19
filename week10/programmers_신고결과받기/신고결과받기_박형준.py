def solution(id_list, report, k):
    report = list(set(report))
    rpt_list = [[] for _ in range(len(id_list))]
    for id in report:
        a, b = id.split()
        x = id_list.index(b)
        rpt_list[x].append(a)

    ans_list = [0 for _ in range(len(id_list))]
    for rpt in rpt_list:
        if len(rpt) >= k:
            y = rpt_list.index(rpt)
            for id in rpt:
                z = id_list.index(id)
                ans_list[z] += 1

    return ans_list
