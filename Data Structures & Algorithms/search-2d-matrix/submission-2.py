class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oleft=0
        oright=len(matrix)-1
        il=0
        ir=len(matrix[0])-1
        while oleft<=oright:
            omid = (oleft+oright)//2
            print(oleft,oright,omid)
            while il<=ir:
                imid = (il+ir)//2
                if matrix[omid][imid]==target:
                    return True
                elif matrix[omid][imid]>target:
                    ir = imid-1
                else:
                    il = imid+1
            print("out",oleft,oright)
            print("in",il,ir)
            if ir == -1:
                oright = omid-1
            else:
                oleft = omid+1
            il=0
            ir=len(matrix[0])-1
        return False


        