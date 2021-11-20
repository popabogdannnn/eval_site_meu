(g++ -Wall -std=c++14 main.cpp -o main) &> compilation_message.txt

if [ $? == 0 ]; 
then
    echo "Compilation succesful"    
else
    echo "Compilation error"
fi