//TSP constructor

#include<iostream>
#include<fstream>
#include<time.h>
#include<stdlib.h>

#define MAX_CITIES 8
#define MAX_DIST 100

struct cityType{
	int x,y;
}cities[MAX_CITIES];

using namespace std;

int main()
{

    ofstream f1;
    f1.open("TSP.txt");
    srand(time(NULL));
    
    
    /*int city;
    
    for(city =0 ;city<MAX_CITIES; city++)
    {
        cities[city].x = rand()%MAX_DIST;
		
    	cities[city].y = rand()%MAX_DIST;
    
        f1<<cities[city].x<<" "<<cities[city].y<<" "<<std::endl;
    }*/
    
    int city, R[] = {28, 55, 42, 68, 45, 11, 74, 65, 31, 29, 65}, K[] = {19, 4, 80, 69, 45, 90, 84, 23, 29, 83, 5};
    
    for(city =0 ;city<MAX_CITIES; city++)
    {
        cities[city].x = R[city];
        
        cities[city].y = K[city];
    
        f1<<cities[city].x<<" "<<cities[city].y<<" "<<std::endl;
    }


    f1.close();

    return 0;

}
