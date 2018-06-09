def sum_of_multiples(limit, multiples):
    m_list = []
    try:
        for m in multiples:
            for i in range(1, limit//m + 1):
                if i*m < limit and i*m not in m_list:
                    m_list.append(i*m)
    except ValueError:
        return 'Invalid input!'
    return sum(m_list)
