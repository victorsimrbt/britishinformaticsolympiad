#include <iostream>
#include <math.h> 

using namespace std;

int diamond_width(int n){
    if (n == 0) return 0;
    if (n < 0) return 0;
    return diamond_width(n-1)*2+1;
}

char locate_quad(pair<int,int> coord,pair<int,int> centre){
    pair<int,int> new_coord = coord;
    new_coord.first -= centre.first;
    new_coord.second -= centre.second;
    int x = new_coord.first ;
    int y = new_coord.second;

    if (y < x && y > -x)
        return 'R';
    if (y > x && y < -x)
        return 'L';
    if (y > x && y > -x)
        return 'U';
    if (y < x && y < -x)
        return 'D';
    return 'O';
}

pair<pair<int,int>,char> find_quads(pair<int,int> coord, pair<int,int> centre, int n){
    int width = round(diamond_width(n));
    char quad = locate_quad(coord,centre);
    pair<int,int> new_centre = centre;
    if (quad == 'R')
        new_centre.first = centre.first + width;
    if (quad == 'L')
        new_centre.first = centre.first - width;
    if (quad == 'U')
       new_centre.second = centre.second + width;
    if (quad == 'D')
       new_centre.second = centre.second - width;
    pair<pair<int,int>,char> return_value;
    return_value.first = new_centre;
    return_value.second = quad;
    return return_value;
}

int main(){
    int x,y;
    cin >> x >> y;
    pair<int,int> centre = {0,0};
    pair<int,int> coord;
    coord.first = x;
    coord.second = y;
    int n = 18;
    while (n > 0){
        pair<pair<int,int>,char> return_value = find_quads(coord,centre,n);
    }
    return 0;
}