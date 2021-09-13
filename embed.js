let print = args => {
    var buffer = ""
    for (var i of args){
        buffer = buffer + i
    }
    console.log(buffer)
}
print("Hello")