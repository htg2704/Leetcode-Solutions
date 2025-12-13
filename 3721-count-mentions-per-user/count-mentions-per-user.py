class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans = [0]*n
        online = [1]*n
        events.sort(key=lambda x:(int(x[1]), x[0]!="OFFLINE"))
        for mes, time, id in events:
            if mes=="OFFLINE":
                online[int(id)]=int(time)+60
            else:
                if id!="HERE" and id!="ALL":
                    for i in id.split(" "):
                        ids = int(i[2:])
                        ans[ids]+=1
                elif id=="ALL":
                    for i in range(n):
                        ans[i]+=1
                else:
                    for i in range(n):
                        if(online[i]<=int(time)):
                            ans[i]+=1

        return ans