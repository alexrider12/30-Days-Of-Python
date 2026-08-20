int_userAge, int_a, int_b = 0, 1, 3
list = ["a", "B", "CC","DD"]
int_adminAge = 20
#print(type(alter))
dict_input = {
    int_userAge: "Please enter your age:\n",
    int_a: "Please enter a number: \n",
    int_b: "Please enter another number: \n"
}
print("a")
for _input in dict_input.keys():
    print(list[int(_input)])