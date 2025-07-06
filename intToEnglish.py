# TC: O(1)
# SC: O(1)
class Solution:
    def numberToWords(self, num: int) -> str:
        below_20=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
                    'Eighteen', 'Nineteen']
        tens=['dummy', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        if num==0:
            return 'Zero'

        trios=[]
        def trio(num, prev, p):
            nonlocal below_20, tens, trios
            #base
            if p>4:
                return
            curr_str=""
            curr=num%(1000**p)-prev
            if curr>=1000:
                curr//=(1000**(p-1))
            if curr>0:
                huns=curr//100
                #Hundreds
                if huns>0:
                    curr_str+=below_20[huns-1]+" Hundred "
                two_digs=curr%100
                #Two digits
                if two_digs>0:
                    if two_digs<20:
                        curr_str+=below_20[two_digs-1]+" "
                    else:
                        #Tens
                        ten=two_digs//10
                        curr_str+=tens[ten-1]+" "
                        #Ones
                        ones=two_digs%10
                        if ones>0:
                            curr_str+=below_20[ones-1]+" "
            trios.append(curr_str)
            prev=num%(1000**p)
            trio(num,prev,p+1)
        
        trio(num,0,1)
        res=""
        #Billions
        if len(trios[3])>0:
            res=trios[3]+"Billion "

        #Millions
        if len(trios[2])>0:
            res+=trios[2]+"Million "
        
        #Thousands
        if len(trios[1])>0:
            res+=trios[1]+"Thousand "
        
        #Hundreds
        if len(trios[0])>0:
            res+=trios[0].strip()
        
        return res.strip()

                
                
