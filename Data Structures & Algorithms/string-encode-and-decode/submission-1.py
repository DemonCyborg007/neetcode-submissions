class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for i in strs:
            for j in i:
                encoded_s+=j
            encoded_s+="kill01$"
        # print(encoded_s)
        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded_l=[]
        st=""
        count = 0
        flag=0
        for i in range(len(s)):
            # print(i)
            # st+=i
            bb=s[i:i+7]
            # print(bb)
            
            
            if flag == 1 and count!=6:
                # print(count)
                count+=1
                continue

            if bb == "kill01$":
                # print(st)
                decoded_l.append(st)
                st=""
                flag=1
                count=0
            else:
                st+=s[i]
        # print(decoded_l)
        return decoded_l
