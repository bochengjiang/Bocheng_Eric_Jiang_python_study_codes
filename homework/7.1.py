# 7-th homework 1st question
## Learn `insert()` function which can be used in `list`;
## Use what you learned to revise the value of the variable `student_list` to ["xiaoming", "dongmei", "xiaohua", "zhangsan", "lisi"]
## The more ways the better.

student_list = ["xiaoming", "dongmei", "zhangsan", "lisi"]
#method no.1
#student_list.insert(2,"xiaohua")
#method no.2
student_list[2:2]=["xiaohua"]
print(student_list)
print(student_list[0:4])