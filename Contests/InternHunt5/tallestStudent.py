"""

Intern Hunt 5.0

The Tallest Student
-------------------

In a classroom, there are several tall students so there is always a dispute regarding who is taller.

A student in the class suggested the following algorithm to resolve the problem. There are flaws in the process of course, but hear me out.

First, line up all the students in the class
Each student in the line calls out the number of students he or she can see in front of him/her.
Note that a student A (with height i) cannot see past student B (with height j) if j > = i .
The student who can see the most number in front is considered to be the tallest
In case of any ties, the student whose index position in the line is the greatest is considered to be the tallest
Indexing begins from 1
Write a program that implements this algorithm.
More clarity can be obtained from the test case.

Constraints

0 <= T <= 4000
0 <= number of students <= 1000
0 <= heights of students <= 150 (in cm)
Sample Input Format

The first Line conatins T number of test cases.
The second Line contains the number of students for each test case.
The third Line contains space separated heights of students.
Sample Output Format

Output for each test case contains the tallest student of the class according to the algorithm outlined
Sample Input

4
5
5 4 3 1 2
6
3 2 1 5 4 1
7
3 2 1 5 4 1 2
7
5 2 1 5 4 1 2
Sample Output

1
1
4
4
Explanation

In the second test case the number of students standing in a row are 6. The student at position 1 can see 3 students
ahead of him, i.e., 2, 1 and 5. He cannot see beyond 5.
Hence the tallest student would be at position 1.
In the third test case, the student at position 1 can see 3 students ahead of him. The student at position 4 can see 3 students ahead of him. So, the student at position
4 is considered to be the tallest because the index position is greater.
Similar logic applies in the fourth test case.
"""

def calculateSpan(arr):
    n = len(arr)
    st = [n-1]
    S = [0] # last element always can see himself only
    for i in range(n-2, -1, -1):
        while (len(st) > 0 and arr[st[-1]] < arr[i]):
            st.pop(-1)
        if len(st) == 0:
            #print("A")
            S.insert(0, n-i-1)
            #print(S)
        else:
            #print("B")
            S.insert(0, st[-1]-i)
            #print(S)
        st.append(i)
    return S

def getTallest(arr):
    get_spans = calculateSpan(arr)
    maxindex = -1
    maxval = -1
    n = len(get_spans)
    if n<=1:
        return n
    for i in range(n-1, -1, -1):
        if get_spans[i] > maxval:
            maxval = get_spans[i]
            maxindex = i + 1
    return maxindex

def main():
    for _ in range(int(input())):
        n = input()
        arr = [int(x) for x in input().strip().split()]
        print(getTallest(arr))
main()

'''
print(getTallest([5,4,3,1,2])) #1
print(getTallest([3,2,1,5,4,1])) #1
print(getTallest([3,2,1,5,4,1,2])) #4
print(getTallest([5,2,1,5,4,1,2])) #4
'''