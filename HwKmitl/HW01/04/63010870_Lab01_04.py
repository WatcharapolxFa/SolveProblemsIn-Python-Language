def num_grid(lst):
    # code Here
    lst_Game = [
        ["_", "_", "_", "_", "_", ],
        ["_", "_", "_", "_", "_", ],
        ["_", "_", "_", "_", "_", ],
        ["_", "_", "_", "_", "_", ],
        ["_", "_", "_", "_", "_", ]
    ]
    for loop in range(5):
        for looP in range(5):
            counts = 0
            if lst[loop][looP] == "-":
                if loop > 0:
                    if lst[loop - 1][looP] == "#":
                        counts = counts + 1
                if looP > 0:
                    if lst[loop][looP-1] == "#":
                        counts = counts + 1
                if loop < 4:
                    if lst[loop + 1][looP] == "#":
                        counts = counts + 1
                if looP < 4:
                    if lst[loop][looP+1] == "#":
                        counts = counts + 1
                if loop > 0 and looP > 0:
                    if lst[loop - 1][looP-1] == "#":
                        counts = counts + 1
                if loop < 4 and looP > 0:
                    if lst[loop + 1][looP-1] == "#":
                        counts = counts + 1
                if loop < 4 and looP < 4:
                    if lst[loop + 1][looP+1] == "#":
                        counts = counts + 1
                if loop > 0 and looP < 4:
                    if lst[loop - 1][looP+1] == "#":
                        counts = counts + 1
                lst_Game[loop][looP] = str(counts)
            if lst[loop][looP] == "#":
                lst_Game[loop][looP] = "#"
    return lst_Game


lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
    lst_input.append([i for i in e.split()])  # append == ใส่เข้าจากบนลงล่าง

# sep="\n" == เปลี่ยนจาก , หลังของแต่ละ list เป็นขึ้นบรรทัดใหม่ Ex >> $$
print("\n", *lst_input, sep="\n")

print("\n", *num_grid(lst_input), sep="\n")


# lst_input = [

#     ["-", "-", "-", "-", "-"], << $$

#     ["-", "-", "-", "-", "-"],

#     ["-", "-", "#", "-", "-"],

#     ["-", "-", "-", "-", "-"],

#     ["-", "-", "-", "-", "-"]

# ]
