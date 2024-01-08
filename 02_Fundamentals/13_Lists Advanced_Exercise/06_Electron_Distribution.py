number_of_electrons = int(input())
shell_list = []
shell_position = 1
while number_of_electrons > 0:
    max_electrons_in_shell = shell_position ** 2 * 2
    if number_of_electrons >= max_electrons_in_shell:
        shell_list.append(max_electrons_in_shell)
        shell_position += 1
    else:
        shell_list.append(number_of_electrons)
    number_of_electrons -= max_electrons_in_shell
print(shell_list)
