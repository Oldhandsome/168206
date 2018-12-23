 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 # 将题目中的条件转化成表达式
 # A:我不是小偷  ==> thief != 1
 # B:D是小偷     ==> thief == 4
 # C:B是小偷     ==> thief == 2
 # D:B诬陷我     ==> thief != 4
 
 def find_a_thief():
     true = 1
     for i in range(4):
     #只有一个人说的是真话。因此如果小偷是i的话，要num == 1 才能抓住小偷
         num = (i != 1) + (i == 4) + (i == 2) + (i != 4)
         if true == num:
             print(chr(96 + i),"是小偷")
     
 if __name__ == "__main__":
     find_a_thief()
