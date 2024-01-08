# version = list(map(int, input().split(".")))
# version[-1] += 1
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#         if index - 1 >= 0:
#             version[index - 1] += 1
#
# new_version = ".".join(list(map(str, version)))
# print(new_version)
version = input()
version_int = version.replace(".", "")
next_version = int(version_int) + 1
print(".".join(str(next_version)))
