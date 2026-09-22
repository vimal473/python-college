x = "variable"
def main():
    def fun():
        global x
        x = "not valid"
        print("call funcation insaid" ,x)
        val = 20
        print(val)
    fun()
main()
print("call funcation outside",x)
    
