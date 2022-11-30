def render(x,y,code):
    canvas.create_text(x+35,y+60,text=code)
    for ind in range(0,len(code)):
        canvas.create_line(x,y,x,y+50 if ind not in [0,len(code)-1] else y+70,width=int(code[ind]))
        x += 10
[globals().update({"data": open("./ciarovy_kod_1.txt", "r").read().split("\n")}),globals().update({"cur_index": -4})]+[globals().update({"root" : __import__("tkinter").Tk()})]+[root.title("Pome")]+[globals().update({"canvas":__import__("tkinter").Canvas(root, width="500", height="500")})]+[canvas.pack()]+[root.bind("<space>",lambda event: [globals().update({"cur_index":cur_index+4})]+[globals().update({"cur_index":len(data)-4}) if cur_index+4>=len(data) else ""]+[canvas.delete("all"),render(10,10,(data[cur_index:cur_index+1])[0]),render(100,10,(data[cur_index+1:cur_index+2])[0]),render(10,100,(data[cur_index+2:cur_index+3])[0]),render(100,100,(data[cur_index+3:cur_index+4])[0])])]+[root.mainloop()]