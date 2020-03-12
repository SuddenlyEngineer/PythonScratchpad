def towers_of_hanoi(from_peg, to_peg, spare_peg, disks=4):
    if disks == 1:
        print(f"Move from {from_peg} to {to_peg}")
        pass
    else:
        towers_of_hanoi(from_peg, spare_peg, to_peg, disks-1)
        print(f"Move from {from_peg} to {to_peg}")
        towers_of_hanoi(spare_peg, to_peg, from_peg, disks-1)

towers_of_hanoi('a', 'c', 'b', 4)