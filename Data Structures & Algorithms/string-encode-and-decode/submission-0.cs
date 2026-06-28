public class Solution {

    public string Encode(IList<string> strs) {
        StringBuilder result = new StringBuilder();
        foreach(string str in strs){
            result.Append(str.Length);
            result.Append('#');
            result.Append(str);
        }

        return result.ToString();
    }

    public List<string> Decode(string s) {
        List<string> result = new List<string>();
        if(s.Length == 0) return result;
        
        int i = 0;
        while(i < s.Length){
            int j = i;

            while(s[j] != '#'){
                j++;
            }

            int length = int.Parse(s.Substring(i, j - i));
            string str = s.Substring(j + 1, length);
            result.Add(str);
            i = j + 1 + length;
        }

        return result;
    }
}