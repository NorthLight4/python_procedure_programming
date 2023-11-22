# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter=','):
    first_group = first_group.split(delimiter)
    second_group = second_group.split(delimiter)
    general_group = list(set(first_group)&set(second_group))
    return sorted(general_group)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_general_group = find_common_participants(participants_first_group,participants_second_group,'|')
print(participants_general_group)