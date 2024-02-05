#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
   int n;
   cin >> n;

   vector<vector<int>> graph(n);
   queue<int> q;
   vector<int> degree(n, 0);
   vector<int> order(n, 0);

   // Populate the 'graph' vector
   for (int i = 0; i < n; i++) {
       int m;
       cin >> m;
       for (int j = 0; j < m; j++) {
           int element;
           cin >> element;
           graph[i].push_back(element);
       }
   }

   // Populate the 'degree' vector based on prerequisites
   for (int i = 0; i < n; i++) {
       for (auto element : graph[i]) {
           degree[element]++;
       }
   }

   // Add courses with indegree 0 to the queue
   for (int i = 0; i < n; i++) {
       if (degree[i] == 0) {
           q.push(i);
       }
   }

   // Perform topological sorting
   int index = 0;
   while (!q.empty()) {
       int element = q.front();
       order[index++] = element;
       q.pop();
       for (auto it : graph[element]) {
           degree[it]--;
           if (degree[it] == 0) {
               q.push(it);
           }
       }
   }

   // Check if there is a valid topological order
   if (index != n) {
      cout << "No topological order";
   } else {
      // Output the topological order
      for (auto it : order) {
          cout << it << " ";
      }
   }

   return 0;
}
