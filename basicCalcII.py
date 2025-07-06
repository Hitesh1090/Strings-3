# TC: O(n)
# SC: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        numq=deque([])
        symq=deque([])
        i=0
        while i<len(s):
            curr_num=0
            num_flag=False
            while i<len(s) and s[i].isnumeric() :
                num_flag=True
                curr_num=curr_num*10+int(s[i])
                i+=1
            if num_flag:
                numq.append(curr_num)
            if i<len(s):
                if s[i]==" ":
                    i+=1
                else:
                    symq.append(s[i])
                    i+=1

        cval=tail=numq.popleft()
        while len(symq)>0:
            sym=symq.popleft()
            num=numq.popleft()
            if sym=="+":
                cval=cval+num
                tail=num
            
            elif sym=="-":
                cval=cval-num
                tail=-num
            
            elif sym=="*":
                cval=(cval-tail)+(tail*num)
                tail=tail*num

            else:
                cval=(cval-tail)+int(tail/num)
                tail=int(tail/num)
        return cval


                    


