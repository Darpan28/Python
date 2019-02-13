cppCode = """
#include<iostream>
using namespace std;
int main(){
    return 0;
}
"""

print(cppCode)

file = open("Myprog.cpp","w")
file.write(cppCode)
print("Data is written")
file.close()
