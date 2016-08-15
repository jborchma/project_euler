def find_div_sum(n):
    div_list = []

    for i in range(1,n//2+1):
        if n % i == 0:
            div_list.append(i)

    return sum(div_list)

tupel_list = dict( ((n,find_div_sum(n) )) for n in range(2,10000) )

summe = sum(n for n in range(2,10000) if tupel_list.get(tupel_list[n]) == n and tupel_list[n] != n  )

print(summe)

