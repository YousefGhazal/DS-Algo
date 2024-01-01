#include <iostream>
using namespace std;
#include <cstdlib>

bool allocstr(int len, char** retptr)
{
    char* p = static_cast<char*>(std::malloc(len + 1)); // +1 for '\0'
    if(p == nullptr)
        return false;
    *retptr = p;
    return true;
}

int main()
{
    
}