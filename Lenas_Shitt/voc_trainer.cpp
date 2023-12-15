#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include "list.hpp"
#include "node.hpp"

int main(){

/**********************************/
/******* read vocab file *******/
/**********************************/
        std::string ctr, line;
        //first read the conrols file
        std::fstream file("Voc6.csv", std::ios::in);
        //csvread.open("../voc.csv");
        //read file and cut at ","
        List<std::string> voc;
        if (file.is_open()){
            
            while(getline(file,line)){
                // we create a stringstream to seperate the command from the description
                std::stringstream str(line);
                List<std::string> T;
                while (getline(str, ctr, ',')){
                    //std::cout << ctr << std::endl;
                    T.push(ctr);
                }
                //std::cout << (*T.begin()).get_name() << std::endl;
                // we add the command and description to the control list
                voc.push((*T.next(T.first())).get_name(),(*T.begin()).get_name());
                std::cout << (*T.begin()).get_name() << std::endl;
                std::string mull;
                std::getline(std::cin, mull);                
                if(mull=="0"){
                    return 0;
                }
                /*std::string what;
                std::cin >> what;
                if (what=="y"){
                    voc.push((*T.next(T.first())).get_name(),(*T.begin()).get_name());
                }*/
                std::cout << (*T.next(T.first())).get_name() << std::endl;


            }
            
        }
        else{
            std::cerr << "Error!" << std::endl;
            //we include three commands so that we will not get problems later
        }
        file.close();




}