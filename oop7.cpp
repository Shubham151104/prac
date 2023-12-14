#include<iostream>
#include<map>
#include<string>


using namespace std;

int main()
{
    map <string, int> populationMap;
    
    populationMap.insert(pair<string, int>("MH", 112));
    populationMap.insert(pair<string, int>("UP", 199));
    populationMap.insert(pair<string, int>("MP", 726));
    populationMap.insert(pair<string, int>("AP", 845));
    
    map<string,int>::iterator iter = populationMap.end();
  
    //output the size of the mapType
    cout<<"Size of populationMap:"<<populationMap.size()<<"\n";
    
    for(iter=populationMap.begin(); iter!=populationMap.end(); ++iter)
    {
        cout<<iter->first<<":"<<iter->second<<"million\n";
    }
    //find will return an iterator to the matching element if it is found 
    //or to the end of the map if the key is not found 
    string state;
    cout<<"\nEnter the state:";
    cin>>state;
    
    iter = populationMap.find(state);
    if(iter!=populationMap.end())
        cout<<state<<"population is:"<<iter->second<<"million\n";
    else
    cout<<"Key is not in populationMap";
    
    //clear the entries in the Map
    populationMap.clear();
    
    return 0;
}
