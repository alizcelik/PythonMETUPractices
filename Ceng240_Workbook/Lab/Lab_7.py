def accounting(filename):
    total_expense = int()
    total_income = int()
    max_company_name = str()
    max_profit = int()
    return_list = list()

    with open(filename, 'r') as f:
        for line in f:
            cells = line.split(',')
            company = cells.pop(0)
            company_profit = int()
            for cell in cells:
                record = cell.split(':')
                if record[1] == 'I':
                    company_profit += int(record[2])
                    total_income += int(record[2])
                else:
                    company_profit -= int(record[2])
                    total_expense += int(record[2])

            if company_profit > max_profit:
                max_company_name = company

    return_list.append(total_income)
    return_list.append(total_expense)
    return_list.append(max_company_name)
    return return_list

print(accounting('records.txt'))

