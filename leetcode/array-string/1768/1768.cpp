class Solution {
  public:
      string mergeAlternately(string word1, string word2) {
          int n = word1.length() + word2.length();
          std::string word3(n, '\0');
  
          for(int i = 0; i <= n; i++){
              if(i%2==0 && word1.length() > 0 || word2.length() < 1){
                  word3[i] = word1[0];
                  word1.erase(0,1);
              } else {
                  word3[i] = word2[0];
                  word2.erase(0,1);
              }
          }
  
          return word3;
      }
  };