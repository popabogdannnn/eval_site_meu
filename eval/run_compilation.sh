
cp main.cpp compilation_jail

ia-sandbox -r /media/bogdan/0C4E0E4A4E0E2CD0/work/Linux/cpp/eval_site_meu/eval/compilation_jail --forward-env\
 --mount /lib:/lib:exec\
 --mount /lib64:/lib64:exec\
 --mount /usr/bin:/usr/bin:exec\
 --mount /usr/lib:/usr/lib:exec\
 --mount /usr/include:/usr/include\
 --memory 128mb --stack 128mb -o json --time 10s --wall-time 12s --stderr output\
 usr/bin/g++ -- -Wall -static -std=c++14 main.cpp -o main



